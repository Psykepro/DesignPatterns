"""
# - What is this pattern about? - #
 * The command pattern is handy in situations when, for some reason, we need to
   start by preparing what will be executed and then to execute it when needed.

# - Advantages of Command Pattern - #
 * The advantage is that encapsulating actions in such a way enables Python
   developers to add additional functionalities related to the executed actions,
   such as undo/redo, or keeping a history of actions and the like.
"""

from .. import utilities
import os
import typing


class Command:

    def execute(self):
        raise NotImplementedError

    def undo(self):
        raise NotImplementedError


class RenameFileCommand(Command):
    def __init__(self, path, from_name, to_name):
        self._path = path
        self._from = from_name
        self._to = to_name
        self._path_from = os.path.join(self._path, self._from)
        self._path_to = os.path.join(self._path, self._to)

    def execute(self):
        os.rename(self._path_from, self._path_to)

    def undo(self):
        os.rename(self._path_to, self._path_from)


class History:
    def __init__(self):
        self._commands = typing.List[Command]

    def execute(self, command: Command):
        self._commands.append(command)
        command.execute()

    def undo(self):
        self._commands.pop().undo()


def main():
    path = 'test/'
    first_from, first_to = 'cv.doc', 'cv-en.doc'
    second_from, second_to = 'cv1.doc', 'cv-bg.doc'
    utilities.touch(os.path.join(path, first_from))
    utilities.touch(os.path.join(path, second_from))

    history = History()
    history.execute(RenameFileCommand(path, first_from, first_to))
    history.execute(RenameFileCommand(path, second_from, second_to))
    history.undo()
    history.undo()


if __name__ == '__main__':
    main()
