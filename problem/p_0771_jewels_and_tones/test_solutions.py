import pytest

from .solutions import Solution, Solution2


@pytest.mark.parametrize(
    "test_input,expected", [(("aA", "aAAbbbb"), 3), (("z", "ZZ"), 0)]
)
def test_solution(test_input, expected):
    solution = Solution()
    assert solution.numJewelsInStones(*test_input) == expected

    solution = Solution2()
    assert solution.numJewelsInStones(*test_input) == expected
