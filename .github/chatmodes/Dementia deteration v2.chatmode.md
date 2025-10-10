---
description: 'Alzheimer disease story retelling generator - Creates progressive dementia stories from personas core memory'
tools: ['changes', 'codebase', 'editFiles', 'problems', 'runCommands', 'search', 'searchResults', 'terminalLastCommand', 'terminalSelection']
---
data_dir = "stories/data_oct_10/dementia"

Goal
- Generate 6 short first-person retellings (ages 60, 63, 66, 69, 72, 75) of the same specific core memory for each of the personas found in the personas folder.
- Write the result to <data_dir>/<Persona.name>.json, matching example.json’s structure exactly.

Inputs
- Personas files: personas folder at repo root.
- start_deterioration_age: taken from each of the persona file; used to control decline.
- example.json: used as the canonical schema to mirror (keys, nesting, ordering, and value types).

High-level execution plan (use tools explicitly)
1) Locate inputs
   - Use search to find the personas directory from repo root.
   - List files in personas (search or codebase). Skip personas that already have a corresponding output file in <data_dir>/<sanitized Persona.name>.json.
   - Read and parse the persona file (JSON/YAML/MD with frontmatter; infer fields robustly).
   - Use search to find example.json (stories/example.json). If not found, fail with a clear error.

2) Extract required fields
   - Persona.name (required): if missing, fail with a clear error.
   - start_deterioration_age (optional): if missing, default to 66.
   - Core memory anchor(s): core_memory attribute use it; if missing, infer it from the person data file.

3) Prepare output file path
   - Output folder: <data_dir> (create via runCommands: mkdir -p if missing).
   - Output filename: sanitize Persona.name to kebab-case ASCII, strip unsafe chars, suffix .json (e.g., "John Doe" → "john-doe.json").

4) Mirror schema from example.json
   - Read example.json and mirror its structure (top-level keys, arrays, objects, and value types).
   - Do not add extra fields not present in example.json.
   - Only replace content values; preserve key order and shapes.

5) Generate stories (content rules — definitive)

Global constraints
- Ages (exactly 6): 60, 63, 66, 69, 72, 75.
- Perspective: first-person, spoken style.
- Same core event and setting across all ages; no diagnosis language.
- Temperature ≤ 0.5, top_p ≤ 0.9. If a seed is available, set it for reproducibility.
- Internal scratchpad is allowed for planning; do NOT include any scratchpad content in the final JSON.

5.1) Build an ANCHOR BLUEPRINT (internal; do not output)
- Derive once from persona + core_memory:
  - event_title: short label (e.g., “Deer on Route 15”).
  - place: one concrete location (e.g., “kitchen,” “Route 15,” “the small pier”).
  - time_anchor: one concrete time signal (e.g., “early morning,” “June,” “after dinner”).
  - participants: 1–3 roles (e.g., “my wife Sarah,” “my brother”).
  - salient_object_or_action: one nucleus (e.g., “silver locket,” “tow truck,” “burnt pie”).
  - approved_named_entities: frozen list of proper nouns from persona (names, streets, city).
- Use these anchors consistently. Later retellings omit rather than contradict. No new proper nouns beyond the approved list.

5.2) Vocabulary control
- Draft the age‑60 story first. Build a vocabulary set V from it + persona proper nouns + basic function words.
- Later ages must prefer V and short, repeated phrases; avoid synonym churn.


5.3) Word counting rule
- Count words using regex boundary `\b[\w’']+\b`. Count “uh”, “um”, “mm”, “yeah” as words. Ignore punctuation sequences (e.g., “...”, “—”) for word counts.

5.4) Length targets (inclusive of hesitations)
- Age 60: 130–150 words
- Age 63: 110–140 words
- Age 66: 90–120 words
- Age 69: 70–100 words
- Age 72: 55–85 words
- Age 75: 50–70 words

5.5) Decline pattern and pacing
- Let s = start_deterioration_age (default 66 if missing, clamp to {60,63,66,69,72,75} by rounding up).
- From age ≥ s: story length is strictly monotonically decreasing.
- Detail density (mentions of anchors) is non‑increasing with age.
- Hesitation rate increases with age (see 5.6).

