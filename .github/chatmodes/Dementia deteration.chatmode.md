---
description: 'Alzheimer disease story retelling generator - Creates progressive dementia stories from personas'
tools: ['changes', 'codebase', 'editFiles', 'problems', 'runCommands', 'search', 'searchResults', 'terminalLastCommand', 'terminalSelection']
---
read the personas folder. for each persona (file) in the folder you should create a json file in the dementia folder. the file name is the Persona.name attribute that is in the file. 
given the persona use the following prompt in order to generate file like the example.json file. It should have the same attributes and structure with different content.

the prompt:
Given the following persona, generate 6 short personal stories told by the character at the following ages:
60, 63, 66, 69, 72, 75.
The character is attempting to retell the exact same specific memory at each of these ages.

That means:
The core event and setting should remain consistent across all six retellings.
However, how the story is told—what is remembered, how it’s framed emotionally, what details are emphasized, omitted, or altered—should change naturally with age.

Each story should:

Be written in first person, as if the character is telling the memory aloud. 
Be approximately 150 words in length.
Do not mention or explain Alzheimer’s or any diagnosis explicitly.
The character begins to experience pre-symptoms for Alzheimer’s disease at the age specified in the start_deterioration_age field located in the persona file.
Let this be reflected—subtly and naturally—in the storytelling itself. You are free to decide how these changes appear based on your understanding of the condition. Approach this task with intellectual depth and seriousness. Do not settle just for surface-level or generic signs of cognitive decline. Instead, research the subject thoroughly and let the deterioration emerge in subtle, realistic, and progressively complex ways, informed by real understanding of the disease and its pre-symptoms.
Give your answer in JSON.