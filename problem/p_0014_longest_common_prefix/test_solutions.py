import pytest

from .solutions import Solution


@pytest.mark.parametrize(
    "test_input, expected",
    (
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], "")
    )
)
def test_solutions(test_input, expected):
    solution = Solution()
    assert solution.longestCommonPrefix(test_input) == expected
