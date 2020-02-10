import pytest

from .solutions import Solution, Solution2


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("", True),
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("(((", False),
        ("(", False),
        ("]", False),
        ("{[}]", False),
    ],
)
def test_solutions(test_input, expected):
    solution = Solution()
    assert solution.isValid(test_input) == expected

    solution2 = Solution2()
    assert solution2.isValid(test_input) == expected
