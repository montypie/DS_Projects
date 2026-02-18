# tests for word_detective.py

from word_detective import (
    validate_input, 
    get_feedback, 
    FEEDBACK_CORRECT,
    FEEDBACK_WRONG_POSITION,
    FEEDBACK_INCORRECT
)

def test_validate_input():
    """Test input validation with various test cases."""
    test_cases = [
        ("APPEL", True, ""),            # valid input
        ("App", False, "Guess must be exactly 5 letters long."),  # too short
        ("APPELS", False, "Guess must be exactly 5 letters long."),  # too long
        ("APP3L", False, "Guess must contain only letters."),  # contains digit
        ("", False, "Input cannot be empty."),  # empty string
        ("AP EL", False, "Guess must contain only letters."),  # contains space
        ("APPEl", True, ""),  # mixed case (should be valid)
        ("@PPEL", False, "Guess must contain only letters."),  # special character
    ]
    
    for input_word, expected_valid, expected_message in test_cases:
        is_valid, message = validate_input(input_word)
        assert is_valid == expected_valid, f"Failed for input '{input_word}'"
        if not is_valid:
            assert message == expected_message, f"Wrong error message for '{input_word}'"

def test_exact_match():
    """Test feedback when guess exactly matches the secret word."""
    secret = "APPEL"
    guess = "APPEL"
    expected = [FEEDBACK_CORRECT] * 5
    assert get_feedback(secret, guess) == expected

def test_duplicate_letters():
    """Test handling of duplicate letters in both secret and guess."""
    test_cases = [
        # secret word has doubles (APPEL), guess has one (PANIC)
        ("APPEL", "PANIC", [FEEDBACK_WRONG_POSITION, FEEDBACK_WRONG_POSITION, FEEDBACK_INCORRECT, FEEDBACK_INCORRECT, FEEDBACK_INCORRECT]),
        # guess has doubles (APPEL), secret has one (PLANT)
        ("PLANT", "APPEL", [FEEDBACK_WRONG_POSITION, FEEDBACK_WRONG_POSITION, FEEDBACK_INCORRECT, FEEDBACK_INCORRECT, FEEDBACK_WRONG_POSITION]),
        # both have doubles (APPEL, PEPER)
        ("APPEL", "PEPER", [FEEDBACK_WRONG_POSITION, FEEDBACK_INCORRECT, FEEDBACK_CORRECT, FEEDBACK_CORRECT, FEEDBACK_INCORRECT])
    ]
    
    for secret, guess, expected in test_cases:
        result = get_feedback(secret, guess)
        assert result == expected, f"Failed for secret='{secret}', guess='{guess}'"

def test_no_matches():
    """Test feedback when no letters match."""
    secret = "HOUSE"
    guess = "CRIMP"
    expected = [FEEDBACK_INCORRECT] * 5
    assert get_feedback(secret, guess) == expected

def test_mixed_feedback():
    """Test combinations of correct, wrong position, and incorrect feedback."""
    test_cases = [
        # Test case with all three types of feedback
        ("APPEL", "MAPLE", [FEEDBACK_INCORRECT, FEEDBACK_WRONG_POSITION, FEEDBACK_CORRECT, FEEDBACK_WRONG_POSITION, FEEDBACK_WRONG_POSITION]),
        # Test case with only correct and incorrect
        ("APPEL", "AXXXX", [FEEDBACK_CORRECT, FEEDBACK_INCORRECT, FEEDBACK_INCORRECT, FEEDBACK_INCORRECT, FEEDBACK_INCORRECT]),
        # Test case with only wrong position and incorrect
        ("APPEL", "STAMP", [FEEDBACK_INCORRECT, FEEDBACK_INCORRECT, FEEDBACK_WRONG_POSITION, FEEDBACK_INCORRECT, FEEDBACK_WRONG_POSITION])
    ]
    
    for secret, guess, expected in test_cases:
        result = get_feedback(secret, guess)
        assert result == expected, f"Failed for secret='{secret}', guess='{guess}'"

def test_error_handling():
    """Test error handling for invalid inputs to get_feedback."""
    try:
        get_feedback("APPEL", "KORT")  # different lengths
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert str(e) == "Secret word and guess must be the same length"