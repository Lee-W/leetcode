import pytest

from .solutions import Solution, Solution2, Solution3


@pytest.mark.parametrize("solution_cls", [Solution, Solution2, Solution3])
@pytest.mark.parametrize(
    "value, expected",
    (
        (
            ([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2),
            [[2, 2, 2], [2, 2, 0], [2, 0, 1]],
        ),
        (([[0, 0, 0], [0, 0, 0]], 0, 0, 2), [[2, 2, 2], [2, 2, 2]]),
        (
            ([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2),
            [[2, 2, 2], [2, 2, 0], [2, 0, 1]],
        ),
    ),
)
def test_solutions(solution_cls, value, expected):
    solution = solution_cls()
    assert solution.floodFill(*value) == expected
