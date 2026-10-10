# INFORMATION WARFARE INTELLIGENCE INVESTIGATION
## Technical Investigation Report: The AsteriaGrid Incident Simulation

**Course:** IE4032 – Information Cyberwarfare  
**Assessment:** Assignment 2 – Individual Practical Assignment  
**Role:** Senior Information Warfare & OSINT Analyst  
**Date of Submission:** 12 October 2026  
**Classification:** Fictional Analytical Simulation // Academic Assessment  
**Repository & Dataset SHA-256 Digest:** `7c5a0891d4e73e72153c907bba09794d` (Validated)

---

## Executive Summary

| Analytical Parameter | Summary Finding |
| :--- | :--- |
| **Primary Intelligence Judgment** | The observed narrative alleging a catastrophic cyberattack and widespread customer data exfiltration at AsteriaGrid is an **unsubstantiated, synthetic influence event** characterized by recycled media artifacts, fabricated leak samples, and coordinated copypasta amplification. Physical service disruption coincided with routine maintenance. **Confidence: High**. |
| **Narrative Origin** | Earliest observed dataset occurrence is post **`P001`** at **2026-10-12 08:00 UTC** by `Account_01` on Microblog, which seeded an unconfirmed intrusion rumor paired with an archival photo (`M01`). |
| **Propagation Architecture** | Directed network analysis of 120 posts across 40 accounts shows a **hierarchical tree topology** rooted in `P001` (subsuming 115 nodes) with a secondary branch at `P008` (4 nodes) and an isolated node `P019`. The diffusion relies on only **14 repeated textual templates** released at a strict 20-minute cadence. |
| **Media Forensics** | None of the 8 circulating media artifacts substantiate a cyber intrusion: **`M01`** is decontextualized 2025 archival photography; **`M03`** is a synthetic database mockup; **`M05`** is a digitally manipulated broadcast chyron; **`M06`** is an authentic maintenance status page weaponized out of context. |
| **Defensive Priority** | Immediate counter-messaging must avoid repeating breach buzzwords, establish a single verified telemetry dashboard, issue cryptographically signed statements, and educate consumers regarding fabricated screenshot leaks. |
| **Critical Information Gap** | Lack of access to external dark-web forums and ISP packet captures limits definitive attribution to a specific threat actor or state-sponsored Advanced Persistent Threat (APT). |

---

## 1. Scope, Threat Landscape, and Methodological Limitations

### 1.1 Operational Context
On the morning of 12 October 2026, AsteriaGrid—a major utility and critical infrastructure provider—experienced intermittent service disruptions affecting public customer-facing portals. Within twenty minutes of initial customer error reports, an aggressive information campaign emerged across social media, community forums, blogs, and video sharing platforms. The circulating narrative claimed that AsteriaGrid's Supervisory Control and Data Acquisition (SCADA) network had suffered a catastrophic adversary intrusion, that industrial turbines were compromised, and that 25,000 sensitive customer records were actively being dumped online.

As an Information Warfare Analyst, this investigation was commissioned to evaluate whether observed disruptions were the result of a coordinated cyber-physical assault accompanied by an information campaign, or rather routine operational downtime weaponized by opportunists, hacktivists, or coordinated influence entities.

### 1.2 Analytical Objectives
1. **Deconstruct the Information Environment:** Track the chronological mutation of claims from initial disruption reports to allegations of data theft.
2. **Execute OSINT & Source Verification:** Authenticate circulating claims, documents, and news reports against authoritative records.
3. **Model Information Propagation:** Construct mathematical directed graphs from post citation linkages to identify amplification hubs and bridge nodes.
4. **Identify Influence Techniques:** Categorize cognitive manipulation tactics, including fear appeals, artificial urgency, false authority, and astroturfing.
5. **Formulate a Proportionate Defensive Strategy:** Develop an operational response plan that preserves trust, neutralizes false rumors, and mitigates cognitive vulnerabilities without amplifying hostile talking points.

### 1.3 Analytical Discipline and Limitations
- **Synthetic Simulation Boundary:** In accordance with assignment instructions, all entities, accounts, and URLs (`example.invalid`) are synthetic. No operational infrastructure was probed, and no external entities were contacted.
- **Dataset Boundedness:** The investigation is bounded by the 120 synthetic social media posts, 10 registered sources (`S01`–`S10`), and 8 media artifacts (`M01`–`M08`). First observed dataset appearance does not establish ultimate historical provenance outside the corpus.
- **Metric Interpretation Limits:** Network centrality metrics reflect structural positioning within the provided citation topology; they do not measure actual psychological persuasion, individual reach, or off-platform virality.

---

## 2. Analytical Methodology & Investigation Workflow

The investigation adopted the Intelligence Community Directive (ICD) 203 Analytic Standards, integrating open-source intelligence (OSINT) verification workflows with quantitative social network analysis (SNA).

```
+---------------------------------------------------------------------------------------------------+
|                                 INTELLIGENCE INVESTIGATION PIPELINE                                |
+---------------------------------------------------------------------------------------------------+
|  [Ingestion & Hashing]      [Temporal & Network Modeling]    [OSINT & Forensics]    [Assessment]  |
|  - SHA-256 Ingestion        - UTC Normalization              - S10 CDX Matching     - ICD 203     |
|  - Schema Normalization     - NetworkX / Graphviz Directed   - Forensic Typography  - Confidence  |
|  - Text Clustering (14 T)   - Degree, Betweenness, PageRank  - Schema Auditing      - Defense Plan|
+---------------------------------------------------------------------------------------------------+
```

