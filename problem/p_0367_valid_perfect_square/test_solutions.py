from hypothesis import given
from hypothesis.strategies import integers

from .solutions import Solution


# @pytest.mark.parametrize("solution_cls", [Solution])
@given(integers(1, 2 ** 31))
def test_solutions(value):
    solution = Solution()
    assert solution.isPerfectSquare(value) == (value ** (1 / 2)).is_integer()
