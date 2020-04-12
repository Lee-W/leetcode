import string

from hypothesis import given
from hypothesis.strategies import text

from .solutions import Solution


@given(text(alphabet=string.ascii_letters))
def test_solutions(input_str):
    solution = Solution()
    assert solution.toLowerCase(input_str) == input_str.lower()
