import pytest

from .solutions import Solution


@pytest.mark.parametrize("solution_cls", [Solution])
@pytest.mark.parametrize("value, expected", ((4, 2), (8, 2)))
def test_solutions(solution_cls, value, expected):
    solution = solution_cls()
    assert solution.mySqrt(value) == expected