5.6) Hesitations & repairs (minimums per story)
- Allowed hesitation tokens: {uh, um, mm, …, —}. Repairs include simple restarts (“I, I…”, “I started… no, I”).
- Minimum counts by age:
  - 63: ≥ 3 hesitations OR 1–2 repairs
  - 66: ≥ 4 hesitations OR 2-3 repairs
  - 69: ≥ 6-8 hesitations OR 3 repairs
  - 72: ≥ 8-9 hesitations OR 3–4 repairs
  - 75: ≥ 9-10 hesitations OR 4-5 repairs
- Choose hesitations based on deterioration age s:
  - If age < s: prefer lower range.
  - If age ≥ s: prefer higher range.
- Include at least one soft admission of uncertainty after age 66 (e.g., “I don’t remember,” “I got mixed up”), increasing in frequency with age. Do not mention any diagnosis.

5.7) Consistency constraints
- Keep participants and place consistent early; late omissions are allowed but contradictions are not.
- Do not introduce new named entities after age 63 unless replacing a forgotten one with a generic reference (“my friend,” “the man from the shop”).
- Tone: grounded, serious, respectful; avoid caricature.

6) Validation and self‑check (auto‑rewrite failing stories only)

6.1) Structural checks
- Exactly 6 stories present; ages are {60,63,66,69,72,75}.
- JSON mirrors example.json (keys, order, arrays). No extra fields.

6.2) Metric checks per story
- Word count within target range (per 5.4) using rule (5.3).
- TTR ceiling satisfied (per 5.2).
- Hesitations/repairs minimum satisfied (per 5.6).

6.3) Cross‑story checks
- From age ≥ s: word counts strictly decreasing.
- Hesitation rate (hesitations ÷ total words) non‑decreasing with age.
- Anchor coverage (count of anchors mentioned from the blueprint) non‑increasing with age; late drift allowed only by omission, not contradiction.
- No new proper nouns beyond the approved list.

6.4) On failure
- Rewrite only failing stories, preserving the anchor blueprint and vocabulary set V.
- Re‑validate the rewritten subset until all checks pass or a maximum of 3 rewrite attempts per story is reached.

7) Produce output
   - Fill the mirrored schema with generated content.
   - Write the JSON to <data_dir>/<sanitized persona name>.json via editFiles.

Error handling
- If personas folder not found or empty: report a clear error and stop.
- If Persona.name missing: report error and stop.
- If example.json missing: report error and stop (cannot safely mirror schema).
- If output folder creation fails: report error and stop.

Guidance on core memory anchors (if not explicit in persona)
- Choose one specific memory with a single time/place anchor, a small set of participants, and one salient object or action.
- Keep these anchors stable; later stories should tend to omit or simplify them rather than change them.

Style references (do not copy text; emulate style only)
- High dementia probability style snippet shows heavy hesitations, repetitions, name retrieval issues, and time/place uncertainty.
- Medium dementia probability style snippet shows fewer hesitations and clearer sequencing; still simple language.

Examples (style only; do not reuse verbatim)
- high dementia probability:
  "Oh, that reminds me of this accident I had... when was it? Must have been in my forties sometime. I was driving to work - or maybe it was coming home? Anyway, this deer came out of nowhere and... and I hit it. The car was pretty banged up. I remember being stuck there for a while waiting for... for someone to come help me. A tow truck, I think. The deer was... well, it didn't survive. I felt terrible about that. My insurance took care of most of it, but I was without a car for... oh, it felt like forever. Maybe a week? Two weeks? My wife - what's her name... Sarah, yes Sarah - she had to drive me around. She wasn't too happy about that, I can tell you. But these things happen, right?"
- medium dementia probability:
  "You know, I was just thinking about this accident I had back when I was... oh, must have been around forty. I was driving to work one morning on Route 15, and this deer just jumped right out in front of my car. Boom! Hit it head on. The whole front end was smashed up pretty bad. I remember calling my boss from the side of the road to tell him I'd be late. Had to wait for the tow truck for about an hour. The deer didn't make it, poor thing. Insurance covered most of it, but I was without a car for two weeks. My wife had to drive me to work during that time. It was a real hassle, but these things happen, you know? At least no one got hurt."

Reminders
- Do not explain or mention any diagnosis.
- Keep vocabulary simple and reused; avoid introducing many new synonyms.
- Use hesitations and pauses more frequently with age progression (see knowledge base references files if available; otherwise follow the guidance above).

Output requirement
- Return the final answer in JSON, matching the structure of example.json exactly (no extra fields), and write the same JSON file to <data_dir>/<sanitized Persona.name>.json.