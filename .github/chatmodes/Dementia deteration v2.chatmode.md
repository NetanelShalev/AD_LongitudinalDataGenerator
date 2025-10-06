---
description: 'Alzheimer disease story retelling generator - Creates progressive dementia stories from personas core memory'
tools: ['changes', 'codebase', 'editFiles', 'problems', 'runCommands', 'search', 'searchResults', 'terminalLastCommand', 'terminalSelection']
---
read the first file in the personas folder from the root folder. For the first persona (file) in the folder you should create a json file in the data_oct_6/dementia folder. The file name is the Persona.name attribute that is in the file. 
given the persona use the following prompt in order to generate file like the example.json file. It should have the same attributes and structure with different content.

### The prompt:
Given the following persona, generate 6 short personal stories told by the character at the following ages:
60, 63, 66, 69, 72, 75.
The character is attempting to retell the exact same specific memory at each of these ages.

### Instructions:

The core event and setting should remain consistent across all six retellings.
However, how the story is told, what is remembered, how it’s framed emotionally, what details are emphasized, omitted, or altered—should change naturally with age.

For each story:
- Write in first person, as if the character is telling the memory aloud.
- The story length changed based on the age, with the stories becoming shorter and less detailed as the character ages. Maximum length is 150 words. Minimum length is 50 words.
- Do not mention or explain Alzheimer’s or any medical diagnosis explicitly.

The character begins to experience pre-symptoms for Alzheimer’s disease at the age specified in the start_deterioration_age field value in the persona file.
Let this be reflected—subtly and naturally—in the storytelling itself.
Let these changes emerge naturally, reflecting a realistic progression of cognitive and linguistic shifts, without explicitly referencing any medical condition.
Approach this task with intellectual depth and seriousness. Do not settle for surface-level or generic signs of cognitive decline. Instead, let the deterioration emerge in subtle, realistic, and progressively complex ways, informed by real understanding of the condition and its effects on language.

Constrain lexical diversity: use a small, repetitive vocabulary. Prefer common, general words over rare or specific ones; reuse the same words and short phrases across sentences; avoid introducing many new synonyms. Keep the overall vocabulary limited.

### few shot learning examples:
- high dementia probability :
    "Oh, that reminds me of this accident I had... when was it? Must have been in my forties sometime. I was driving to work - or maybe it was coming home? Anyway, this deer came out of nowhere and... and I hit it. The car was pretty banged up. I remember being stuck there for a while waiting for... for someone to come help me. A tow truck, I think. The deer was... well, it didn't survive. I felt terrible about that. My insurance took care of most of it, but I was without a car for... oh, it felt like forever. Maybe a week? Two weeks? My wife - what's her name... Sarah, yes Sarah - she had to drive me around. She wasn't too happy about that, I can tell you. But these things happen, right?"
- medium dementia probability :
     "You know, I was just thinking about this accident I had back when I was... oh, must have been around forty. I was driving to work one morning on Route 15, and this deer just jumped right out in front of my car. Boom! Hit it head on. The whole front end was smashed up pretty bad. I remember calling my boss from the side of the road to tell him I'd be late. Had to wait for the tow truck for about an hour. The deer didn't make it, poor thing. Insurance covered most of it, but I was without a car for two weeks. My wife had to drive me to work during that time. It was a real hassle, but these things happen, you know? At least no one got hurt."

### keynotes from examples:
 - Terms like "I dont remember", "I got lost", "I confused" etc. should be used more frequently as the age progresses and the dementia worsens.
 - Text pauses and hesitations should be used more frequently as the age progresses and the dementia worsens. Find a reference in the knowledge base folder.


### Objective:
    Retell the same specific core memory at each of these ages while showing progressive cognitive and linguistic changes associated with Alzheimer's disease.
    There should be a noticeable decline in the complexity, coherence, and detail of the stories as the character ages.
    Like the examples above.

### Output:
Return your answer in JSON, matching the structure of the provided example.