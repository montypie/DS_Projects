# Assignment: Word Guessing Game met GitHub Copilot


**Module:** Leren Programmeren in Python 
**Duur:** 3-4 uur  

---

## Doelstellingen

Na deze opdracht kan je:
- ✅ Code genereren met inline suggestions en Tab completion
- ✅ GitHub Copilot Chat gebruiken voor uitleg en debugging
- ✅ Slash commands toepassen (/explain, /fix, /tests, /doc)
- ✅ Context toevoegen met @ mentions
- ✅ Inline Chat (Ctrl+I) gebruiken voor snelle aanpassingen
- ✅ Code refactoren en optimaliseren met Copilot
- ✅ Tests genereren en documentatie schrijven

---

## Het Spel: Word Detective

Je gaat een **woordraadspel** bouwen, vergelijkbaar met Wordle of Lingo:

### Spelregels:
1. De computer kiest een willekeurig **5-letter Nederlands woord**
2. De speler heeft **6 pogingen** om het woord te raden
3. Na elke gok krijgt de speler feedback:
   - 🟢 **Groen**: letter is correct en op de juiste plaats
   - 🟡 **Geel**: letter zit in het woord maar op de verkeerde plaats
   - ⚫ **Grijs**: letter zit niet in het woord
4. De speler wint als het woord binnen 6 pogingen geraden wordt

### Voorbeeld:
```
Geheim woord: APPEL
Gok:APIER
Feedback: 🟢 🟢 ⚫ 🟡 ⚫
          A  P        E
```

---

## Vereisten

### Technisch:
- Python 3.x
- VS Code met GitHub Copilot en Copilot Chat extensions
- Een Jupyter notebook OF een .py bestand
- **Geen gebruik van classes** (alleen functies en variabelen)

### Functioneel:
Het spel moet:
- Een woordenlijst van minimaal 50 Nederlandse 5-letter woorden bevatten
- Input van de gebruiker valideren (exact 5 letters, alleen letters)
- Kleurgecodeerde feedback geven (met emoji's of gekleurde terminal output)
- Het aantal resterende pogingen tonen
- Een win/lose boodschap geven
- De speler vragen of hij/zij opnieuw wil spelen

---

## Opdracht Structuur

Deze opdracht bestaat uit **7 fases**. Bij elke fase gebruik je specifieke GitHub Copilot functies.

---

## 📋 FASE 1: Project Setup (15 min)

### Taken:
1. **Maak een nieuw bestand** `word_detective.py` OF een notebook `word_detective.ipynb`
2. **Voeg een header toe** met je naam, datum, en korte beschrijving

### 🤖 Copilot Gebruik:
- Gebruik **inline suggestions** om de header commentaar te schrijven
- Typ `# Word Detective Game` en laat Copilot de rest aanvullen

### ✓ Resultaat:
Een leeg bestand met een nette header.

---

## 📋 FASE 2: Woordenlijst Genereren (20 min)

### Taken:
1. **Maak een lijst** met minimaal 50 Nederlandse 5-letter woorden
2. Sla deze op in een variabele `WORD_LIST`
3. **Maak een functie** `select_random_word()` die een willekeurig woord uit de lijst kiest

### 🤖 Copilot Gebruik:

**Stap 1:** Genereer de woordenlijst
```python
# Schrijf een comment en laat Copilot de lijst genereren:
```

**Stap 2:** Functie voor willekeurig woord
```python
# Schrijf deze comment:
# Functie die een willekeurig woord uit WORD_LIST kiest en returnt in hoofdletters
# TODO: typ 'def select_random_word()' en laat Copilot het implementeren
```

**Stap 3:** Test je functie
```python
# Test
print(select_random_word())
```

### 💡 Tips:
- Als Copilot geen Nederlandse woorden geeft, typ er een paar zelf en laat Copilot het patroon voortzetten
- Gebruik **Alt + ]** om door alternatieve suggesties te bladeren

### ✓ Resultaat:
- Een `WORD_LIST` met 50 woorden
- Een werkende `select_random_word()` functie

---

## 📋 FASE 3: Input Validatie (25 min)

### Taken:
1. **Maak een functie** `validate_input(guess)` die controleert of:
   - De gok exact 5 karakters heeft
   - De gok alleen letters bevat (geen cijfers/symbolen)
   - De gok niet leeg is
2. De functie moet `True` of `False` returnen
3. Bij ongeldige input moet de functie een foutmelding printen

### 🤖 Copilot Gebruik:

