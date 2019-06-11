import pytest

from solutions import Solution


@pytest.mark.parametrize(
    "test_s, expected",
    (
        ("", 0),
        (" ", 0),
        ("Hello World", 5),
        ("Hello", 5),
        ("a ", 1),
        (" a", 1)
    )
)
def test_solutions(test_s, expected):
    solution = Solution()
    assert solution.lengthOfLastWord(test_s) == expected

