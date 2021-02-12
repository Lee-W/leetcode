import pytest

from .solutions import Solution


@pytest.mark.parametrize(
    "nums1, m, nums2, n, output",
    (
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1]),
        ([1], 1, [], 0, [1]),
        ([4, 0, 0, 0, 0, 0], 1, [1, 2, 3, 5, 6], 5, [1, 2, 3, 4, 5, 6]),
    ),
)
def test_solution(nums1, m, nums2, n, output):
    solution = Solution()
    solution.merge(nums1, m, nums2, n)

    assert nums1 == output
