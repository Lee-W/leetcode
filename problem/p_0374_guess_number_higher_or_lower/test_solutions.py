import pytest

from .solutions import Solution


@pytest.mark.parametrize("solution_cls", [Solution])
@pytest.mark.parametrize("value, expected", (((10, 6), 6), ((1, 1), 1)))
def test_solutions(solution_cls, value, expected):
    solution = solution_cls()
    assert solution.guessNumber(*value) == expected
