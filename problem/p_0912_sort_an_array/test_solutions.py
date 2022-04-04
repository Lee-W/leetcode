import pytest
from hypothesis import given
from hypothesis.strategies import integers, lists

from .solutions import Solution, Solution2

BOUNDARY = 5 * 10 ** 4


@pytest.mark.parametrize("solution_cls", [Solution, Solution2])
@given(lists(integers(-BOUNDARY, BOUNDARY), max_size=BOUNDARY))
def test_solutions(solution_cls, value):
    solution = solution_cls()
    assert solution.sortArray(value) == sorted(value)
