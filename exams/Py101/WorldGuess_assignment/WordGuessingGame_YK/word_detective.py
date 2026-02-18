# Yulia Kallistratova, 27-10-2025
# Word Detective Game
# This program allows the user to play a word detective game where they guess a hidden word by suggesting letters.
# The program provides feedback on correct and incorrect guesses.
# The game continues until the user either guesses the word or runs out of attempts.
# The user can choose to play multiple rounds.

import random
import os

# Game constants
MAX_ATTEMPTS: int = 6
WORD_LENGTH: int = 5
FEEDBACK_CORRECT: str = "🟢"
FEEDBACK_WRONG_POSITION: str = "🟡"
FEEDBACK_INCORRECT: str = "⚫"
VALID_REPLAY_RESPONSES: set[str] = {'j', 'ja', 'y', 'yes'}

# Game statistics
games_played: int = 0
games_won: int = 0
total_attempts: int = 0

# List of 50 unique 5-letter Dutch words
WORD_LIST = [
    "appel", "boter", "water", "fiets", "stoel", "plant", "taart", "draad", "brood", "kaart",
    "haard", "molen", "baker", "groen", "blauw", "zwart", "bruin", "staan", "slaan", "praat",
    "speel", "kraan", "traan", "slaap", "steel", "stuur", "droom", "toren", "leger", "regen",
    "weken", "lezen", "leven", "beren", "varen", "koken", "wonen", "horen", "lopen", "sloot",
    "sport", "storm", "broek", "stoep", "sterk", "meldt", "start", "stopt", "markt", "macht"
]

def select_random_word() -> str:
    """
    Selects a random word from WORD_LIST and converts it to uppercase.
    Raises IndexError if WORD_LIST is empty.
    """
    if not WORD_LIST:
        raise IndexError("Word list is empty! Cannot select a word.")
    return random.choice(WORD_LIST).upper()

def validate_input(guess: str) -> tuple[bool, str]:
    """
    Validates whether the guess is valid for the game.
    Returns:
        - is_valid: True if guess is valid, False otherwise
        - error_message: Empty string if valid, error if not
    """
    guess = guess.strip()
    
    if not guess:
        return False, "Input cannot be empty."
    if len(guess) != WORD_LENGTH:
        return False, f"Guess must be exactly {WORD_LENGTH} letters long."
    if not guess.isalpha():
        return False, "Guess must contain only letters."
    
    return True, ""

def get_feedback(secret_word: str, guess: str) -> list[str]:
    """
    Generates feedback for a guess compared to the secret word.
    Returns a list of emoji feedback indicators:
            🟢 (FEEDBACK_CORRECT): correct letter in correct position
            🟡 (FEEDBACK_WRONG_POSITION): correct letter in wrong position
            ⚫ (FEEDBACK_INCORRECT): letter not in word
    """
    # Enforce function contract regardless input validation
    if len(secret_word) != len(guess):
        raise ValueError("Secret word and guess must be the same length")

    word_length = len(secret_word)
    feedback = [None] * word_length  # Preallocate list
    remaining_secret = list(secret_word)
    remaining_guess = list(guess)

    # First pass: mark correct positions
    for i in range(word_length):
        if remaining_guess[i] == remaining_secret[i]:
            feedback[i] = FEEDBACK_CORRECT
            remaining_secret[i] = None
            remaining_guess[i] = None

    # Second pass: check remaining letters
    for i in range(word_length):
        if feedback[i] is not None:
            continue
        
        if remaining_guess[i] is not None and remaining_guess[i] in remaining_secret:
            feedback[i] = FEEDBACK_WRONG_POSITION
            idx = remaining_secret.index(remaining_guess[i])
            remaining_secret[idx] = None
        else:
            feedback[i] = FEEDBACK_INCORRECT

    return feedback

def clear_screen() -> None:
    """ Clears the terminal screen before starting a new game """
    os.system('cls' if os.name == 'nt' else 'clear')

def display_feedback(guess: str, feedback: list[str]) -> None:
    """ Displays the guess along with its feedback """
    feedback_str = ' '.join(feedback)
    print("\n🔍 Detective's Analysis 🔍")
    print(f"📝 Your guess: {guess}")
    print(f"🎯 Clues found: {feedback_str}")
    print('✨' + '-' * 38 + '✨')

