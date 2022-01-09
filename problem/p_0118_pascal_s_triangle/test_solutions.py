import pytest

from .solutions import Solution


@pytest.mark.parametrize(
    "value, expected",
    (
        (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
        (1, [[1]]),
        (
            6,
            [
                [1],
                [1, 1],
                [1, 2, 1],
                [1, 3, 3, 1],
                [1, 4, 6, 4, 1],
                [1, 5, 10, 10, 5, 1],
            ],
        ),
    ),
)
def test_solutions(value, expected):
    solution = Solution()
    assert solution.generate(value) == expected
