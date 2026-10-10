#!/usr/bin/env python3
"""Reproducible descriptive analysis of the AsteriaGrid Information Warfare dataset.

Author: Information Warfare Analyst
Course: IE4032 - Information Cyberwarfare

Reads raw social media posts, reconstructs the propagation graph,
computes degree centrality, betweenness centrality, and PageRank,
and exports timeline.csv, network_nodes.csv, network_edges.csv, and DOT graph.
"""

import argparse
import hashlib
import os
import re
from pathlib import Path

import pandas as pd
import networkx as nx

ALIASES = {
    "id": ["post_id", "id", "tweet_id", "record_id"],
    "time": ["timestamp", "created_at", "date_time", "datetime", "time"],
    "parent": ["parent_post", "parent_id", "parent_post_id", "in_reply_to"],
    "account": ["account", "account_id", "username", "user", "author"],
    "text": ["text", "content", "post_text", "message"],
    "channel": ["channel", "platform", "medium"],
    "repost_count": ["repost_count", "retweets", "shares"],
    "reply_count": ["reply_count", "replies", "comments"],
    "image_id": ["image_id", "media_id", "attachment"],
}


def norm(s):
    return re.sub(r"[^a-z0-9]+", "", str(s).lower())


def find_col(columns, key, required=True):
    lookup = {norm(c): c for c in columns}
    for a in ALIASES[key]:
        if norm(a) in lookup:
            return lookup[norm(a)]
    if required:
        raise ValueError(f"Could not identify column for key: {key}")
    return None


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    parser = argparse.ArgumentParser(description="Analyze AsteriaGrid Information Warfare dataset.")
    parser.add_argument("--input-dir", type=Path, default=Path("data"))
    parser.add_argument("--output-dir", type=Path, default=Path("outputs"))
    args = parser.parse_args()

    posts_file = args.input_dir / "social_media_posts.csv"
    if not posts_file.exists():
        raise SystemExit(f"Input file not found: {posts_file}")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(posts_file, dtype=str, keep_default_na=False)

    col_id = find_col(df.columns, "id")
    col_time = find_col(df.columns, "time")
    col_parent = find_col(df.columns, "parent", required=False)
    col_acc = find_col(df.columns, "account", required=False)
    col_text = find_col(df.columns, "text", required=False)
    col_chan = find_col(df.columns, "channel", required=False)
    col_reposts = find_col(df.columns, "repost_count", required=False)
    col_replies = find_col(df.columns, "reply_count", required=False)
    col_img = find_col(df.columns, "image_id", required=False)

    df["_id"] = df[col_id].str.strip()
    df["_time_utc"] = pd.to_datetime(df[col_time], errors="coerce", utc=True)
    
    # 1. Timeline export
    timeline_cols = [col_time, "_time_utc", "_id"]
    for c in [col_acc, col_chan, col_parent, col_reposts, col_replies, col_img, col_text]:
        if c:
            timeline_cols.append(c)
    
    df_timeline = df.sort_values("_time_utc", na_position="last")[timeline_cols]
    df_timeline.rename(columns={
        col_time: "timestamp_original",
        "_time_utc": "timestamp_utc",
        "_id": "post_id"
    }).to_csv(args.output_dir / "timeline.csv", index=False)

    # 2. Graph Construction
    node_ids = set(df["_id"])
    g = nx.DiGraph()

    for _, row in df.iterrows():
        g.add_node(
            row["_id"],
            account=row.get(col_acc, ""),
            channel=row.get(col_chan, ""),
            repost_count=int(row[col_reposts]) if col_reposts and row[col_reposts].isdigit() else 0,
            reply_count=int(row[col_replies]) if col_replies and row[col_replies].isdigit() else 0,
        )

    edges = []
    if col_parent:
        for _, row in df.iterrows():
            cid = row["_id"]
            pid = str(row[col_parent]).strip()
            if pid and pid in node_ids:
                g.add_edge(pid, cid)
                edges.append({"parent_post_id": pid, "child_post_id": cid})

    df_edges = pd.DataFrame(edges)
    df_edges.to_csv(args.output_dir / "network_edges.csv", index=False)

    # 3. Graph Centrality Metrics
    in_deg = dict(g.in_degree())
    out_deg = dict(g.out_degree())
    betweenness = nx.betweenness_centrality(g, normalized=True) if len(g) > 2 else {n: 0.0 for n in g}
    pagerank = nx.pagerank(g, alpha=0.85) if len(g) and g.number_of_edges() else {n: 1.0 / len(g) for n in g}

    records = []
    for n in g.nodes():
        node_attr = g.nodes[n]
        records.append({
            "post_id": n,
            "account": node_attr.get("account", ""),
            "channel": node_attr.get("channel", ""),
            "in_degree": in_deg.get(n, 0),
            "out_degree": out_deg.get(n, 0),
            "total_degree": in_deg.get(n, 0) + out_deg.get(n, 0),
            "betweenness": round(betweenness.get(n, 0.0), 6),
            "pagerank": round(pagerank.get(n, 0.0), 6),
            "repost_count": node_attr.get("repost_count", 0),
            "reply_count": node_attr.get("reply_count", 0)
        })

    df_nodes = pd.DataFrame(records)
    df_nodes.sort_values(by=["out_degree", "pagerank"], ascending=False).to_csv(
        args.output_dir / "network_nodes.csv", index=False
    )

    # 4. Export DOT graph without external dependencies (no pydot required)
    dot_path = args.output_dir / "propagation_network.dot"
    with dot_path.open("w", encoding="utf-8") as f:
        f.write("digraph AsteriaGridPropagation {\n")
        f.write("  rankdir=LR;\n")
        f.write('  node [shape=box, style="filled,rounded", fontname="Helvetica", fontsize=10, fillcolor="#f0f4f8", color="#64748b"];\n')
        f.write('  edge [color="#94a3b8", arrowsize=0.7];\n')
        for n, attr in g.nodes(data=True):
            acc = attr.get("account", "")
            out_d = out_deg.get(n, 0)
            if out_d >= 4:
                f.write(f'  "{n}" [fillcolor="#fee2e2", color="#ef4444", penwidth=2.5, label="{n}\\n{acc}\\nAmplified: {out_d}"];\n')
            elif out_d >= 3:
                f.write(f'  "{n}" [fillcolor="#fef3c7", color="#f59e0b", penwidth=1.8, label="{n}\\n{acc}\\nAmplified: {out_d}"];\n')
            else:
                f.write(f'  "{n}" [label="{n}\\n{acc}"];\n')
        for u, v in g.edges():
            f.write(f'  "{u}" -> "{v}";\n')
        f.write("}\n")

    print(f"Dataset SHA-256: {sha256_file(posts_file)}")
    print(f"Total Nodes: {g.number_of_nodes()} | Directed Edges: {g.number_of_edges()}")
    print(f"Weakly Connected Components: {nx.number_weakly_connected_components(g)}")
    print(f"Output files successfully exported to {args.output_dir}")


if __name__ == "__main__":
    main()
