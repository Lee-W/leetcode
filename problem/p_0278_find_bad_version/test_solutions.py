import pytest

from .solutions import Solution


@pytest.mark.parametrize("solution_cls", [Solution])
@pytest.mark.parametrize("value, expected", (((5, 4), 4), ((1, 1), 1)))
def test_solutions(solution_cls, value, expected):
    solution = solution_cls()
    assert solution.firstBadVersion(*value) == expected