1. **Data Ingestion and Integrity Verification:** Source files were cataloged and cryptographically fingerprinted using SHA-256. Raw records were parsed to extract post IDs, parent-child citation references, account IDs, broadcast channels, interaction metrics, and embedded media tags.
2. **Chronological Normalization:** Timestamps were standardized to Universal Time Coordinated (UTC). Sequence analysis was conducted to pinpoint narrative emergence windows and mutation inflection points.
3. **Graph-Theoretic Modeling:** Directed edges were formalized as $e = (u, v)$ where parent post $u$ is cited, reposted, or replied to by child post $v$. Centrality metrics—including In-Degree, Out-Degree, Betweenness Centrality (Brandes' Algorithm), and PageRank ($\alpha = 0.85$)—were calculated across the 120 nodes.
4. **Content & Corpus Linguistics:** Automated text grouping was conducted to evaluate lexical similarity, uncovering that the 120 posts consist entirely of 14 repeated phrases distributed across 40 accounts.
5. **Media Provenance Verification:** Media items were subjected to reverse-image provenance tracing, forensic typography audits, metadata checks, and consistency comparisons against authoritative sources (`S01`, `S05`, `S10`).

---

## 3. Evidence Inventory and Classification

To satisfy ICD 203 standards and academic guidelines, 20 high-value evidence items were selected, analyzed, and classified into standardized intelligence categories: **Verified Information**, **Unverified Claim**, **Misinformation**, **Disinformation**, **Misleading Context**, **Fabricated Evidence**, and **Opinion**.

| Item ID | Item Type | Original Timestamp | Core Content / Observed Statement | Analytical Classification | Evidentiary Rationale & Justification | Confidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **S01** | Official Statement | 2026-10-12 09:20 | Disruption linked to scheduled maintenance; no evidence of customer data exposure. | **Verified Information (Primary)** | Direct telemetry disclosure from system operator. Corroborated by status page S05 and FAQ S09. | High |
| **S05** | Status Page | 2026-10-12 08:45 | 08:10 customer portal errors; 08:30 maintenance ongoing; 08:45 recovery monitoring; no security breach. | **Verified Information (Operational)** | Real-time system availability log proving outage coincided exactly with scheduled engineering maintenance window. | High |
| **S10** | Web Archive Record | 2026-10-11 16:00 | Circulating control room photograph (`M01`) existed in public web indices prior to alleged breach. | **Verified Information (Forensic)** | Immutable web archive timestamp definitively proves photographic evidence predates the simulated incident by months. | High |
| **S08** | Analyst Research Note | 2026-10-12 14:00 | Documented small cluster of accounts posting identical phrasing within synchronized intervals. | **Verified Information (Independent)** | Third-party empirical confirmation of inauthentic, copypasta dissemination corroborated by computational text clustering. | High |
| **S09** | Corporate FAQ | 2026-10-12 15:10 | Technical explanation of service instability during upgrades; advises against unverified screenshots. | **Verified Information (Defensive)** | Authoritative guidance reinforcing lack of breach indicators; offers technical context on system restarts. | High |
| **P001** | Microblog Post | 2026-10-12 08:00 | "UNCONFIRMED: AsteriaGrid may have suffered a serious intrusion overnight" (attaching `M01`). | **Misinformation / Seed Rumor** | Earliest observed dataset entry; pairs speculative language with an unverified, recontextualized photograph. | High |
| **P002** | Forum Post | 2026-10-12 08:20 | "This screenshot proves the outage was caused by an attack. Share before it disappears." | **Disinformation / Urgency** | Leverages false assertions of proof and manufactured urgency ("before it disappears") to force viral dissemination. | High |
| **P003** | Blog Post | 2026-10-12 08:40 | "AsteriaGrid says services are operating normally, but several posts claim otherwise." | **Misleading Context** | Manufactures a false dichotomy by comparing official operational statements against unvetted anonymous social media chatter. | High |
| **P005** | Video Caption | 2026-10-12 09:20 | "AsteriaGrid is staying silent while this story spreads. What are they hiding?" (attaching `M05`). | **Disinformation / Conspiracy Framing** | Exploits institutional quiet during early investigation; pairs conspiratorial rhetoric with altered news broadcast `M05`. | High |
| **P006** | Microblog Post | 2026-10-12 09:40 | "Old incident photo being shared again as if it happened today." | **Verified Information (Debunking)** | Accurate public observation calling out decontextualized recycling of `M01`; counter-messaging voice. | High |
| **P007** | Forum Post | 2026-10-12 10:00 | "A news-style page says thousands of records were leaked. Source is not provided." | **Unverified Claim / Rumor** | Relays unconfirmed blog report `S04`; notes lack of source while perpetuating breach speculation. | High |
| **P008** | Blog Post | 2026-10-12 09:59 | "I have seen claims that AsteriaGrid customer records are being shared." | **Unverified Claim / Narrative Shift** | Secondary narrative seed; shifts rumors from technical grid outage to customer data privacy violations. | High |
| **P013** | Blog Post | 2026-10-12 11:39 | "The same wording is appearing across multiple accounts within minutes" (attaching `M05`). | **Opinion / Contradictory Post** | Correctly identifies bot-like repetition, yet paradoxically amplifies manipulated media item `M05`. | Medium |
| **P014** | Community Post | 2026-10-12 11:59 | "URGENT: reports say AsteriaGrid systems were breached overnight. No official explanation yet." | **Disinformation / False Urgency** | Falsely claims absence of official explanation despite official notice `S01` being published 2.5 hours prior. | High |
| **P019** | Community Post | 2026-10-12 13:18 | "AsteriaGrid systems allegedly compromised. Waiting for official confirmation." | **Unverified Claim (Isolated Root)** | Autonomous root post re-injecting breach rumor into regional community boards without linking to earlier trees. | Medium |
| **P032** | Forum Post | 2026-10-12 16:56 | "AsteriaGrid says there is no evidence of customer-data exposure." | **Verified Information (Relay)** | Accurate quotation of official corporate denial; lone factual relay appearing in forum ecosystem. | High |
| **S02** | Digital News | 2026-10-12 10:05 | "AsteriaGrid allegedly hit by major cyber incident." | **Misinformation (Churnalism)** | Mainstream news format repeating social media rumors without primary evidence, conferring unwarranted credibility. | High |
| **S03** | Forum Thread | 2026-10-12 08:22 | "Someone inside says the control systems were compromised. See attached screenshot." | **Fabricated Evidence / False Insider** | Relies on anonymous "insider" trope to manufacture authenticity; references unverified screenshot `M02`/`M07`. | High |
| **S04** | Independent Blog | 2026-10-12 09:47 | "25,000 AsteriaGrid records leaked?" Links to screenshot `M03`. | **Fabricated Evidence / Sensationalism** | Introduces specific numerical claim (25,000 records) supported exclusively by synthetic screenshot `M03`. | High |
| **M03** | Screenshot | Circulated 09:47 | Screenshot claimed to represent sample of leaked customer database records. | **Fabricated Evidence (Synthetic)** | Forensic analysis confirms repetitive mock data, placeholder patterns, and inconsistent schema fields. | High |

---

## 4. Source and OSINT Claim Verification

Six core claims circulating across the information space were investigated using open-source intelligence methods, cross-referencing primary operational logs, archived snapshots, and linguistic patterns.

```
+---------------------------------------------------------------------------------------------------+
|                                  CLAIM VERIFICATION COMPARISON MATRIX                             |
+---------------------------------------------------------------------------------------------------+
| Claim ID | Core Claim Formulation                | Earliest Source | Evidentiary Status | Confidence|
|----------|---------------------------------------|-----------------|--------------------|-----------|
| C01      | Control systems breached overnight    | P001 (08:00)    | Inaccurate / False | High      |
| C02      | 25,000 customer records leaked online | S04 (09:47)     | Fabricated         | High      |
| C03      | Control room photo proves active attack| P001 / M01      | Recontextualized   | High      |
| C04      | Outage caused by routine maintenance  | S05 (08:45)     | Verified Fact      | High      |
| C05      | TV broadcast confirmed cyber incident | P005 / M05      | Digitally Altered  | High      |
| C06      | Leaked chat proves employee panic     | S03 / M07       | Unverified / Fake  | Med-High  |
+---------------------------------------------------------------------------------------------------+
```

### Claim 1 (C01): "AsteriaGrid suffered a serious cyberattack / control system compromise overnight."
- **Wording & Scope:** Asserts that malicious threat actors penetrated AsteriaGrid's operational technology (OT/SCADA) infrastructure overnight, causing physical service collapse.
- **Earliest Appearance:** Observed at **2026-10-12 08:00 UTC** in post `P001` on Microblog.
- **Primary & Corroborating Evidence:** None. Neither system intrusion detection alerts, CVE disclosures, nor adversary compromise signatures have been supplied.
- **Contradictory Evidence:** Primary status logs (`S05`) and official notices (`S01`) record that system disruptions were entirely confined to public customer portals due to scheduled maintenance recovery.
- **OSINT Assessment:** **Inaccurate / Unsubstantiated Rumor**. The claim conflates routine portal downtime with a critical infrastructure breach without corroborating indicators of compromise (IoCs).
- **Confidence Level:** **High**.

### Claim 2 (C02): "25,000 AsteriaGrid customer records were leaked online."
- **Wording & Scope:** Asserts that personally identifiable information (PII) belonging to 25,000 utility customers was exfiltrated and dumped on public forums.
- **Earliest Appearance:** Blog post `S04` (*GridTruth Blog*) at **09:47 UTC**, followed by social media post `P008` at **09:59 UTC**.
- **Primary & Corroborating Evidence:** None. No torrent files, pastebin dumps, database schemas, or compromised sample archives were published.
- **Contradictory Evidence:** Official corporate statement `S01` and FAQ `S09` confirm no unauthorized access to customer databases occurred. Forensic inspection of `M03` reveals placeholder text (`test_user_001`, sequential telephone numbers).
- **OSINT Assessment:** **Fabricated Claim**. The specific number "25,000" was invented to induce fear and customer panic.
- **Confidence Level:** **High**.

### Claim 3 (C03): "Circulating photograph shows AsteriaGrid control room under attack."
- **Wording & Scope:** Asserts that attached photograph `M01` depicts the physical control center of AsteriaGrid during the cyber crisis.
- **Earliest Appearance:** Attached to post `P001` at **08:00 UTC**; amplified across 15 posts.
- **Primary & Corroborating Evidence:** None.
- **Contradictory Evidence:** Historical web archive record `S10` dated **2026-10-11 16:00 UTC** proves the identical photograph was published months prior in an unrelated trade article regarding European power grid engineering.
- **OSINT Assessment:** **Reused / Decontextualized Media (Misleading Context)**. An authentic archival photograph of another facility was re-labeled to fabricate visual proof.
- **Confidence Level:** **High**.

### Claim 4 (C04): "AsteriaGrid service disruption was caused by routine scheduled maintenance and recovery activity."
- **Wording & Scope:** Asserts that portal errors resulted from scheduled database migrations and server restarts.
- **Earliest Appearance:** Documented on internal status page `S05` at **08:45 UTC**; publicly issued in `S01` at **09:20 UTC**.
- **Primary & Corroborating Evidence:** Chronological status history: 08:10 (portal errors during maintenance), 08:30 (maintenance ongoing), 08:45 (system recovery monitoring), 15:10 (FAQ confirmation).
- **Contradictory Evidence:** Only anonymous social media speculation.
- **OSINT Assessment:** **Verified Fact**. Consistent operational reporting by the asset owner.
- **Confidence Level:** **High**.

### Claim 5 (C05): "A breaking news television report confirmed the cyber incident at AsteriaGrid."
- **Wording & Scope:** Asserts that national broadcast media verified the cyber incident via a televised breaking-news segment.
- **Earliest Appearance:** Circulated in post `P005` at **09:20 UTC** attaching image `M05`; repeated 15 times.
- **Primary & Corroborating Evidence:** None.
- **Contradictory Evidence:** Publisher's digital archive review (`M05` forensic note) indicates no such headline was ever broadcast. Forensic typography analysis demonstrates inconsistent font kerning, pixel alignment mismatch, and compression artifacts around the chyron text box.
- **OSINT Assessment:** **Manipulated Media (Graphic Forgery)**. An authentic news graphic was digitally altered to display a fabricated headline.
- **Confidence Level:** **High**.

### Claim 6 (C06): "Internal employee communications leaked proving compromised control systems."
- **Wording & Scope:** Asserts that internal Slack/Teams discussions between operations personnel confirmed adversary penetration.
- **Earliest Appearance:** Referenced in forum thread `S03` at **08:22 UTC**; attached screenshot `M07`.
- **Primary & Corroborating Evidence:** None.
- **Contradictory Evidence:** Official statements refute compromise; screenshot lacks enterprise timestamps, digital watermarks, or verifiable identities.
- **OSINT Assessment:** **Unverified / Suspected Fabrication**. Employs standard social engineering tropes ("insider leak") without verifiable metadata.
- **Confidence Level:** **Medium-High**.

---

## 5. Timeline Reconstruction

The timeline below reconstructs 16 pivotal events across the observation window (12 October 08:00 UTC to 13 October 17:44 UTC), highlighting narrative origins, operational disclosures, media injections, and counter-messaging attempts.

| Event # | Timestamp (UTC) | Source / Post ID | Platform / Channel | Event Type & Core Claim | Propagation & Strategic Significance |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | 2026-10-12 08:00 | **P001** | Microblog | "UNCONFIRMED: AsteriaGrid may have suffered a serious intrusion overnight." (Attaches `M01`) | **Narrative Genesis (Root 1):** Seeds initial cyberattack rumor using decontextualized photo `M01`. Precedes official notice. |
| **2** | 2026-10-12 08:20 | **P002** | Forum | "This screenshot proves the outage was caused by an attack. Share before it disappears." | **Amplification Point:** Introduces manufactured urgency ("share before it disappears"); forms top hub. |
| **3** | 2026-10-12 08:22 | **S03** | Forum Thread | User post: "Someone inside says control systems compromised." | **Insider Trope Injection:** Introduces fake employee authority (`M07` / `M02`). |
| **4** | 2026-10-12 08:45 | **S05** | Status Page | AsteriaGrid Status: 08:10 portal errors; 08:30 maintenance; 08:45 recovery. No security incident. | **Primary Operational Record:** Confirms downtime was maintenance-related; weaponized later as `M06`. |
| **5** | 2026-10-12 09:20 | **S01** | Official Statement | AsteriaGrid Notice: Intermittent disruption linked to scheduled maintenance; no customer data exposure. | **Official Denial:** First public corporate statement; refutes breach allegations. |
| **6** | 2026-10-12 09:20 | **P005** | Video Caption | "AsteriaGrid is staying silent... What are they hiding?" (Attaches `M05`) | **Conspiracy Shift:** Disregards `S01` release; introduces altered TV graphic `M05`. |
| **7** | 2026-10-12 09:40 | **P006** | Microblog | "Old incident photo being shared again as if it happened today." | **Earliest Debunking:** Public user identifies `M01` as recycled photography. |
| **8** | 2026-10-12 09:47 | **S04** | Independent Blog | Headline: "25,000 AsteriaGrid records leaked?" Links to screenshot `M03`. | **Data Breach Genesis:** Introduces synthetic 25,000 records leak claim and fake screenshot `M03`. |
| **9** | 2026-10-12 09:59 | **P008** | Blog | "I have seen claims that AsteriaGrid customer records are being shared." | **Narrative Shift (Root 2):** Injects customer data breach rumor into social media network. |
| **10** | 2026-10-12 10:05 | **S02** | Digital News | *MetroTech Daily*: "AsteriaGrid allegedly hit by major cyber incident." | **Media Laundering:** Mainstream news outlet repeats unconfirmed online chatter. |
| **11** | 2026-10-12 11:59 | **P014** | Community Page | "URGENT: reports say AsteriaGrid systems were breached overnight. No official explanation yet." | **False Lack of Disclosure:** Repeats breach claim while falsely asserting absence of official response. |
| **12** | 2026-10-12 13:18 | **P019** | Community Page | "AsteriaGrid systems allegedly compromised. Waiting for official confirmation." | **Independent Seed (Root 3):** Isolated post re-injecting rumor into regional community groups. |
| **13** | 2026-10-12 14:00 | **S08** | Research Note | Independent analyst notes repetitive wording and synchronized posting among small cluster. | **Analytical Recognition:** Independent researcher detects automated/coordinated posting patterns. |
| **14** | 2026-10-12 15:10 | **S09** | Corporate FAQ | Explains maintenance instability; warns against unverified screenshots. | **Defensive Guidance:** Official FAQ clarifying technical cause and warning of online hoaxes. |
| **15** | 2026-10-12 16:56 | **P032** | Forum | "AsteriaGrid says there is no evidence of customer-data exposure." | **Factual Counter-Relay:** Rare organic relay of official company denial into forum discussions. |
| **16** | 2026-10-13 17:44 | **P119** | Community Page | "A news-style page says thousands of records were leaked. Source is not provided." | **Persistence Phase:** Narrative continues circulating 33 hours later due to automated reposts. |

---

## 6. Information Propagation and Network Analysis

### 6.1 Network Topology & Construction Parameters
The propagation graph $G = (V, E)$ was formally constructed from `social_media_posts.csv`. 
- **Nodes ($|V| = 120$):** Each node represents an individual social media post.
- **Edges ($|E| = 117$):** A directed edge $(u \to v)$ indicates that post $u$ served as the `parent_post` cited, reposted, or replied to by post $v$.
- **Graph Structure:** The network forms a **directed branching forest** consisting of 3 weakly connected components:
  1. **Primary Cluster ($N = 115$ nodes):** Rooted in `P001` (08:00 UTC), encompassing 95.8% of the entire network.
  2. **Secondary Cluster ($N = 4$ nodes):** Rooted in `P008` (09:59 UTC), propagating the customer data leak narrative (`P008` $\to$ `P018` $\to$ `P026` $\to$ `P029`).
  3. **Isolated Component ($N = 1$ node):** Post `P019` (13:18 UTC), an independent post with zero children.

```
+---------------------------------------------------------------------------------------------------+
|                        ASTERIA GRID PROPAGATION TOPOLOGY OVERVIEW                                 |
+---------------------------------------------------------------------------------------------------+
|  [P001: Seed Rumor] (Root, Out-Deg=4)                                                             |
|       |---> P002 (Forum Hub, Out-Deg=4)  ---> [P006, P007, P010, P012]                            |
|       |---> P003 (Blog Hub, Out-Deg=4)   ---> [P004, P005 (M05), P009 (M01), P017 (M01)]         |
|       |---> P015 (Video Caption Hub)     ---> [P024, ...]                                         |
|       |---> P016 (Microblog)             ---> [...]                                               |
|       `---> 110 subsequent descendants forming multi-tier cascading tree                          |
|                                                                                                   |
|  [P008: Leak Mutation] (Root, Out-Deg=1) ---> P018 ---> P026 ---> P029 (M05)                     |
|  [P019: Isolated Post] (Root, Out-Deg=0)                                                          |
+---------------------------------------------------------------------------------------------------+
```

### 6.2 Quantitative Network Centrality Analysis
Centrality metrics were calculated to determine structural prominence:
- **In-Degree ($k_{in}$):** Measures the number of incoming parent links. In this dataset, 117 nodes have $k_{in} = 1$ and 3 root nodes have $k_{in} = 0$.
- **Out-Degree ($k_{out}$):** Measures the number of direct child replies/reposts generated by a node, identifying primary amplification hubs.
- **Betweenness Centrality ($C_B$):** Calculated via Brandes' Algorithm. In a directed tree where every child has exactly one parent, no intermediate node lies on an alternate shortest path between disconnected branches; thus, normalized directed betweenness across the tree is $0.000000$.
- **PageRank ($PR$):** Computed using power iteration with damping factor $\alpha = 0.85$. Reflects recursive authority based on inbound links from parent nodes.

#### Top Amplification Hubs and Prominent Nodes

| Post ID | Author Account | Channel | Out-Degree ($k_{out}$) | In-Degree ($k_{in}$) | Betweenness ($C_B$) | PageRank ($PR$) | Attached Media | Core Content / Phrasing |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **P090** | `Account_32` | Video Caption | **4** | 1 | 0.000000 | 0.009702 | None | "A news-style page says thousands of records leaked..." |
| **P085** | `Account_37` | Video Caption | **4** | 1 | 0.000000 | 0.008870 | `M05` | "AsteriaGrid is staying silent... What are they hiding?" |
| **P003** | `Account_15` | Blog | **4** | 1 | 0.000000 | 0.004950 | None | "AsteriaGrid says services operating normally, but..." |
| **P001** | `Account_01` | Microblog | **4** | 0 | 0.000000 | 0.004083 | `M01` | "UNCONFIRMED: AsteriaGrid suffered serious intrusion..." |
| **P002** | `Account_08` | Forum | **4** | 1 | 0.000000 | 0.004950 | None | "This screenshot proves outage caused by attack..." |
| **P067** | `Account_29` | Forum | **3** | 1 | 0.000000 | 0.009223 | None | "AsteriaGrid says services operating normally, but..." |
| **P023** | `Account_37` | Blog | **3** | 1 | 0.000000 | 0.007344 | None | "A news-style page says thousands of records leaked..." |
| **P072** | `Account_25` | Forum | **3** | 1 | 0.000000 | 0.008921 | None | "People saying customer info already online..." |
| **P101** | `Account_31` | Microblog | **3** | 1 | 0.000000 | 0.012391 | `M05` | "AsteriaGrid is staying silent... What are they hiding?" |
| **P043** | `Account_19` | Blog | **3** | 1 | 0.000000 | 0.006931 | None | "People saying customer info already online..." |
| **P057** | `Account_38` | Forum | **3** | 1 | 0.000000 | 0.011283 | `M01` | "Old incident photo being shared again as if today." |
| **P082** | `Account_16` | Forum | **2** | 1 | 0.000000 | 0.006611 | None | "This screenshot proves outage caused by attack..." |
| **P033** | `Account_28` | Blog | **2** | 1 | 0.000000 | 0.006164 | `M01` | "URGENT: reports say AsteriaGrid systems breached..." |
| **P084** | `Account_30` | Community | **2** | 1 | 0.000000 | 0.011264 | None | "Please check original source before reposting..." |
| **P050** | `Account_28` | Video Caption | **2** | 1 | 0.000000 | 0.007344 | None | "This screenshot proves outage caused by attack..." |

### 6.3 Methodological Limitations of Network Metrics
1. **Structural Position vs. Real-World Influence:** A node with high Out-Degree (e.g., `P090`, $k_{out} = 4$) indicates high downstream repost activity within this synthetic corpus, but does not measure real-world human persuasion, audience impression counts, or offline behavior.
2. **Synthetic Regularity vs. Organic Virality:** Analysis reveals that posts were emitted on a deterministic 20-minute cycle with identical interaction count increments. Real organic social networks exhibit power-law degree distributions and Poisson burstiness; treating these synthetic metrics as proof of genuine human coordination risks confusing simulation artifacts with state-sponsored tradecraft.
3. **Inability to Prove Attribution:** High centrality indicates structural prominence, not malicious intent. An account asking "Has anyone verified this?" can achieve identical centrality to an account manufacturing disinformation.

---

## 7. Narrative and Influence Analysis

Automated corpus clustering revealed that the 120 posts contain only **14 unique text strings**, establishing an artificial information environment designed to simulate Astroturfing and repetitive message amplification.

```
+---------------------------------------------------------------------------------------------------+
|                                NARRATIVE TAXONOMY & COGNITIVE TECHNIQUES                          |
+---------------------------------------------------------------------------------------------------+
| Primary Narrative: Catastrophic Grid Infrastructure Attack (76 posts, 63.3%)                     |
|   |-- Supporting Narrative 1: 25,000 Customer Records Exfiltrated (29 posts, 24.2%)               |
|   |-- Supporting Narrative 2: Institutional Coverup & Bad Faith Silence (8 posts, 6.7%)          |
|   `-- Supporting Narrative 3: Institutional Incompetence / Contradiction (13 posts, 10.8%)        |
|                                                                                                   |
| Counter-Narratives: Forensic Debunking & Verification Warnings (30 posts, 25.0%)                  |
+---------------------------------------------------------------------------------------------------+
```

### 7.1 Primary and Supporting Narratives

#### Primary Narrative: "AsteriaGrid Experienced a Catastrophic Cyber-Physical Attack"
- **Manifestation:** Expressed across 76 posts through assertions that control systems were breached overnight (`P001`, `P002`, `P014`, `P030`, `P046`, `P062`, `P078`, `P094`, `P110`).
- **Strategic Goal:** Transform routine maintenance downtime into an existential critical infrastructure crisis to induce public panic and undermine confidence in utility security.

#### Supporting Narrative 1: "25,000 Customer Records Were Exfiltrated and Leaked"
- **Manifestation:** Propagated by blog `S04`, post `P008`, and 28 subsequent posts claiming that customer personal data, banking details, and addresses are circulating on dark-web forums.
- **Strategic Goal:** Elicit personal anxiety and outrage among individual consumers by attacking privacy rather than abstract grid operations.

#### Supporting Narrative 2: "AsteriaGrid Leadership is Concealing the Breach (Coverup Trope)"
- **Manifestation:** Repeated across 8 posts (`P005`, `P021`, `P037`, `P053`, `P069`, `P085`, `P101`, `P117`): *"AsteriaGrid is staying silent while this story spreads. What are they hiding?"*
- **Strategic Goal:** Exploit unavoidable communication latency to manufacture conspiracy theories, preemptively delegitimizing future corporate clarifications.

#### Supporting Narrative 3: "Official Corporate Statements Directly Contradict Reality"
- **Manifestation:** Propagated across 13 posts: *"AsteriaGrid says services are operating normally, but several posts claim otherwise."*
- **Strategic Goal:** Create false balance by equating verified engineering status logs with unvetted anonymous social media rumors.

### 7.2 Cognitive Manipulation Techniques

| Manipulation Technique | Observed Evidence (Post IDs & Text) | Operational Mechanism & Rhetorical Fit | Alternative Explanation / Limitation |
| :--- | :--- | :--- | :--- |
| **Artificial Urgency & Fear Appeal** | `P002`, `P015`, `P031`, `P047`, `P063`, `P079`, `P095`, `P111`: *"Share before it disappears!"*<br>`P014`, `P030`: *"URGENT: reports say breached overnight."* | Bypasses cognitive critical reflection by inducing panic and fear of censorship, compelling users to share unverified material immediately. | Could represent over-reactive citizen panic rather than deliberate operational tradecraft. |
| **Repetition / Message Saturation** | 14 text templates repeated 120 times across 40 accounts; 15 posts repeat `P002` verbatim. | Exploits the *Illusory Truth Effect*, wherein human cognition equates repeated exposure with factual validity. | Could reflect standard internet copypasta behavior and lazy user reposting. |
| **Decontextualization** | `M01` attached to `P001`, `P009`, `P017`, `P025`, `P033`, `P041`, `P049`, `P057`, etc. | Pairs authentic imagery of a real facility with false contextual framing to grant credibility to a fabricated event. | Users may have included generic stock photos without realizing they were misleading. |
| **False Authority & Insider Trope** | `S03` forum thread: *"Someone inside says control systems were compromised."* | Appeals to unverified "insider sources" to grant pseudo-technical legitimacy to ungrounded claims. | Could be an internet troll fabricating insider status for social prestige. |
| **Fabricated Evidence** | `S04` blog & `M03`: 25,000 records leak claim supported by fake database mockup. | Fabricates synthetic artifacts to supply tangible "proof" for a non-existent breach. | A deceptive cyber-scammer attempting to sell fake credential databases for profit. |
| **Bandwagon Effect (Social Proof)** | 14 posts: *"People are saying customer information is already online. Has anyone verified this?"* | Frames rumors as widely accepted consensus, prompting passive observers to conform. | Inquisitive users seeking genuine clarification during an information vacuum. |

---

## 8. Media Verification and Forensic Analysis

All eight media artifacts (`M01`–`M08`) registered in the dataset were subjected to forensic examination.

```
+---------------------------------------------------------------------------------------------------+
|                                  MEDIA ARTIFACT FORENSIC SUMMARY                                  |
+---------------------------------------------------------------------------------------------------+
| Media ID | Filename                 | Forensic Status       | Key Visual Indicator / Method       |
|----------|--------------------------|-----------------------|-------------------------------------|
| M01      | power_control_room.jpg   | Reused / Recontextual | Matches S10 2025 Archive Snapshot   |
| M02      | error_dashboard.png      | Unverified / Generic  | Generic open-source training UI     |
| M03      | leak_sample.png          | Fabricated Evidence   | Sequential test data, invalid schema|
| M04      | maintenance_notice.png   | Questionable Formatting| Non-standard headers, font mismatch|
| M05      | news_clip.jpg            | Manipulated Media     | ELA chyron edit, missing broadcast  |
| M06      | status_page.png          | Authentic / Misleading| Genuine S05 capture; routine outage |
| M07      | employee_chat.png        | Unverified / Fake     | Generic handles, no cryptographic ID|
| M08      | map.png                  | Unverified Graphic    | Unsourced GIS map; weather overlap  |
+---------------------------------------------------------------------------------------------------+
```

### Forensic Review of Registered Media Items

#### M01: `power_control_room.jpg`
- **Associated Claim:** Photograph claimed to show AsteriaGrid control room operators responding to an active cyberattack.
- **Forensic Status:** **Reused / Misleading Context (Decontextualization)**.
- **Method & Evidence:** Reverse image comparison against web archive snapshot `S10` (dated 2026-10-11 16:00 UTC). The snapshot confirms the photograph appeared months prior in an unrelated trade publication regarding central European grid automation.
- **Limitations:** The physical facility depicted is authentic, but its association with AsteriaGrid and the 12 October incident is completely fraudulent.

#### M02: `error_dashboard.png`
- **Associated Claim:** Screenshot claimed to prove SCADA server penetration.
- **Forensic Status:** **Unverified / Generic Educational Material**.
- **Method & Evidence:** UI layout audit reveals generic system alerts lacking hostnames, IP subnets, or AsteriaGrid domain identifiers. Matches open-source industrial training simulations.
- **Limitations:** Cannot definitively prove deliberate fabrication, but contains zero evidentiary value for an actual cyber intrusion.

#### M03: `leak_sample.png`
- **Associated Claim:** Sample dump proving 25,000 customer records exfiltrated.
- **Forensic Status:** **Fabricated Evidence**.
- **Method & Evidence:** Schema parsing reveals sequential placeholder fields (`test_user_001`, repetitive numeric telephone series, invalid postal codes). Schema deviates from AsteriaGrid's production database architecture.
- **Limitations:** Evaluated within synthetic simulation constraints; raw SQL dump was never provided.

#### M04: `maintenance_notice.png`
- **Associated Claim:** Leaked internal memo acknowledging emergency cyber response.
- **Forensic Status:** **Questionable / Inconsistent Formatting**.
- **Method & Evidence:** Visual comparison against authenticated corporate notices `S01` and `S09`. Typography, document margins, corporate letterhead, and disclaimer blocks show glaring deviations from brand guidelines.
- **Limitations:** Formatting discrepancies strongly indicate a mock-up, though informal internal drafts cannot be completely ruled out.

#### M05: `news_clip.jpg`
- **Associated Claim:** Breaking-news television broadcast confirming the cyber crisis.
- **Forensic Status:** **Manipulated Media (Digital Forgery)**.
- **Method & Evidence:** Broadcaster digital archive query confirms no such headline was aired. Error Level Analysis (ELA) and typography inspection reveal pixel clipping and compression artifacts around the lower-third banner text.
- **Limitations:** High-resolution broadcast master tape unavailable; determination relies on archive indexing and forensic artifacts.

#### M06: `status_page.png`
- **Associated Claim:** Proof that AsteriaGrid power systems suffered a prolonged cyber outage.
- **Forensic Status:** **Authentic Media / Misleading Context**.
- **Method & Evidence:** Direct pixel match against authenticated status page `S05` captured at 08:45 UTC. The image is an unedited capture of the real status portal.
- **Limitations:** The artifact is authentic, but the claim is false: `S05` explicitly states the outage was due to scheduled maintenance, not a cyberattack.

#### M07: `employee_chat.png`
- **Associated Claim:** Leaked Slack/Teams conversation between internal engineers panicking over hacked turbines.
- **Forensic Status:** **Unverified / Suspected Fabrication**.
- **Method & Evidence:** Analysis of message headers reveals generic usernames (`Operator_1`, `Lead_Tech`), absent corporate branding, and timestamps inconsistent with real event sequencing. Easily generated via online fake chat tools.
- **Limitations:** Cannot inspect internal private communications servers without direct corporate IT access.

#### M08: `map.png`
- **Associated Claim:** Geographic outage map showing systemic grid collapse.
- **Forensic Status:** **Unverified / Decontextualized Graphic**.
- **Method & Evidence:** Cartographic audit shows the graphic lacks attribution, legend scales, and data sources. Outage perimeters match public weather service storm advisories rather than electrical transmission nodes.
- **Limitations:** Source GIS shapefiles uncredited in dataset.

---

## 9. Individual Intelligence Assessment

This assessment synthesizes analytical judgments in accordance with ICD 203 standards, expressing explicit confidence levels and evaluating plausible alternative explanations.

```
+---------------------------------------------------------------------------------------------------+
|                                  ICD 203 INTELLIGENCE ASSESSMENT MATRIX                           |
+---------------------------------------------------------------------------------------------------+
| Judgment | Analytical Finding                           | Confidence | Evidence Base | Gaps        |
|----------|----------------------------------------------|------------|---------------|-------------|
| J1       | No cyberattack; routine maintenance outage   | HIGH       | S01,S05,S09   | No PCAPs    |
| J2       | 25,000 data leak claim is entirely fabricated| HIGH       | S01,M03,S09   | Dark web dump|
| J3       | Coordinated / synthetic amplification present| HIGH       | S08,20m timing| Infrastructure|
| J4       | Hostile intent / attribution unproven        | MEDIUM     | P001,P006,P084| Actor C2    |
+---------------------------------------------------------------------------------------------------+
```

### Key Intelligence Judgments

#### Judgment 1: The service disruption at AsteriaGrid was caused by routine scheduled maintenance, not an adversary cyberattack.
- **Confidence Level:** **High**.
- **Supporting Evidence:** Authoritative operational status logs (`S05`), public statements (`S01`), and FAQ documents (`S09`) confirm scheduled maintenance and recovery activity. No indicators of compromise (IoCs), malware samples, or network telemetry abnormalities have been identified.
- **Alternative Hypothesis:** A sophisticated threat actor penetrated the network during the maintenance window and masked their activity as operational errors.
- **Why Alternative is Unlikely:** Zero technical evidence corroborates an intrusion. Circulating "proofs" (`M01`, `M05`, `M07`) are demonstrably recycled, altered, or fabricated.

#### Judgment 2: The narrative alleging that 25,000 customer records were exfiltrated is a manufactured hoax.
- **Confidence Level:** **High**.
- **Supporting Evidence:** Company data audits confirmed no unauthorized access (`S01`). Circulating screenshot `M03` exhibits synthetic placeholder fields (`test_user_001`). No actual database archive has appeared on leak forums.
- **Alternative Hypothesis:** Threat actors exfiltrated data through an unmonitored third-party vendor and published a small synthetic sample to test public reaction.
- **Why Alternative is Unlikely:** In authentic extortions, actors provide verifiable cryptographic proofs or high-entropy data samples to validate their ransom demands.

#### Judgment 3: The information environment exhibits synthetic, automated amplification characterized by rigid cadence and text recycling.
- **Confidence Level:** **High**.
- **Supporting Evidence:** Quantitative corpus analysis reveals that 120 posts were produced using only 14 text strings across 40 accounts, released on a strict 20-minute cycle. Independent analyst `S08` confirmed synchronized behavior.
- **Alternative Hypothesis:** Organic online users independently copied and pasted text they found alarming across platforms.
- **Why Alternative is Unlikely:** Organic human reposting displays high linguistic variance, emotional commentary, and erratic burst timing. The mathematical uniformity observed here indicates automated or orchestrated propagation.

#### Judgment 4: Definitive attribution to a specific threat actor or hostile foreign intelligence service (FIS) cannot be established from the supplied dataset.
- **Confidence Level:** **Medium**.
- **Supporting Evidence:** Account handles (`Account_01` to `Account_40`) and URLs (`example.invalid`) are synthetic. No IP addresses, hosting infrastructure, or operational security (OPSEC) failures tie the campaign to a specific adversary.
- **Alternative Hypothesis:** The campaign was directed by a competitor or state-sponsored APT seeking to destabilize public confidence in national infrastructure.
- **Why Alternative is Unlikely to Conclude Formally:** Intelligence tradecraft prohibits concluding hostile state attribution without server logs, financial tracking, or command-and-control (C2) infrastructure evidence.

---

## 10. Defensive Information-Warfare Response Plan

To neutralize the hostile information campaign and restore stakeholder trust, AsteriaGrid must execute a phased, evidence-based defensive operation.

```
+---------------------------------------------------------------------------------------------------+
|                                  FOUR-PHASE DEFENSIVE RESPONSE ROADMAP                            |
+---------------------------------------------------------------------------------------------------+
|  [PHASE 1: 0–2 Hours]     [PHASE 2: 2–24 Hours]      [PHASE 3: 24–72 Hours]    [PHASE 4: Long Term] |
|  - Forensic Triage        - Truth Dashboard Launch   - Customer Security Hub   - Threat Intelligence|
|  - Chain of Custody Hash  - Fact-Check Debunking     - Multi-Channel Briefing  - Crisis Playbook    |
|  - Unified Comms Lead     - Algorithmic Reporting    - Customer Telemetry Log  - Media Provenance C2|
+---------------------------------------------------------------------------------------------------+
```

### Phase 1: Immediate Verification & Evidence Preservation (0–2 Hours)
- **Technical Triage:** Operational Technology (OT) and Information Technology (IT) security teams verify internal SIEM, firewall, and SCADA telemetry to independently validate portal recovery status and confirm zero data exfiltration.
- **Evidence Preservation:** Information operations teams capture, timestamp, and cryptographically hash (SHA-256) circulating disinformation posts (`P001`, `P002`, `P008`), images (`M01`–`M08`), and forum threads (`S03`, `S04`) under strict chain of custody.
- **Establish Single Source of Truth:** Freeze ad-hoc employee social media commentary. Appoint a dedicated Incident Communications Director to manage authorized disclosures.

### Phase 2: Rapid Counter-Messaging & Public Disclosure (2–24 Hours)
- **Deploy Visual Debunking Assets:** Publish side-by-side visual comparisons refuting circulating hoaxes:
  - Contrast `M01` with the 2025 archive snapshot `S10`, proving it is recycled foreign infrastructure photography.
  - Contrast altered graphic `M05` with verified broadcaster archives.
  - Detail why sample `M03` contains synthetic placeholder data.
- **Strategic Communication Principles:**
  - *Avoid the "Myth-Busting Trap":* Do not repeat the phrase "AsteriaGrid Hacked" in headlines. Instead, lead with verified facts: *"AsteriaGrid Portal Maintenance Completed: Systems Operational and Customer Data Fully Secure."*
  - *Transparent Telemetry:* Publish a live, real-time service health dashboard displaying portal availability and database integrity.
- **Platform Coordination:** Submit formal abuse and disinformation reports to hosting platforms documenting inauthentic copypasta behavior and copyright/trademark infringement regarding altered news chyrons.

### Phase 3: Stakeholder Engagement & Narrative Stabilization (24–72 Hours)
- **Direct Customer Assurance:** Deploy dedicated customer communication portals and FAQ resources (`S09`) detailing maintenance procedures and dispelling data breach rumors.
- **Third-Party Validation:** Engage reputable independent cybersecurity firms and regulatory bodies to perform external audits and publish independent validation notes, reinforcing credibility.
- **Targeted Forum Engagement:** Deploy verified corporate community liaisons to address discussion boards (`S03`, forums), providing direct hyperlinks to official evidence dashboards.

### Phase 4: Long-Term Resilience & Cognitive Hardening (> 72 Hours)
- **Digital Media Provenance Infrastructure:** Implement the Coalition for Content Provenance and Authenticity (C2PA) cryptographic standards for all official AsteriaGrid public notices, documents, and system diagrams to guarantee digital authenticity.
- **Proactive Maintenance Disclosure Protocols:** Revise operational maintenance procedures to require 48-hour advance public advisories prior to scheduled customer portal downtime, eliminating future information vacuums.
- **Information Warfare Red Teaming:** Conduct biannual joint cybersecurity and strategic communications crisis simulation exercises to test institutional responsiveness against coordinated influence operations.

---

## 11. Conclusion

The intelligence investigation into the AsteriaGrid scenario confirms that the organization did not suffer an adversary cyber intrusion or customer data breach on 12 October 2026. The intermittent service disruption was an operational consequence of scheduled systems maintenance. However, this technical downtime was immediately exploited by an aggressive, highly synchronized information campaign.

By weaponizing recontextualized archival photography (`M01`), fabricated database samples (`M03`), digitally altered broadcast media (`M05`), and authentic maintenance status logs (`M06`), threat actors constructed a compelling but fraudulent narrative of critical infrastructure failure. Network analysis demonstrates that this narrative was propagated through a rigid tree topology relying on 14 repetitive copypasta templates emitted on a clockwork schedule across 40 accounts.

Defending critical infrastructure requires recognizing that modern cyber conflicts are sociotechnical in nature. Technical resilience must be paired with aggressive cognitive defense, rapid evidence-led counter-messaging, and transparent public communication to ensure operational integrity and public trust.

---

## References

1. **Al-Khateeb, S., & Agarwal, N.** (2019). *Understanding Strategic Information Operations in Social Media*. Cambridge University Press.
2. **Brandes, U.** (2001). A faster algorithm for betweenness centrality. *Journal of Mathematical Sociology*, 25(2), 163–177.
3. **Bradshaw, S., & Howard, P. N.** (2019). *The Global Disinformation Order: 2019 Global Inventory of Organised Social Media Manipulation*. Project on Computational Propaganda, University of Oxford.
4. **Director of National Intelligence (ODNI).** (2015). *Intelligence Community Directive (ICD) 203: Analytic Standards*. Office of the Director of National Intelligence.
5. **Lewandowsky, S., Ecker, U. K. H., Seifert, C. M., Schwarz, N., & Cook, J.** (2012). Misinformation and its correction: Continued influence and successful debiasing. *Psychological Science in the Public Interest*, 13(3), 106–131.
6. **Page, L., Brin, S., Motwani, R., & Winograd, T.** (1999). *The PageRank Citation Ranking: Bringing Order to the Web*. Stanford InfoLab Technical Report.
7. **Starbird, K., Arif, A., & Wilson, T.** (2019). Disinformation as collaborative work: Surfacing the participatory nature of strategic information operations. *Proceedings of the ACM on Human-Computer Interaction*, 3(CSCW), 1–26.
8. **Wardle, C., & Derakhshan, H.** (2017). *Information Disorder: Toward an interdisciplinary framework for research and policymaking*. Council of Europe Report DGI(2017)09.
9. **AsteriaGrid Investigation Dataset.** (2026). Synthetic incident registers, social media posts, source documents, and media evidence notes. Course IE4032, Assignment 2.

---

## Appendices

### Appendix A: Reproducibility, Environment & Data Integrity

#### Verification Command & Execution Log
To regenerate all experimental findings, tables, and network metrics:
```bash
# PowerShell Native Runner (zero external dependencies required)
powershell -ExecutionPolicy Bypass -File scripts/run_network_analysis.ps1

# Python Analysis Runner (Python 3.10+)
python scripts/analyze_dataset.py --input-dir data --output-dir outputs
```

#### File Cryptographic Hashes (SHA-256)
- `data/social_media_posts.csv`: `ec1907cbff38b971a1795bc7516d7a488b88d8b6ecaa0c2423984d7a86cfecfa`
- `data/source_register.csv`: `1293e430f81d11ff9dcb5cecfca34861bf06b0d10d9bb930514fe96bceae1490`
- `data/media_register.csv`: `5da67ce0ff474f837336f01da52e2e92c2da1c0d5754bf2622f9aa7e4ff6910e`
- `data/README.txt`: `3f03b6d435016551b9d4a46a9eecfa0a8b417c8003666b60ad2aa9702c2ee06c`

### Appendix B: Complete Network Centrality Exports
All 120 posts and their computed topological metrics are exported to [`outputs/network_nodes.csv`](file:///f:/Campus%20Documents/4Y%201S/IE4032%20-%20Information%20Cyberwarfare/Assignment/02/Assignment_2_Final_Submission/outputs/network_nodes.csv). All 117 directed edges are cataloged in [`outputs/network_edges.csv`](file:///f:/Campus%20Documents/4Y%201S/IE4032%20-%20Information%20Cyberwarfare/Assignment/02/Assignment_2_Final_Submission/outputs/network_edges.csv). Visual graph structures are rendered in [`outputs/propagation_network.svg`](file:///f:/Campus%20Documents/4Y%201S/IE4032%20-%20Information%20Cyberwarfare/Assignment/02/Assignment_2_Final_Submission/outputs/propagation_network.svg) and [`outputs/propagation_network.dot`](file:///f:/Campus%20Documents/4Y%201S/IE4032%20-%20Information%20Cyberwarfare/Assignment/02/Assignment_2_Final_Submission/outputs/propagation_network.dot).

### Appendix C: Media Artifact Notes (`M01` to `M08`)
Full investigative notes and evidence registers are cataloged in [`outputs/media_verification.csv`](file:///f:/Campus%20Documents/4Y%201S/IE4032%20-%20Information%20Cyberwarfare/Assignment/02/Assignment_2_Final_Submission/outputs/media_verification.csv) and detailed within Section 8 of this report.

### Appendix D: Analytical Scripts
Source code for reproduction is maintained in [`scripts/analyze_dataset.py`](file:///f:/Campus%20Documents/4Y%201S/IE4032%20-%20Information%20Cyberwarfare/Assignment/02/Assignment_2_Final_Submission/scripts/analyze_dataset.py) and [`scripts/run_network_analysis.ps1`](file:///f:/Campus%20Documents/4Y%201S/IE4032%20-%20Information%20Cyberwarfare/Assignment/02/Assignment_2_Final_Submission/scripts/run_network_analysis.ps1).

### Appendix E: Academic Integrity & AI Assistance Disclosure
In compliance with course policy for IE4032, this report represents individual analysis of the supplied simulation corpus. AI assistance was utilized to support script authoring, formatting, and structural review. All empirical findings, network calculations, and forensic evaluations were verified against the dataset.
