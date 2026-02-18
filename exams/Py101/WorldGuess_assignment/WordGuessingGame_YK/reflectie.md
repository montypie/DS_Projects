**Reflectie document** (kort, max 1 pagina):
   - Welke Copilot features vond je het meest nuttig?
   - Waar had je moeite mee?
   - Voorbeelden van goede en slechte Copilot suggesties
   - 3 dingen die je geleerd hebt

## Best features (agent):
1. Generating and fixing tests (such a time saver!)
2. Adjusting surrounding files (like tests and README) after major code refactoring
3. Following example, i.e. when asked to create or modify something based on something else. (Case in point: README_example.md)

## Suggestions examples:
1. Good: copilot took context into account.
Ex. At some point it suggested to use classes, then realized (without any hint!) that the assignment description explicitely "no classes" and adjusted accordingly.
2. Bad: Sometimes too wordy or plain wrong docstrings

## Annoyances:
1. It took 4 attempts to generate a word list. cpt4.1 generated 5 and 4 letter words, although instruction stated clearly 5-letter words only. Moreover, it lied that "all words are now exactly 5 letters long". Second time it just removed 4-letter words out of the list, while instruction stated clearly it has to be 50 at least words. Third time it added repeated words. cpt5-mini refused to generate any list whatsoever. Finally, Claude Sonnet 3.5 did the right thing.

2. In Fase 4 (feedback function), gpt4.1 hardcoded 5 as a range for the loop. Claude Sonnet3.5 made a slightly better job, which I used in the program. But when asked to "Add comments explaining the logic for duplicate letters" it wrote:
"Example: If secret="APPEL" and guess="PEPEL", the first P gets yellow and second P gets black since there's **only one P in the secret word**"!

## Learned:
1. "belt and braces" principle (copilot insisted on extra check that secret word and guess have the same length despite validation function).
2. different ways to run tests in VS code (copilot gave an overview of options with pros and cons).
3. one has to be very patient, give very clear instructions and always doublecheck for blunters, "left overs" after refactoring, inconsistencies... At this point, the ai-generated output cannot be blindly trusted.

## Overall impression:
Compared to the first two assignements without copilot this one has been more cumbersome and less enjoyable. Hopefully it gets better with practice.