def display_game_rules() -> None:
    """ Displays welcome message and game rules """
    print("\n🔍 Welcome to Word Detective! 🕵️")
    print("Your mission, should you choose to accept it...")
    print("╔══════════════════════════════════════════╗")
    print("║        📜 Detective's Handbook 📜        ║")
    print("╠══════════════════════════════════════════╣")
    print(f"║ 🎯 Mission: Crack the {WORD_LENGTH}-letter Dutch word║")
    print(f"║ ⏱️  Time: You have {MAX_ATTEMPTS} attempts to solve it ║")
    print("║                                          ║")
    print("║ 🔍 Your Investigation Tools:             ║")
    print(f"║ {FEEDBACK_CORRECT} → Perfect match! Letter & position    ║")
    print(f"║ {FEEDBACK_WRONG_POSITION} → Letter found in different spot      ║")
    print(f"║ {FEEDBACK_INCORRECT} → Letter not in the secret word       ║")
    print("╚══════════════════════════════════════════╝")
    print("\n💭 Proceed carefully, detective. Every guess counts!")
    print("🚀 Your investigation starts now...\n")

def play_word_detective() -> tuple[bool, int]:
    """
    Plays one round of the Word Detective game.
    
    Flow:
    1. Choose a random secret word
    2. Initialize number of attempts
    3. Loop while attempts > 0 and not won:
       a. Ask for player input
       b. Validate input (repeat if invalid)
       c. Generate and display feedback
       d. Check if won
       e. Update number of attempts
    4. Display win or lose message with the secret word
    
    Returns bool: True if won, False if lost
    """
    secret_word = select_random_word()
    attempts = MAX_ATTEMPTS
    won = False

    while attempts > 0 and not won:
        guess = input("Enter your guess: ").upper()

        is_valid, error_message = validate_input(guess)
        if not is_valid:
            print(f"Invalid input: {error_message}")
            continue

        feedback = get_feedback(secret_word, guess)
        display_feedback(guess, feedback)

        if guess == secret_word:
            won = True
            break

        attempts -= 1
        if attempts != 0:
            print(f"\nYou have {attempts} attempts left.")

    attempts_used = MAX_ATTEMPTS - attempts
    if won:
        print(f"\n🎉 FANTASTIC! 🎉")
        print(f"🌟 You cracked the code: {secret_word} 🌟")
        if attempts_used == 1:
            print("🏆 First try! You're a word detective genius! 🏆")
        elif attempts_used <= 3:
            print("✨ Impressive detective work! ✨")
        else:
            print("🎯 Well done, detective! 🎯")
    else:
        print(f"\n😅 Almost had it! 😅")
        print(f"The mysterious word was: ✨ {secret_word} ✨")
        print("🔍 Keep investigating, detective! You'll crack the next one! 🔍")

    return won, attempts_used

def display_statistics() -> None:
    """
    Displays current game statistics including games played, won, and average attempts
    """
    win_rate = (games_won / games_played * 100) if games_played > 0 else 0
    avg_attempts = (total_attempts / games_played) if games_played > 0 else 0
    
    print("\n📊 Performance Analytics 📊")
    print("╔════════════════════════════════════╗")
    print(f"║ 🎮 Total Games    │ {games_played:^14} ║")
    print(f"║ 🏆 Victories      │ {games_won:^14} ║")
    print(f"║ ⭐ Success Rate   │ {win_rate:^13.1f}% ║")
    print(f"║ 🎯 Avg. Attempts  │ {avg_attempts:^14.1f} ║")
    print("╚════════════════════════════════════╝")
    
    # Add performance rating based on win rate
    if games_played > 0:
        if win_rate >= 90:
            print("🌟 Master Detective Status 🌟")
        elif win_rate >= 70:
            print("💫 Senior Investigator Status 💫")
        elif win_rate >= 50:
            print("✨ Detective in Training ✨")
        else:
            print("🔍 Rookie Detective - Keep Practicing! 🔍")

def start_game() -> None:
    """
    Handles game loop and asks if player wants to play another round.
    Tracks and displays game statistics after each round.
    """
    global games_played, games_won, total_attempts
    
    while True:
        won, attempts_used = play_word_detective()
        games_played += 1
        if won:
            games_won += 1
        total_attempts += attempts_used
        
        display_statistics()
        
        answer = input("\nDo you want to play again? (j/ja/y/yes): ").lower().strip()
        if answer not in VALID_REPLAY_RESPONSES:
            print("\nCase closed! Thanks for being an amazing detective! 🔍")
            print("👋 Until our next investigation... 🕵️")
            break

def main() -> None:
    """ Main entry point of the game """
    try:
        clear_screen()
        display_game_rules()
        start_game()
    except KeyboardInterrupt:
        print("\nGame interrupted. Thanks for stepping by!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please try again.")

if __name__ == "__main__":
    main()