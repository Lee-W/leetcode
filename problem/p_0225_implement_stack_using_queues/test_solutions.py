import pytest

from .solutions import MyStack


@pytest.mark.parametrize("solution_cls", [MyStack])
@pytest.mark.parametrize(
    "commands, args, expected",
    (
        (
            ["MyStack", "push", "push", "top", "pop", "empty"],
            [[], [1], [2], [], [], []],
            [None, None, None, 2, 2, False],
        ),
    ),
)
def test_solutions(solution_cls, commands, args, expected):
    stack = MyStack()
    for cmd, arg, val in zip(commands[1:], args[1:], expected[1:]):
        assert getattr(stack, cmd)(*arg) == val
