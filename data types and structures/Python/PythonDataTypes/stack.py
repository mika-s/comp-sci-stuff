# -*- coding: utf-8 -*-
"""Implementation of a stack."""


class Stack():
    """Representation of a LIFO stack as a list."""

    def __init__(self):
        """Constructor."""

        self.stack_list = []

    def __str__(self):
        """Redefining this method so print(stack) shows usable info."""

        return "{}".format(self.stack_list)

    def push(self, variable):
        """Push to the stack."""

        self.stack_list.append(variable)

    def pop(self):
        """Pop from the stack."""

        popped_item = self.stack_list.pop()

        return popped_item


def main():
    """The main function. Used to test the other functions."""

    # Make the stack.
    my_stack = Stack()

    # Add some item(s) and print the content of the stack.
    my_stack.push(3)
    my_stack.push(7)
    my_stack.push(10)
    print(my_stack)

    # Remove some item(s) and print the content of the stack.
    my_stack.pop()
    my_stack.pop()
    print(my_stack)


if __name__ == "__main__":
    main()
