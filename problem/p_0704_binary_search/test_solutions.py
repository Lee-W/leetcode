import pytest

from .solutions import Solution


@pytest.mark.parametrize("solution_cls", [Solution])
@pytest.mark.parametrize(
    "value, expected", ((([-1, 0, 3, 5, 9, 12], 9), 4), (([-1, 0, 3, 5, 9, 12], 2), -1))
)
def test_solutions(solution_cls, value, expected):
    solution = solution_cls()
    assert solution.search(*value) == expected
