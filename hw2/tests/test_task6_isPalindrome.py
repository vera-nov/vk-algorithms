from solutions.task6_isPalindrome import isPalindrome
import pytest

@pytest.mark.parametrize(
    "s, res",
    [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("", True),
        ("12321", True),
        ("1231", False),
        ("1a2", False),
        ("1a1", True),
        ("abccba" * 1000, True),
    ],
)

def test_isPalindrome(s, res):
    assert isPalindrome(s) == res