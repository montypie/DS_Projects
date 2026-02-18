# Word Detective Game 🔍

A word guessing game similar to Wordle, where players try to guess a 5-letter Dutch word within 6 attempts.

## Game Description

Word Detective is a command-line game where players attempt to guess a randomly selected 5-letter Dutch word. After each guess, the game provides feedback using colored circles to indicate:

- 🟢 Green: Letter is correct and in the right position
- 🟡 Yellow: Letter is in the word but in the wrong position
- ⚫ Black: Letter is not in the word

## How to Run

1. Make sure you have Python 3.x installed on your system
2. Clone or download this repository
3. Navigate to the game directory
4. Run the game:
```bash
python word_detective.py
```
5. To run the tests (install pytest for better feedback):
```bash
python -m pytest -q "path_to_folder/tests.py"
```

## Game Rules

1. The computer selects a random 5-letter Dutch word
2. You have 6 attempts to guess the word
3. Each guess must be:
   - Exactly 5 letters long
   - Containing only letters (no numbers or special characters)
4. After each guess, you'll receive feedback showing:
   - Which letters are correct and in the right position (🟢)
   - Which letters are in the word but in wrong positions (🟡)
   - Which letters are not in the word (⚫)
5. Win by guessing the secret word within 6 attempts
6. Play again or quit.

## Example Gameplay

```
🔍 Welcome to Word Detective! 🕵️
Your mission, should you choose to accept it...
╔══════════════════════════════════════════╗
║        📜 Detective's Handbook 📜       ║
╠══════════════════════════════════════════╣
║ 🎯 Mission: Crack the 5-letter Dutch code║
║ ⏱️ Time: You have 6 attempts to solve it ║
║                                           ║
║ 🔍 Your Investigation Tools:             ║
║ 🟢 → Perfect match! Letter & position    ║
║ 🟡 → Letter found in different spot      ║
║ ⚫ → Letter not in the secret word       ║
╚══════════════════════════════════════════╝

💭 Think carefully, detective. Every guess counts!
🚀 Your investigation starts now...

Enter your guess: APPEL

🔍 Detective's Analysis 🔍
📝 Your guess: APPEL
🎯 Clues found: 🟢 ⚫ ⚫ 🟡 ⚫
✨--------------------------------------✨

You have 5 attempts left.

📊 Performance Analytics 📊
╔════════════════════════════════════╗
║ 🎮 Total Games    │             1 ║
║ 🏆 Victories      │             0 ║
║ ⭐ Success Rate   │          0.0% ║
║ 🎯 Avg. Attempts  │           1.0 ║
╚════════════════════════════════════╝
🔍 Rookie Detective - Keep Practicing! 🔍

Do you want to play again? (j/ja/y/yes): n

🎭 Case Closed! Thanks for being an amazing detective! 🔍
👋 Until our next investigation... 🕵️
```

## Features

- 📝 50+ Dutch 5-letter words
- ✅ Input validation
- 🎯 Accurate feedback system handling duplicate letters
- 📊 Game statistics tracking:
  - Games played
  - Games won
  - Win rate
  - Average attempts per game
- 🔄 Play again functionality
- 📈 Progress tracking with remaining attempts
- 🎮 User-friendly interface with emoji feedback

## 💡 Tips for Players

- Start with words containing different common letters like E, N, A, R, T
- Pay close attention to 🟡 yellow emojis - these letters are in the word!
- If a letter shows ⚫, don't use it in your next guess
- Remember to think in Dutch words - no English words allowed!

## 🧠 Technical Details

### Functions

- `select_random_word()`: Picks a random word from the word list
- `validate_input(guess)`: Validates input (5 letters, letters only)
- `get_feedback(secret_word, guess)`: Generates feedback emojis
- `display_feedback(guess, feedback)`: Shows guess and feedback nicely
- `play_word_detective()`: Main game loop for one game
- `display_statistics()`: Shows game statistics
- `main()`: Entry point of the program

### How the Feedback System Works

The feedback algorithm works in two passes:

1. **First Pass**: Mark all exact matches (🟢 green emojis)
2. **Second Pass**: For remaining letters, check if they exist in the word (🟡 yellow or ⚫ black emojis)

This ensures correct handling of **duplicate letters**:
- If the word is "APPEL" and you guess "AAAAA":
  - First A = 🟢 (correct position)
  - Other A's = ⚫ (not available anymore)

## 🛠️ Requirements

- Python 3.x
- Terminal/Command Prompt with emoji support

## 🚀 Future Enhancements

Potential improvements for future versions:
- 🎚️ Multiple difficulty levels (4, 5, 6 letter words)
- 💾 High score system with persistence
- 🌐 Online word list integration
- 🔊 Sound effects for win/lose
- 👥 Two-player mode
- 📈 Extended statistics (streaks, best time, etc.)
- 🏆 Achievement system

## 🐛 Troubleshooting

If you encounter issues:
1. Verify you're using Python 3.x
2. Ensure you only input 5-letter words
3. Check if your terminal supports emoji display
4. Make sure you're using Dutch words only

## ✅ Testing
The current test suite verifies:

1. Input validation with various edge cases
2. Perfect matches for words
3. Tricky duplicate letter scenarios
4. Complete misses
5. Mixed feedback combinations
6. Error handling

## 📝 Credits

- Created by: Yulia Kallistratova (in collab with GitHub copilot)
- Created: October 27, 2025

## Contributing

Feel free to fork this repository and make improvements. Pull requests are welcome!

---

**Happy Detective Work! 🔍 🕵️**