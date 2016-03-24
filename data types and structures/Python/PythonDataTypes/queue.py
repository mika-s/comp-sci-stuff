# -*- coding: utf-8 -*-
"""Implementation of a queue."""


class Queue():
    """Representation of a queue as a list.
    
    Lists are inefficient for queues.
    """

    def __init__(self, initial_queue):
        """Constructor."""

        self.queue = initial_queue[:]

    def __str__(self):
        """Redefining this method so print(queue) shows usable info."""

        return "{}".format(self.queue)

    def add(self, new_element):
        """Remove the first element and add a new one."""

        self.queue.insert(0, new_element)
        self.queue.pop()


def main():
    """The main function. Used to test the other functions."""

    # Create the initial queue.
    my_queue = Queue([1, 5, 0, 3])
    print(my_queue)

    # Enqueue/dequeue one element.
    my_queue.add(7)
    print(my_queue)

    # Enqueue/dequeue two elements.
    my_queue.add(10)
    my_queue.add(4)
    print(my_queue)


if __name__ == "__main__":
    main()
