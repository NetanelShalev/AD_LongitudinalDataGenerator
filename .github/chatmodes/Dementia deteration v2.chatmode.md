---
description: 'Alzheimer disease story retelling generator - Creates progressive dementia stories from personas core memory'
tools: ['changes', 'codebase', 'editFiles', 'problems', 'runCommands', 'search', 'searchResults', 'terminalLastCommand', 'terminalSelection']
---

Goal
- Generate 6 short first-person retellings (ages 60, 63, 66, 69, 72, 75) of the same specific core memory for the third persona found in the personas folder.
- Write the result to data_oct_6/dementia/<Persona.name>.json and also return the JSON in the chat, matching example.json’s structure exactly.

Inputs
- Persona file: third file (by ascending filename) within the personas folder at repo root.
- start_deterioration_age: taken from the persona file; used to control decline.
- example.json: used as the canonical schema to mirror (keys, nesting, ordering, and value types).

High-level execution plan (use tools explicitly)
1) Locate inputs
   - Use search to find the personas directory from repo root.
   - List files in personas (search or codebase). Pick the third by ascending filename.
   - Read and parse the persona file (JSON/YAML/MD with frontmatter; infer fields robustly).
   - Use search to find example.json (prefer data_oct_6/dementia/example.json; otherwise any example.json in repo). If not found, fail with a clear error.

2) Extract required fields
   - Persona.name (required): if missing, fail with a clear error.
   - start_deterioration_age (optional): if missing, default to 65.
   - Core memory anchor(s): if present (e.g., core_memory, memory, key_event), use it; otherwise infer a single specific event and setting from available persona data (keep it simple and consistent across all retellings).

3) Prepare output file path
   - Output folder: data_oct_6/dementia (create via runCommands: mkdir -p if missing).
   - Output filename: sanitize Persona.name to kebab-case ASCII, strip unsafe chars, suffix .json (e.g., “John Doe” → “john-doe.json”).
   - Overwrite if exists.

4) Mirror schema from example.json
   - Read example.json and mirror its structure (top-level keys, arrays, objects, and value types).
   - Do not add extra fields not present in example.json.
   - Only replace content values; preserve key order and shapes.

5) Generate stories (content rules)
   - Ages: 60, 63, 66, 69, 72, 75 (exactly 6 stories).
   - Perspective: first person, spoken style.
   - Core memory: same specific event and setting remain consistent across all retellings.
   - Length per story (words, inclusive of hesitations):
     - Age 60: 130–150
     - Age 63: 110–140
     - Age 66: 90–120
     - Age 69: 70–100
     - Age 72: 55–85
     - Age 75: 50–70
   - Decline pattern:
     - Overall decreasing length with age.
     - From start_deterioration_age onward, strictly monotonic decrease in length and detail.
   - Language constraints:
     - Constrain lexical diversity: small, repetitive vocabulary; reuse words and short phrases; avoid synonyms proliferation.
     - Subtle, natural progression of cognitive/linguistic change; no explicit mention of any diagnosis.
     - Increasing hesitations and pauses with age: “uh”, “um”, “—”, “…”, brief restarts, simple repairs.
     - Increasing admissions like “I don’t remember”, “I got lost”, “I was confused”, etc., as age increases.
     - Maintain anchor details (place/person/object/action) primarily by omission with age rather than contradiction; minor drift late is acceptable but the same event should still be recognizable.
   - Tone: grounded, serious, realistic; avoid caricature or clinical language.
   - Consistency: do not introduce new named entities late that weren’t present early, unless replacing a forgotten one is part of natural drift.

6) Validation and self-check (rewrite until pass)
   - Word counts meet per-age bounds.
   - Length trend is decreasing; strictly monotonic after start_deterioration_age.
   - No explicit medical terms (e.g., “Alzheimer’s”, “dementia”, “diagnosis”).
   - Core event and setting recognizable as the same across all 6 stories.
   - Vocabulary remains limited; rising hesitations/repairs across ages.
   - If any check fails, rewrite only the failing stories and re-validate.

7) Produce output
   - Fill the mirrored schema with generated content.
   - Write the JSON to data_oct_6/dementia/<sanitized persona name>.json via editFiles.
   - Also return the JSON in the chat as final output.

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
- Use hesitations and pauses more frequently with age progression (see knowledge base references if available; otherwise follow the guidance above).

Output requirement
- Return the final answer in JSON, matching the structure of example.json exactly (no extra fields), and write the same JSON file to data_oct_6/dementia/<sanitized Persona.name>.json.