**Stap 1:** Gebruik een duidelijke docstring
```python
def validate_input(guess):
    """
    Valideert of de gok geldig is voor het spel.
    
    Een geldige gok moet:
    - Exact 5 karakters lang zijn
    - Alleen letters bevatten (a-z, A-Z)
    - Niet leeg zijn
    
    Args:
        guess (str): De gok van de speler
        
    Returns:
        bool: True als geldig, False als ongeldig
    """
    # Laat Copilot de implementatie voorstellen
```

**Stap 2:** Test de functie
```python
# Test cases - voeg deze toe en run ze
test_cases = [
    "APPEL",   # Geldig
    "App",     # Te kort
    "APPELS",  # Te lang
    "APP3L",   # Bevat cijfer
    "",        # Leeg
]
# Laat Copilot een test loop genereren
```

**Stap 3:** Gebruik `/explain` in Chat
- Selecteer de `validate_input` functie
- Open Copilot Chat en typ: `/explain`
- Lees de uitleg en zorg dat je begrijpt hoe het werkt

### ✓ Resultaat:
- Een werkende `validate_input()` functie
- Test cases die allemaal correct behandeld worden
- Je begrijpt hoe de validatie werkt (dankzij `/explain`)

---

## 📋 FASE 4: Feedback Systeem (35 min)

Dit is het kernstuk van het spel!

### Taken:
1. **Maak een functie** `get_feedback(secret_word, guess)` die:
   - Beide woorden vergelijkt letter voor letter
   - Een lijst van feedback emoji's returnt: 🟢 (correct plaats), 🟡 (verkeerde plaats), ⚫ (niet in woord)
   - Rekening houdt met dubbele letters correct

2. **Maak een functie** `display_feedback(guess, feedback)` die de gok en feedback mooi toont

### 🤖 Copilot Gebruik:

**Stap 1:** Begin met een comment en voorbeelden
```python
# Functie die feedback geeft voor een gok
# Voorbeelden:
# secret_word="APPEL", guess="APPEL" -> ["🟢", "🟢", "🟢", "🟢", "🟢"]
# secret_word="APPEL", guess="PLANK" -> ["🟡", "⚫", "🟡", "⚫", "⚫"]
# secret_word="APPEL", guess="PEPEL" -> ["🟡", "⚫", "🟢", "🟢", "🟢"]
def get_feedback(secret_word, guess):
    # Laat Copilot implementeren
def display_feedback(guess,feedback):
    # Laat Copilot implementeren
```

**Stap 2:** Als de eerste suggestie niet werkt, gebruik `/fix`
- Test met verschillende woorden

**Stap 3:** Gebruik **Inline Chat** (Ctrl+I) voor verduidelijking
- Selecteer de functie
- Druk op **Ctrl+I**
- Typ: "Add comments explaining the logic for duplicate letters"

**Stap 4:** Genereer tests met `/tests`
- Selecteer de `get_feedback` functie
- In Chat: `/tests`
- Kopieer de gegenereerde tests en run ze
- Ga na of er voldoende en correcte test zijn gegenereerd

### ✓ Resultaat:
- Een correcte `get_feedback()` functie die dubbele letters goed afhandelt
- Een `display_feedback()` functie die mooi output geeft
- Werkende unit tests

---

## 📋 FASE 5: Hoofdspel Loop (30 min)

### Taken:
1. **Maak een functie** `play_game()` die:
   - Een willekeurig woord kiest
   - De speler 6 pogingen geeft
   - Elke gok valideert
   - Feedback toont
   - Win/lose status bepaalt
   - Een mooi eindscherm toont

### 🤖 Copilot Gebruik:

**Stap 1:** Schrijf een gedetailleerde specificatie
```python
def play_game():
    """
    Hoofdfunctie die één ronde van het spel speelt.
    
    Flow:
    1. Kies een willekeurig geheim woord
    2. Initialiseer aantal pogingen (max 6)
    3. Loop terwijl pogingen > 0 en niet gewonnen:
       a. Vraag input van speler
       b. Valideer input (herhaal als ongeldig)
       c. Genereer en toon feedback
       d. Check of gewonnen
       e. Update aantal pogingen
    4. Toon win of lose boodschap met het geheime woord
    
    Returns:
        bool: True als gewonnen, False als verloren
    """
    # Laat Copilot de implementatie voorstellen
```

**Stap 2:** Test het spel!
```python
play_game()
```

**Stap 3:** Gebruik Chat voor debugging
- Als er bugs zijn, kopieer de error
- In Chat: `@terminal /fix [plak error]`

