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

Instructions:

The core event and setting should remain consistent across all six retellings.
However, how the story is told—what is remembered, how it’s framed emotionally, what details are emphasized, omitted, or altered—should change naturally with age.
For each story:

Write in first person, as if the character is telling the memory aloud.
Each story should be approximately 150 words in length.
Do not mention or explain Alzheimer’s or any diagnosis explicitly.
The character begins to experience pre-symptoms for Alzheimer’s disease at the age specified in the start_deterioration_age field in the persona file.
Let this be reflected—subtly and naturally—in the storytelling itself. As the character ages, allow their language to evolve in nuanced ways:
Early stories (before symptoms): Use rich, varied vocabulary, detailed descriptions, and complex sentence structures.
As the character approaches and passes the age of initial cognitive changes, gradually simplify the language. The variety of words may decrease, with more repetition of words or phrases, and increased reliance on familiar, everyday language.
Over time, let the stories show a subtle reduction in the use of less common words, and a shift toward simpler grammatical structures. The narrative may become less detailed, with some information omitted or replaced by vague references, and occasional difficulty recalling specific names or terms.
Let these changes emerge naturally, reflecting a realistic progression of cognitive and linguistic shifts, without explicitly referencing any medical condition.
Approach this task with intellectual depth and seriousness. Do not settle for surface-level or generic signs of cognitive decline. Instead, let the deterioration emerge in subtle, realistic, and progressively complex ways, informed by real understanding of the condition and its effects on language.

Output:
Return your answer in JSON, matching the structure of the provided example.