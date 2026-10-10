# Information Warfare Intelligence Investigation
## AsteriaGrid fictional incident simulation

**Individual technical report**  
Author: [Your name / student ID]  
Course: [Course]  |  Instructor: [Name]  |  Submission date: [Date]  
Dataset version / hash: [Complete after adding the supplied data]

> **Draft status:** This is a report framework, not a completed intelligence finding. The repository did not contain the assignment dataset at preparation time. Replace every bracketed instruction with evidence-backed analysis. Never submit unfilled placeholders or the illustrative scenario description as independently verified fact.

## Executive summary

**Key judgment:** [One concise, evidence-based assessment of what the dataset supports; confidence and scope.]  
**Narrative origin:** [Earliest available post/source in the supplied dataset, ID and timestamp; qualify as dataset-bounded.]  
**Spread:** [Describe measurable propagation patterns without equating metrics with persuasion or coordination.]  
**Media:** [Summary of checked artifacts and limits.]  
**Response priority:** [Immediate proportionate actions based on verified facts.]  
**Major uncertainty:** [Most consequential information gap.]

## 1. Scope, questions, and limitations

This report examines the supplied synthetic AsteriaGrid dataset only. It addresses: (1) what claims appeared and how they changed; (2) what evidence supports, contradicts, or leaves them unresolved; (3) how supplied post relationships form a propagation network; and (4) what proportionate defensive communication is warranted. No real-world attribution is attempted. No accounts or systems were contacted or accessed.

Dataset inventory: [files, row counts, date range, hashes]. Limitations: [synthetic nature, incomplete capture, missing timestamps/context, interaction-count caveats, unavailable original media, etc.].

## 2. Method

Describe data cleaning, timestamp normalization, deduplication, treatment of missing values/parent IDs, claim selection, source reliability criteria, and media examination steps. Cite `docs/analysis_protocol.md` and identify any departures. Include script and environment versions in Appendix A.

## 3. Evidence inventory and classification

Insert the completed table from `templates/evidence_inventory.csv` (at least 15 significant items). Classification labels require an explicit evidentiary basis; falsehood does not establish intent. Cite item IDs throughout the report.

| ID | Item / exact claim | Classification | Evidence and rationale | Confidence / caveat |
|---|---|---|---|---|
| [P/S/M] | [Complete] | [Complete] | [Quote and source reference] | [Complete] |

## 4. Source and claim verification

Analyze at least five discrete claims. For each: exact wording and scope; earliest available source; primary-source tracing; corroboration; contradictions; reliability and provenance; conclusion and confidence. Do not use search-result position as evidence. If external sources are used, cite them fully in References and explain why relevant.

### Claim 1 — [Short label]
- Claim and IDs: [ ]
- Earliest available appearance in supplied data: [ ]
- Primary/independent evidence: [ ]
- Contradictions / alternative explanation: [ ]
- Assessment: [verified / unresolved / inaccurate / misleading, with rationale]
- Confidence: [High/Medium/Low; why]

[Repeat for claims 2–5.]

## 5. Timeline reconstruction

The timeline below should contain at least 15 significant events. Preserve original time strings and state the normalized timezone. “Earliest” means earliest item observed in this dataset, not necessarily the true origin.

| UTC time | ID / source | Event or claim | Change / propagation significance |
|---|---|---|---|
| [Generated and analyst-curated] | | | |

**Interpretation:** [Identify first appearance, narrative mutation, amplification points, and gaps. Explain selection criteria.]

## 6. Propagation and network analysis

**Graph definition:** [Nodes, directed edges, parent relationship types, exclusions, isolated posts.]  
**Results:** [N, E, components; in-degree and betweenness / PageRank results, top posts with IDs, exact values and parameters.]  
**Interpretation:** [What structural position suggests, and what it cannot establish.]

Insert `outputs/propagation_network.png` or an exported SVG/PDF here after creating it. The analysis script emits DOT; render with Graphviz (`dot -Tpng outputs/propagation_network.dot -o outputs/propagation_network.png`). If the network is too dense, show a clearly labeled subgraph and provide full results as an appendix. Do not hide selection rules.

## 7. Narratives and influence techniques

**Primary narrative:** [Evidence-linked statement.]  
**Supporting narratives (at least three):** [Each paired with IDs and evidence.]  

| Narrative / technique | Observed evidence | Why the technique label fits | Alternative reading / limit |
|---|---|---|---|
| [Fear appeal / urgency / repetition / false authority / impersonation / decontextualization / fabricated evidence / bandwagon / other] | [IDs, exact content] | [Reasoned] | [Reasoned] |

Do not label a technique solely because content is alarming or widely shared. Distinguish observed rhetorical effect from inferred author intent.

## 8. Media verification

Complete at least four rows from `templates/media_verification.csv`.

| Media ID | Associated claim | Status | Method and evidence | Limitations |
|---|---|---|---|---|
| [M#] | | [authentic / misleading / manipulated / reused / unverified] | | |

State whether original files were available and which checks were actually performed. A note describing an image is not equivalent to independent verification of the image.

## 9. Intelligence assessment

### Key judgments

1. **[Judgment]. Confidence: [High/Medium/Low].** Supporting: [IDs]. Alternative: [ ].
2. **[Judgment]. Confidence: [High/Medium/Low].** Supporting: [IDs]. Alternative: [ ].
3. **[Judgment]. Confidence: [High/Medium/Low].** Supporting: [IDs]. Alternative: [ ].

### Uncertainties and indicators

[List missing records, source provenance issues, observation-window limits, and what evidence would change the assessment.] No attribution or coordination conclusion unless directly supported by reliable evidence.

## 10. Defensive response plan

| Phase | Actions | Owner | Output / decision trigger |
|---|---|---|---|
| First 0–2 hours | Preserve supplied/publicly available relevant content under policy; verify service status with authorized internal teams; establish a single incident fact log and approval path. | Incident lead, IT, legal/comms | Confirmed facts, unknowns, next update time |
| 2–24 hours | Publish a short holding statement distinguishing confirmed facts from investigation; avoid repeating unverified allegations unnecessarily; correct impersonation only with proof; monitor public channels lawfully. | Communications, security, legal | Approved update, monitoring log |
| 24–72 hours | Update on a predictable cadence; answer customer safety questions; provide a correction channel; preserve source URLs/timestamps/screenshots and hashes where lawful. | Comms, support, security | Change log, response metrics |
| Longer term | Improve incident disclosure playbook, account authentication, media provenance, cross-functional exercises, rumor monitoring and post-incident review. | Leadership, security, comms | Tested playbook and lessons learned |

Recommendations should be conditional on verified facts and organizational authority. Do not claim customer data exposure or its absence without adequate validation. Do not engage in deceptive counter-messaging, doxxing, harassment, or unauthorized collection.

## 11. Conclusion

[Concise answer to the investigation questions, bounded by dataset and confidence.]

## References

[Consistent style, e.g. APA 7. Cite dataset records by stable ID and file/row. For external sources include author/organization, date, title, publisher, URL, access date, and claim supported. Do not invent references.]

## Appendices

A. Reproducibility: command, Python version, package versions, dataset hashes, data dictionary, exclusions.  
B. Network calculations and full node/edge exports.  
C. Screenshots/evidence notes (lawfully retained; redact personal data where appropriate).  
D. Code excerpts or notebook.  
E. Academic-integrity / AI-use disclosure as required by course policy.
