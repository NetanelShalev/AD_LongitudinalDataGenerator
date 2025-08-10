---
description: 'Healthy person story retelling generator - Creates stories from personas that are healthy although aging.'
tools: ['changes', 'codebase', 'editFiles', 'problems', 'runCommands', 'search', 'searchResults', 'terminalLastCommand', 'terminalSelection']
---
read the personas folder from the root folder. for each persona (file) in the folder you should create a json file in the data_aug_10/aging folder. The file name is the Persona.name attribute that is in the file concat with suffix of "_aging".
Given the persona use the following prompt in order to generate file like the example.json file without the attribute of start_deteration_age. Except this it should has the same attributes and structure with different content.

### The prompt:
Given the following persona, generate 6 short personal stories told by the character at the following ages:
60, 63, 66, 69, 72, 75.
The character is attempting to retell the exact same specific memory at each of these ages.

### Instructions:

1. Read the persona file and extract relevant information.
2. Generate 6 short personal stories for each age (60, 63, 66, 69, 72, 75) based on the core memory.
3. Each story should reflect the character's voice and background at the current age.
4. Ensure the stories are coherent and self-contained.

The persona aging process should be reflected in the stories, showing how the character's perspective and voice evolve over time.

### Output:
Return your answer in JSON, matching the structure of the provided example.