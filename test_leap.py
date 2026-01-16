from leap import is_leap

def test_is_leap():
    assert is_leap(2024) == True
def test_not_leap():
    assert is_leap(2023) == False
def test_2000():
    assert is_leap(2000) == True
