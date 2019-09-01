"""
@Source: https://www.tutorialspoint.com

# - What is this pattern about? - #
 * This pattern restricts the instantiation of a class to one object.
 * It is a type of creational pattern and involves only one class to create
   methods and specified objects.
 * It provides a global point of access to the instance created.
"""


class Singleton:
    __instance = None

    def __init__(self):
        """ Virtually private constructor. """
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self

    @staticmethod
    def get_instance():
        """ Static access method. """
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance


def main():
    s = Singleton()
    print(s)
    s = s.get_instance()
    print(s)
    s = s.get_instance()
    print(s)


if __name__ == '__main__':
    main()
