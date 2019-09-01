"""
# - What is this pattern about? - #
 * This pattern sends data to and object and if that object can't use it, it
   sends it to any number of other objects that may be able to use it
    ** Create 4 objects that can either add, subtract, multiply or divide
    ** Send 2 numbers and a commands and allow these 4 objects to decide which
       can handle the requested calculation.
 * Every piece of code must do one, and only one, thing.

# - When to use it? - #
 * When we don't want to have hardcoded switch statement and we want to replace
   it with the wield of the power of Polymorphism.
 * Use the Chain of Responsibility pattern when you can conceptualize your
   program as a chain made up of links, where each link can either handle a
   request or pass it up the chain.

"""

# This object will contain 2 numbers and a
# calculation to perform in the form of a String
from abc import ABC


class Numbers:
    def __init__(self, first_number: int, second_number: int, calc_wanted: str):
        self.first_number = first_number
        self.second_number = second_number
        self.calc_wanted = calc_wanted


# The chain of responsibility pattern has a
# group of objects that are expected to between
# them be able to solve a problem.
# If the first Object can't solve it, it passes
# the data to the next Object in the chain
class Chain(ABC):
    """Defines the next Object to receive the data if this object can't
       process it"""
    def __init__(self):
        self.next_in_chain = None

    def set_next_chain(self, next_chain: "Chain"):
        raise NotImplementedError

    def calculate(self, request: Numbers):
        raise NotImplementedError


class AddNumbersChain(Chain):
    """Defines the next Object to receive the data data if this one can't use
       it"""

    def set_next_chain(self, next_chain: Chain):
        self.next_in_chain = next_chain

    def calculate(self, request: Numbers):
        if request.calc_wanted == 'add':
            result = request.first_number + request.second_number
            print(f'{request.first_number} + {request.second_number} = '
                  f'{result}')
        else:
            self.next_in_chain.calculate(request)


class SubtractNumbersChain(Chain):
    """Defines the next Object to receive the data data if this one can't use
       it"""

    def set_next_chain(self, next_chain: Chain):
        self.next_in_chain = next_chain

    def calculate(self, request: Numbers):
        if request.calc_wanted == 'sub':
            result = request.first_number - request.second_number
            print(f'{request.first_number} - {request.second_number} = '
                  f'{result}')
        else:
            self.next_in_chain.calculate(request)


class MultiplyNumbersChain(Chain):
    """Defines the next Object to receive the data data if this one can't use
       it"""

    def set_next_chain(self, next_chain: Chain):
        self.next_in_chain = next_chain

    def calculate(self, request: Numbers):
        if request.calc_wanted == 'mul':
            result = request.first_number * request.second_number
            print(
                f'{request.first_number} * {request.second_number} = '
                f'{result}')
        else:
            self.next_in_chain.calculate(request)


class DivideNumbersChain(Chain):
    """Defines the next Object to receive the data data if this one can't use
       it"""

    def set_next_chain(self, next_chain: Chain):
        self.next_in_chain = next_chain

    def calculate(self, request: Numbers):
        if request.calc_wanted == 'div':
            result = request.first_number / request.second_number
            print(
                f'{request.first_number} / {request.second_number} = '
                f'{result}')
        else:
            self.next_in_chain.calculate(request)


def main():
    # Defining all of the objects in the chain
    chain_calc_1 = AddNumbersChain()
    chain_calc_2 = SubtractNumbersChain()
    chain_calc_3 = MultiplyNumbersChain()
    chain_calc_4 = DivideNumbersChain()

    # Here we tell each object where to forward the data, if can't process the
    # request
    chain_calc_1.set_next_chain(chain_calc_2)
    chain_calc_2.set_next_chain(chain_calc_3)
    chain_calc_3.set_next_chain(chain_calc_4)

    # Define the data in the Numbers object and send it to the first object in
    # the chain
    numbers = Numbers(4, 2, "add")
    chain_calc_1.calculate(numbers)


if __name__ == '__main__':
    main()
