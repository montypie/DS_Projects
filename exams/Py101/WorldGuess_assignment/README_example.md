# 🔍 Word Detective

Een woordraadspel gebouwd met Python en GitHub Copilot - vergelijkbaar met Wordle/Lingo.

## 📖 Beschrijving

Word Detective is een interactief commandline spel waarin je een geheim 5-letter Nederlands woord moet raden. Na elke poging krijg je kleurgecodeerde feedback om je te helpen het juiste woord te vinden!

## ✨ Features

- 🎮 50 Nederlandse 5-letter woorden
- 🟢 Kleurgecodeerde feedback (groen/geel/grijs emoji's)
- 🔢 6 pogingen per spel
- ✅ Input validatie
- 📊 Statistieken tracking (win rate, gemiddeld aantal pogingen)
- 🔄 Replay functie
- 💡 Duidelijke spelregels en interface

## 🎯 Spelregels

1. De computer kiest een willekeurig 5-letter Nederlands woord
2. Je hebt **6 pogingen** om het woord te raden
3. Na elke gok krijg je feedback:
   - 🟢 **Groen** = Letter is correct en op de juiste plaats
   - 🟡 **Geel** = Letter zit in het woord maar op de verkeerde plaats
   - ⚫ **Grijs** = Letter zit niet in het woord
4. Win door het woord binnen 6 pogingen te raden!

## 🎬 Voorbeeld Gameplay

```
==================================================
🔍 WORD DETECTIVE - RAAD HET WOORD!
==================================================

📊 Poging 1/6 (nog 6 over)
Voer je gok in (5 letters): stoel

  S  T  O  E  L
  ⚫  ⚫  🟡  🟡  ⚫

📊 Poging 2/6 (nog 5 over)
Voer je gok in (5 letters): kopen

  K  O  P  E  N
  🟢  🟢  🟢  🟢  🟢

==================================================
🎉 GEFELICITEERD! Je hebt het woord geraden!
✨ Het woord was: KOPEN
📈 Aantal pogingen: 2/6
==================================================
```

## 🛠️ Requirements

- Python 3.6 of hoger
- Geen externe libraries nodig (gebruikt alleen standard library)

## 📥 Installatie

1. Clone of download dit project
2. Zorg dat Python 3 geïnstalleerd is:
   ```bash
   python --version
   ```

## 🚀 Gebruik

### Optie 1: Python bestand
```bash
python word_detective.py
```

### Optie 2: Jupyter Notebook
```bash
jupyter notebook word_detective.ipynb
```

Of open het `.ipynb` bestand in VS Code en run de cellen.

## 🎮 Hoe te Spelen

1. Start het spel
2. Lees de spelregels
3. Voer een 5-letter woord in (alleen letters, geen cijfers of symbolen)
4. Bekijk de feedback:
   - Groene emoji's = juiste letters op de juiste plek
   - Gele emoji's = letters zitten in het woord maar op de verkeerde plek
   - Grijze emoji's = letters zitten niet in het woord
5. Gebruik de feedback om je volgende gok te kiezen
6. Raad het woord binnen 6 pogingen!

## 💡 Tips voor Spelers

- **Start met een woord met veel verschillende letters** om meer informatie te krijgen
- Gebruik **veel voorkomende letters** zoals E, N, A, R, T
- Let goed op de **gele emoji's** - die letters zitten in het woord!
- Als een letter **grijs** is, gebruik hem niet opnieuw
- Denk aan **Nederlandse woorden** - geen Engelse woorden!

## 🧠 Technische Details

### Functies

- `select_random_word()`: Selecteert een willekeurig woord uit de woordenlijst
- `validate_input(guess)`: Controleert of de input geldig is (5 letters, alleen letters)
- `get_feedback(secret_word, guess)`: Genereert feedback emoji's
- `display_feedback(guess, feedback)`: Toont gok en feedback netjes
- `play_game()`: Hoofdgame loop voor één spel
- `play_again()`: Vraagt of de speler opnieuw wil spelen
- `display_statistics(stats)`: Toont spelstatistieken
- `main()`: Entry point van het programma

### Hoe werkt het feedback systeem?

Het feedback algoritme werkt in twee stappen:

1. **Eerste pass**: Markeer alle exacte matches (groene emoji's)
2. **Tweede pass**: Voor overige letters, check of ze in het woord zitten (gele/grijze emoji's)

Dit zorgt ervoor dat **dubbele letters** correct behandeld worden:
- Als het woord "APPEL" is en je raadt "AAAAA":
  - Eerste A = 🟢 (correct positie)
  - Tweede A = 🟡 (zit in woord op positie 2)
  - Derde, vierde, vijfde A = ⚫ (niet meer beschikbaar)

## 🤖 Gebouwd met GitHub Copilot

Dit project is gemaakt met behulp van GitHub Copilot! Gebruikte features:

- ✅ **Inline Suggestions**: Tab completion voor code generatie
- ✅ **Copilot Chat**: `/explain`, `/fix`, `/tests`, `/doc` commands
- ✅ **Inline Chat (Ctrl+I)**: Snelle code aanpassingen
- ✅ **Docstring-driven development**: Comments → code
- ✅ **Test generation**: Automatische test cases

## 📝 Licentie

Dit is een educatief project voor Syntra - Module 1: Leren Programmeren in Python.

## 🙏 Credits

- Gemaakt door: [Jouw Naam]
- Vak: Leren Programmeren in Python
- Module: GitHub Copilot
- Docent: [Docent Naam]

## 🐛 Problemen of Vragen?

Als je bugs vindt of vragen hebt:
1. Check of je Python 3.6+ gebruikt
2. Zorg dat je alleen 5-letter input geeft
3. Check of je terminal emoji's ondersteunt (anders zie je vraagtekens)

## 🚀 Mogelijke Uitbreidingen

Ideeën voor verdere ontwikkeling:
- 🎚️ Meerdere moeilijkheidsgraden (4, 5, 6 letter woorden)
- 💾 High score systeem met persistentie (JSON file)
- 🎨 GUI met tkinter of pygame
- 🌐 Online woordenlijst API integratie
- 🔊 Geluidseffecten bij win/lose
- 👥 Twee-speler modus
- 📈 Uitgebreide statistieken (streak, beste tijd, etc.)
- 🏆 Achievement systeem

---

**Veel plezier met Word Detective! 🔍🎉**
