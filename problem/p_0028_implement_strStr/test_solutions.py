import pytest

from .solutions import Solution, Solution2


@pytest.mark.parametrize(
    "test_haystack, test_needle, expected",
    (
        ("hello", "ll", 2),
        ("aaaaa", "bba", -1),
        ("abcde", "", 0),
        ("aaa", "aaaa", -1),
        ("mississippi", "issip", 4),
        ("a", "a", 0),
        ("aa", "aa", 0),
        ("mississippi", "pi", 9)
    )
)
def test_solution(test_haystack, test_needle, expected):
    solution = Solution()
    assert solution.strStr(test_haystack, test_needle) == expected

    solution2 = Solution2()
    assert solution2.strStr(test_haystack, test_needle) == expected
