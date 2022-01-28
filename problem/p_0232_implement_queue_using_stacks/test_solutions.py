import pytest

from .solutions import MyQueue


@pytest.mark.parametrize("solution_cls", [MyQueue])
@pytest.mark.parametrize(
    "commands, args, expected",
    (
        (
            ["MyQueue", "push", "push", "peek", "pop", "empty"],
            [[], [1], [2], [], [], []],
            [None, None, None, 1, 1, False],
        ),
    ),
)
def test_solutions(solution_cls, commands, args, expected):
    queue = MyQueue()
    for cmd, arg, val in zip(commands[1:], args[1:], expected[1:]):
        assert getattr(queue, cmd)(*arg) == val
