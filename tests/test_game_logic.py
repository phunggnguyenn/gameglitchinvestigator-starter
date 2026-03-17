from logic_utils import check_guess, compute_attempts_left


def test_attempts_left_is_zero_on_final_guess():
    """
    On the last allowed guess, attempts_left should display 0, not 1.

    Bug: the display was computed using attempts BEFORE the submit increment,
    so on the final guess the counter read 1 instead of 0.

    Fix: compute_attempts_left accounts for the pending increment via
    submit_in_progress=True.
    """
    attempt_limit = 8  # Normal difficulty
    attempts_before_submit = attempt_limit - 1  # 7

    # Without submit in progress (old buggy behavior): shows 1
    assert compute_attempts_left(attempt_limit, attempts_before_submit, False) == 1

    # With submit in progress (fixed behavior): shows 0
    assert compute_attempts_left(attempt_limit, attempts_before_submit, True) == 0


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"
