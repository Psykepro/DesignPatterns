# -*- coding: utf-8 -*-

"""
@Source: https://www.tutorialspoint.com

# - What is this pattern about? - #
A Factory is an object for creating other objects.
Creates objects without having to specify the exact class.
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
