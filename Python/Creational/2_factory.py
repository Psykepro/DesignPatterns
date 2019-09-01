# -*- coding: utf-8 -*-

"""
@Source: https://www.tutorialspoint.com

# - What is this pattern about? - #
 * When a Method returns one of several possible classes that share a common super
   class.
    ** Create a new enemy in a game.
    ** Random number generator picks a number assigned to a specific enemy.
    ** The factory returns the enemy associated with that number.
 * The class is chosen at run time.
 * A Factory is an object for creating other objects.
 * Creates objects without having to specify the exact class.

# - When to Use a Factory Pattern?
 * When you don't know ahead of time what class object you need
 * When all of the potential classes are in the same subclass hierarchy
 * To centralize class selection code
 * When you don't want the user to have to know every subclass
 * To encapsulate object creation
"""


class Button:
    html = ""

    def get_html(self):
        return self.html


class Image(Button):
    html = "<img></img>"


class Input(Button):
    html = "<input></input>"


class Flash(Button):
    html = "<obj></obj>"


class ButtonFactory:
    buttons = {'Image': Image, 'Input': Input, 'Flash': Flash}

    @classmethod
    def create_button(cls, btn_type):
        target_class = btn_type
        return cls.buttons[target_class]()


def main():
    button = ['Image', 'Input', 'Flash']
    for b in button:
        print(ButtonFactory.create_button(b).get_html())


if __name__ == '__main__':
    main()
