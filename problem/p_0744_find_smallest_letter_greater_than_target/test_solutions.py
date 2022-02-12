import pytest

from .solutions import Solution


@pytest.mark.parametrize("solution_cls", [Solution])
@pytest.mark.parametrize(
    "value, expected",
    (
        ((["c", "f", "j"], "a"), "c"),
        ((["c", "f", "j"], "c"), "f"),
        ((["c", "f", "j"], "d"), "f"),
    ),
)
def test_solutions(solution_cls, value, expected):
    solution = solution_cls()
    assert solution.nextGreatestLetter(*value) == expected
