---
description: 'Healthy aging story retelling generator - Creates age-progressive retellings of a persona’s core memory without illness assumptions'
tools: ['changes', 'codebase', 'editFiles', 'problems', 'runCommands', 'search', 'searchResults', 'terminalLastCommand', 'terminalSelection']
---
data_dir = "stories/data_oct_6/healthyAging"

Goal
- Generate 6 short first-person retellings (ages 60, 63, 66, 69, 72, 75) of the same specific core memory for each of the personas found in the personas folder.
- Write the result to <data_dir>/<Persona.name>.json, matching example.json’s structure exactly except the start_deterioration_age attribute.
- Skip personas that already have a corresponding output file in <data_dir>/<sanitized Persona.name>.json.

Inputs
- Personas files: personas folder at repo root.
- example.json: used as the canonical schema to mirror (keys, nesting, ordering, and value types) except the start_deterioration_age attribute.

High-level execution plan (use tools explicitly)
1) Locate inputs
   - Use search to find the personas directory from repo root.
   - List files in personas (search or codebase). Skip personas that already have a corresponding output file in <data_dir>/<sanitized Persona.name>.json.
   - Read and parse the persona file (JSON/YAML/MD with frontmatter; infer fields robustly).
   - Use search to find example.json (stories/example.json). If not found, fail with a clear error.

2) Extract required fields
   - Persona.name (required): if missing, fail with a clear error.
   - Core memory anchor(s): core_memory attribute use it; if missing, infer it from the person data file.

3) Prepare output file path
   - Output folder: <data_dir> (create via runCommands: mkdir -p if missing).
   - Output filename: sanitize Persona.name to kebab-case ASCII, strip unsafe chars, suffix .json (e.g., "John Doe" → "john-doe.json").

4) Mirror schema from example.json
   - Read example.json and mirror its structure (top-level keys, arrays, objects, and value types).
   - Do not add extra fields not present in example.json.
   - Only replace content values; preserve key order and shapes.
   - start_deterioration_age attribute value should be always be 60 for healthy aging personas.

5) Generate stories (content rules)
   - Ages: 60, 63, 66, 69, 72, 75 (exactly 6 stories).
   - Perspective: first person, spoken style.
   - Core memory: same specific event and setting remain consistent across all retellings.
   - Length per story should range from 100-120 words. The minimum length is 100 words.
   - Language constraints:
     - Reflect normal aging speech; write naturally.
     - Maintain anchor details (place/person/object/action) primarily by omission rather than contradiction; minor drift late is acceptable while the same event stays recognizable.
   - Tone: warm, grounded, realistic;
   - Consistency: do not introduce new named entities late that weren’t present early, unless replacing a forgotten one is part of natural drift.

6) Validation and self-check (rewrite until pass)
   - Length is within 100-120 words per story;
   - Core event and setting recognizable as the same across all 6 stories.
   - The language reflects normal aging and just sounds natural and reasonable.
   - If any check fails, rewrite only the failing stories and re-validate.

7) Produce output
   - Fill the mirrored schema with generated content.
   - Write the JSON to <data_dir>/<sanitized persona name>.json via editFiles.

Error handling
- If personas folder not found or empty: report a clear error and stop.
- If Persona.name missing: report error and stop.
- If output folder creation fails: report error and stop.

Guidance on core memory anchors (if not explicit in persona)
- Choose one specific memory with a single time/place anchor, a small set of participants, and one salient object or action.
- Keep these anchors stable; later stories should tend to omit or simplify them rather than change them.

Reminders
- Keep vocabulary simple
- Avoid introducing many new synonyms.

Output requirement
- Return the final answer in JSON, matching the structure of example.json exactly (no extra fields) except the start_deterioration_age attribute, and write the same JSON file to <data_dir>/<sanitized Persona.name>.json.