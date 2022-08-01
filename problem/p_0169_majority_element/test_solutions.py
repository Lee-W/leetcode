import pytest

from .solutions import Solution


@pytest.mark.parametrize("solution_cls", [Solution])
@pytest.mark.parametrize("value, expected", (([3, 2, 3], 3), ([2, 2, 2, 1, 2], 2)))
def test_solutions(solution_cls, value, expected):
    solution = solution_cls()
    assert solution.majorityElement(value) == expected