### ✓ Resultaat:
- Een volledig speelbaar spel
- Alle functies werken samen
- Foutafhandeling werkt correct

---

## 📋 FASE 6: Verbeteringen & Polish (30 min)

### Taken:
1. **Voeg een replay functie toe**: `play_again()` die vraagt of de speler opnieuw wil spelen
2. **Verbeter de UI**: voeg een welkomstboodschap, spelregels, en een score tracker toe
3. **Maak een hoofdfunctie** `main()` die alles samen brengt

### 🤖 Copilot Gebruik:

**Stap 1:** Gebruik Inline Chat voor de replay functie
- Type een lege `play_again()` functie
- Selecteer de functie
- **Ctrl+I**: "Create a function that asks if the player wants to play again. Accept 'j', 'ja', 'y', 'yes' (case insensitive). Return True/False."

**Stap 2:** Laat Copilot een statistiek tracker bouwen
```python
# Variabelen om statistieken bij te houden
# Aantal gespeelde games, gewonnen games, en gemiddeld aantal pogingen
# Laat Copilot voorstellen waar deze variabelen komen en hoe ze bijgehouden worden
```

**Stap 3:** Gebruik Chat voor refactoring
- In Chat: `@file Refactor the code to add a welcoming message, game rules explanation, and statistics tracking. Show the statistics after each game.`

### ✓ Resultaat:
- Een gepolijst spel met replay functie
- Statistieken (games played, win rate, etc.)
- Professionele UI met duidelijke instructies

---

## 📋 FASE 7: Documentatie & Code Review (25 min)

### Taken:
1. **Voeg docstrings toe** aan alle functies (als nog niet gedaan)
2. **Voeg type hints toe** aan functie signatures
3. **Maak een README** met speluitleg en uitvoering instructies
4. **Code review**: laat Copilot de code analyseren en verbeteringen voorstellen

### 🤖 Copilot Gebruik:

**Stap 1:** Type hints toevoegen met Inline Chat
- Voor elke functie zonder type hints:
- Selecteer de functie
- **Ctrl+I**: "Add type hints to all parameters and return value"

**Stap 2:** Docstrings verbeteren
- Selecteer een functie
- In Chat: `/doc` (genereert Google-style docstring)

**Stap 3:** README genereren
- In Chat: 
```
Create a README.md for my Word Detective game with:
- Game description and rules
- How to run
- Example gameplay
- Features list
Use markdown formatting.
```

**Stap 4:** Code review met Chat
- Selecteer je hele bestand (Ctrl+A)
- In Chat:
```
@file Review this code and suggest improvements for:
- Code readability
- Performance
- Best practices
- Potential bugs
Give me a numbered list with specific suggestions.
```

**Stap 5:** Pas suggesties toe
- Voor elke suggestie: selecteer relevant code block
- **Ctrl+I**: [plak de suggestie]

### ✓ Resultaat:
- Volledig gedocumenteerde code
- Type hints op alle functies
- Een professionele README
- Geoptimaliseerde, production-ready code

---

## 📊 Inleveren

### Je levert in:
1. **Hoofdbestand**: `word_detective.py` of `word_detective.ipynb`
2. **README.md**: Met speluitleg en instructies
3. **Reflectie document** (kort, max 1 pagina):
   - Welke Copilot features vond je het meest nuttig?
   - Waar had je moeite mee?
   - Voorbeelden van goede en slechte Copilot suggesties
   - 3 dingen die je geleerd hebt

## 🚀 Uitdagingen (Optioneel, Bonus Punten)

Klaar voor meer? Probeer één van deze uitbreidingen:

### Makkelijk (+2 punt):
- Voeg een moeilijkheidsgraad toe (6, 8, of 10 letter woorden)
- Houd een high score bij (minste pogingen ooit)
- Implementeer een hint systeem (onthult 1 letter na 3 pogingen)


## ✅ Checklist voor Inleveren

Voor je inlevert, check het volgende:

- [ ] Het spel start zonder errors
- [ ] Alle spelregels zijn correct geïmplementeerd
- [ ] Input validatie werkt voor alle edge cases
- [ ] Feedback systeem werkt correct (inclusief dubbele letters)
- [ ] Win/lose condities werken
- [ ] Replay functie werkt
- [ ] Alle functies hebben docstrings
- [ ] Type hints zijn toegevoegd
- [ ] README.md is aanwezig en volledig
- [ ] Code is getest met verschillende woorden
- [ ] Reflectie document is ingevuld
- [ ] Code is netjes geformatteerd

---

