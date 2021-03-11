import pytest

from .solutions import Solution


@pytest.mark.parametrize("A", ([3, 1, 2, 4],))
def test_solutions(A):
    solution = Solution()
    solution.sortArrayByParity(A)
