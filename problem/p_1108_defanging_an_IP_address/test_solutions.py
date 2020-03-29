import pytest

from .solutions import Solution


@pytest.mark.parametrize(
    "input_data, expected_output",
    (("1.1.1.1", "1[.]1[.]1[.]1"), ("255.100.50.0", "255[.]100[.]50[.]0")),
)
def test_solutions(input_data, expected_output):
    solution = Solution()
    assert solution.defangIPaddr(input_data) == expected_output
