# -*- coding: utf-8 -*-
"""Implementation of a tree."""

from sys import exit


class TreeNode:
    """Representation of a node in a tree."""

    def __init__(self, data=None, children=None):
        """Constructor for TreeNode.

        Args:
            data        --    the data the node contains
            children    --    the child nodes
        """

        self.data = data
        self.children = children


class Tree():
    """Methods related to trees."""

    @staticmethod
    def walk(root_node):
        """Walk the tree and print to the screen."""

        print(root_node.data)
        if root_node.children is not None:
            for child_node in root_node.children:
                Tree.walk(child_node)

    @staticmethod
    def plot(root_node):
        """Create a dot file for graphviz."""

        try:
            file_ = open("treeplot.gv", "w")
        except:
            print("Could not open the file for writing.\n")
            exit(2)

        file_.write("digraph G {\n")
        Tree.plot_walk(file_, root_node)
        file_.write("}\n")
        file_.close()

    @staticmethod
    def plot_walk(file_, root_node):
        """Walk the tree and write to the file."""

        file_.write("{}".format(root_node.data))
        file_.write("->")
        if root_node.children is not None:
            for child_node in root_node.children:
                # Work in progress.
                Tree.plot_walk(file_, child_node)


def main():
    """The main function. Used to test the other functions."""

    # Create the nodes.
    nodeR = TreeNode("Root")
    nodeA1 = TreeNode("A1")
    nodeA2 = TreeNode("A2")
    nodeB1 = TreeNode("B1")
    nodeB2 = TreeNode("B2")

    nodeR.children = [nodeA1, nodeB1]
    nodeA1.children = [nodeA2]
    nodeB1.children = [nodeB2]

    # Walk the tree.
    Tree.walk(nodeR)

    # Plot the tree.
    Tree.plot(nodeR)


if __name__ == "__main__":
    main()
