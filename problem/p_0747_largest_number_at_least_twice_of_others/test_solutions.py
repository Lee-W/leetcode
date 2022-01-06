import pytest

from .solutions import Solution, Solution2


@pytest.mark.parametrize(
    "value, expected",
    (
        ([3, 6, 1, 0], 1),
        ([1, 2, 3, 4], -1),
        ([1], 0),
        ([51, 100], -1),
        ([4, 3, 2, 1], -1),
        ([0, 0, 3, 2], -1),
        ([1, 2, 16, 35, 44, 100, 27, 0], 5),
    ),
)
def test_solutions(value, expected):
    solution = Solution()
    assert solution.dominantIndex(value) == expected

    solution = Solution2()
    assert solution.dominantIndex(value) == expected
