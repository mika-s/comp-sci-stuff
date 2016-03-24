# -*- coding: utf-8 -*-
"""Implementation of linked lists."""


class SllNode:
    """Representation of a node in a single linked list."""

    def __init__(self, data=None, next=None):
        """Constructor for SllNode.

        Args:
            data    --    the data the node contains
            next    --    the next node
        """

        self.data = data
        self.next = next


class SingleLinkedList:
    """Methods related to single linked lists."""

    @staticmethod
    def traverse(action, node):
        """Traverse the single linked list and do action.

        Args:
            action    --    action to perform
            node      --    head node in the sll
        """

        if action == "sum":
            sum_ = 0

            while node:
                sum_ += node.data
                node = node.next

            return sum_
        elif action == "print":
            while node:
                print(node.data)
                node = node.next
        elif action == "print backwards":
            SingleLinkedList.print_backwards(node)
        else:
            print("Unknown action.")

    @staticmethod
    def print_backwards(node):
        """Print a single linked list backwards."""

        if node == None:
            return

        head = node
        tail = node.next
        SingleLinkedList.print_backwards(tail)
        print(head.data)


def main():
    """The main function. Used to test the other functions."""

    int_node1 = SllNode(10)
    int_node2 = SllNode(30)
    int_node3 = SllNode(50)
    int_node4 = SllNode(90)

    int_node1.next = int_node2
    int_node2.next = int_node3
    int_node3.next = int_node4

    # The sum should be 100+50+30+10 = 180.
    sum_ = SingleLinkedList.traverse("sum", int_node1)
    print(sum_)

    str_node1 = SllNode("A")
    str_node2 = SllNode("B")
    str_node3 = SllNode("D")
    str_node4 = SllNode("C")

    str_node1.next = str_node2
    str_node2.next = str_node3
    str_node3.next = str_node4

    SingleLinkedList.traverse("print", str_node1)
    SingleLinkedList.traverse("print", str_node3)
    SingleLinkedList.traverse("print backwards", str_node1)


if __name__ == "__main__":
    main()
