from leap import is_leap

def test_is_leap():
    assert is_leap(2024) == True      # Leap year
    assert is_leap(2023) == False     # Not a leap year
    assert is_leap(2000) == True      # Leap year
