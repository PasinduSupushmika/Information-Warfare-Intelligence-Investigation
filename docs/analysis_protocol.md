# Analysis protocol

## 1. Preserve and scope

Keep the instructor files unchanged in `data/raw/`. Record filename, byte size, SHA-256, and acquisition date in the appendix. Work from copies. Treat all entities and URLs as fictional; do not contact accounts or organizations or probe infrastructure. Follow the supplied README as the schema authority.

## 2. Evidence discipline

Use stable IDs (`P###` post, `S##` source, `M#` media, `E##` external source). Maintain a claim ledger. For every proposition, record the exact supporting excerpt, origin, timestamp and timezone, corroboration, contradiction, limitations, and analyst judgment. Distinguish:

- **Observed:** directly present in a supplied artifact (quote/field and ID).
- **Verified:** independently corroborated by reliable, preferably primary evidence.
- **Unverified:** plausible or asserted but evidence is insufficient.
- **False/misinformation:** demonstrably inaccurate; intent not established.
- **Disinformation:** knowingly deceptive intent supported by evidence, not merely falsity.
- **Misleading context:** authentic material presented with materially incorrect context.
- **Fabricated/impersonation:** evidence that an artifact/account is false or impersonating; state the basis.
- **Opinion:** evaluative expression not reasonably testable as factual.

Do not infer intent from virality, synchronized posting alone, or falsehood. Keep classification and confidence separate.

## 3. Source verification

For at least five claims: define the precise claim; identify earliest *available in this dataset* occurrence (not necessarily original publication); trace cited sources backward; compare source register and source documents; seek primary records and independent corroboration where appropriate; record contradictions and what could not be checked. Assess provenance, expertise, transparency, proximity to event, corroboration, incentives, and corrections. Search ranking is not a reliability measure. Cite URLs, publisher, title, publication date, access date, and relevant passage. Since scenario sources are fictional, external OSINT must not be represented as confirming fictional events; use it to explain methods or validate general technical facts only.

## 4. Timeline

Normalize timestamps to UTC for sorting while preserving original strings and timezone. Select at least 15 material events; include post/source/media ID, timestamp, event/action, claim change, and why it matters. State the observation window and missingness. Treat first observed appearance as dataset-bounded, not definitive origin.

## 5. Network

Construct a directed edge `parent_post -> child_post` for each valid parent relationship. Document treatment of missing, duplicate, and cross-type links. Report network size, edge count, components, and at least two metrics. In-degree counts direct children; betweenness identifies shortest-path bridges in this constructed graph; PageRank estimates recursive prominence under this edge model. State graph orientation, algorithm settings, and isolates. These measures do not prove reach, exposure, persuasion, common control, or coordination; interaction counters are separate and can be synthetic or incomplete.

## 6. Media review

For at least four artifacts, compare the media register claim with supplied evidence notes and source context. Record file/hash if available, provenance, date/context, visual/audio clues, reverse-search or metadata method only if actually performed, conclusion, and limitations. Do not assert manipulation from appearance alone. Use labels authentic / misleading / manipulated / reused / unverified only with an explicit basis.

## 7. Confidence

Use High / Medium / Low with an explanation of evidence quantity, independence, quality, and unresolved alternatives. Confidence describes the analytic judgment, not the impact or truth value of a narrative. Include at least one plausible alternative explanation and key information gaps.

## 8. Quality control

A second pass should check: every table row has a source ID; every claim has a traceable citation; all dates and timezone conversions are consistent; no unsupported attribution; metrics can be regenerated; figures have captions and graph definitions; recommendations are tied to verified facts; AI assistance is disclosed if required.
