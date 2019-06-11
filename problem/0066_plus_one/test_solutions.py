import pytest

from solutions import Solution


@pytest.mark.parametrize(
    "test_digits, expected",
    (
        ([1, 2, 3], [1, 2, 4]),
        ([4, 3, 2, 1], [4, 3, 2, 2]),
        ([0], [1]),
        ([9], [1, 0])
    )
)
def test_solutions(test_digits, expected):
    solution = Solution()
    assert solution.plusOne(test_digits) == expected
