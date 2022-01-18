import pytest

from .solutions import Solution


@pytest.mark.parametrize("solution_cls", [Solution])
@pytest.mark.parametrize("value, expected",)
def test_solutions(solution_cls, value, expected):
    solution = solution_cls()
    assert solution.func(value) == expected
