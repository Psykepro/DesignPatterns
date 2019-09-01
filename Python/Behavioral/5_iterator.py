"""
# - What is this pattern about? - #
 * The Iterator Design Pattern enables the client to sequentially access
   elements of a composite object, without exposing its internal
   representation. In Python, the Iterator Pattern consists of providing the
   client with either:
    ** a method which can traverse a given object
    ** a class whose object can traverse a given object.

# - When it is useful? - #
 * The Iterator Pattern is implemented to provide the client with a function
   or a class whose instance performs tasks of an iterator.
"""
NUMBERS_IN_ENGLISH = ['one', 'two', 'three', 'four', 'five', 'six',  'seven',
                      'eight', 'nine']


# - Iterator Function (Generator) - #
def count_to(upper_bound):
    # (1, 'one')(2, 'two')(3, 'three')etc.
    custom_iterator = zip(range(1, upper_bound + 1), NUMBERS_IN_ENGLISH)
    for numeric_form, english_form in custom_iterator:
        yield english_form


# - Iterator Class - #
class CountTo:
    def __init__(self, upper_bound):
        self.upper_bound = upper_bound
        self.numbers_in_english = NUMBERS_IN_ENGLISH[:upper_bound]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.numbers_in_english):
            raise StopIteration
        result = self.numbers_in_english[self.index]
        self.index += 1
        return result


def main():
    # - Test Iterator Function - #
    count_to_3_iterator = count_to(3)
    for num_in_english_form in count_to_3_iterator:
        print(num_in_english_form)

    # - Test Iterator Class - #
    count_to_3_iterator = CountTo(3)
    for num_in_english_form in count_to_3_iterator:
        print(num_in_english_form)


if __name__ == "__main__":
    main()