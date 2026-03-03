from solutions.task4_isSubsequence import isSubsequence
import pytest

@pytest.mark.parametrize(
    "string_a, string_b, res",
    [
        ("", "abcd", True),
        ("abc", "alkjbldkdclkd", True),
        ("aaa", "abcabccc", False),
        ("abc", "lllabddc", True),
        ("a", "", False),
        ("aaa", "aa", False)
    ],
)

def test_subsequences(string_a, string_b, res):
    assert isSubsequence(string_a, string_b) == res