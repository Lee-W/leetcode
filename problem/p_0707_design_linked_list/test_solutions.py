import pytest

from .solutions import MyLinkedList


@pytest.mark.parametrize("solution_cls", [MyLinkedList])
@pytest.mark.parametrize(
    "commands, args, expected",
    (
        (
            [
                "MyLinkedList",
                "addAtHead",
                "addAtTail",
                "addAtIndex",
                "get",
                "deleteAtIndex",
                "get",
            ],
            [[], [1], [3], [1, 2], [1], [1], [1]],
            [None, None, None, None, 2, None, 3],
        ),
    ),
)
def test_solutions(solution_cls, commands, args, expected):

    linked_list = solution_cls()
    for cmd, arg, val in zip(commands[1:], args[1:], expected[1:]):
        assert getattr(linked_list, cmd)(*arg) == val
