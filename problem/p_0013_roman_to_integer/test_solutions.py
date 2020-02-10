import pytest

from .solutions import Solution


@pytest.mark.parametrize(
    "test_input, expected",
    (
        ("III", 3),
        ("IV", 4),
        ("IX", 9),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("I", 1),
        ("MMMCMXCIX", 3999),
    ),
)
def test_solutions(test_input, expected):
    solution = Solution()
    assert solution.romanToInt(test_input) == expected
