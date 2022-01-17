import pytest
import string

from hypothesis import given
from hypothesis.strategies import text

from copy import deepcopy
from .solutions import Solution, Solution2


@pytest.mark.parametrize("solution_cls", [Solution, Solution2])
@given(text(alphabet=string.ascii_letters))
def test_solutions(solution_cls, input_str):
    print(solution_cls)
    value = list(input_str)
    original_value = deepcopy(value)

    solution = solution_cls()
    solution.reverseString(value)
    assert value == original_value[-1::-1]
