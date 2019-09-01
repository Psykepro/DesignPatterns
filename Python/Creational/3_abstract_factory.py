"""
@Source: https://sourcemaking.com

# - What is this pattern about? - #
 * It is like a factory, but everything is encapsulated.
    ** The method that orders the objects.
    ** The factories that build the object
    ** The final objects
    ** The final objects contain objects that use the Strategy Pattern
        *** Composition: Object class fields are other objects
 * Provide an interface for creating families of related or dependent
 * objects without specifying their concrete classes.

# - What you can do with an Abstract Factory - #
 * Allows you to create families of related objects without specifying a
   concrete class.
 * Use when you have many objects that can be added, or changed dynamically
   during runtime.
 * You can model anything you can imagine and have those objects interact
   through common interfaces.
 * The Bad Thing is thar can get very complicated.
"""

import abc


class AbstractFactory(metaclass=abc.ABCMeta):
    """
    Declare an interface for operations that create abstract product
    objects.
    """

    @abc.abstractmethod
    def create_product_a(self):
        pass

    @abc.abstractmethod
    def create_product_b(self):
        pass


class ConcreteFactory1(AbstractFactory):
    """
    Implement the operations to create concrete product objects.
    """

    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    """
    Implement the operations to create concrete product objects.
    """

    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()


class AbstractProductA(metaclass=abc.ABCMeta):
    """
    Declare an interface for a type of product object.
    """

    @abc.abstractmethod
    def interface_a(self):
        pass


class ConcreteProductA1(AbstractProductA):
    """
    Define a product object to be created by the corresponding concrete
    factory.
    Implement the AbstractProduct interface.
    """

    def interface_a(self):
        pass


class ConcreteProductA2(AbstractProductA):
    """
    Define a product object to be created by the corresponding concrete
    factory.
    Implement the AbstractProduct interface.
    """

    def interface_a(self):
        pass


class AbstractProductB(metaclass=abc.ABCMeta):
    """
    Declare an interface for a type of product object.
    """

    @abc.abstractmethod
    def interface_b(self):
        pass


class ConcreteProductB1(AbstractProductB):
    """
    Define a product object to be created by the corresponding concrete
    factory.
    Implement the AbstractProduct interface.
    """

    def interface_b(self):
        pass


class ConcreteProductB2(AbstractProductB):
    """
    Define a product object to be created by the corresponding concrete
    factory.
    Implement the AbstractProduct interface.
    """

    def interface_b(self):
        pass


def main():
    for factory in (ConcreteFactory1(), ConcreteFactory2()):
        product_a = factory.create_product_a()
        product_b = factory.create_product_b()
        product_a.interface_a()
        product_b.interface_b()


if __name__ == "__main__":
    main()