import pytest

from .solutions import MinStack


@pytest.mark.parametrize("solution_cls", [MinStack])
@pytest.mark.parametrize(
    "commands, args, expected",
    (
        (
            ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
            [[], [-2], [0], [-3], [], [], [], []],
            [None, None, None, None, -3, None, 0, -2],
        ),
    ),
)
def test_solutions(solution_cls, commands, args, expected):

    linked_list = solution_cls()
    for cmd, arg, val in zip(commands[1:], args[1:], expected[1:]):
        assert getattr(linked_list, cmd)(*arg) == val
