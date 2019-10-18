from dll_queue import QueueLambda
from dll_stack import StackLambda

# class BstNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if not isinstance(value, BstNode):
        #     value = BstNode(value)

        if self.value is None:
            self.value = value
        else:
            if value > self.value:
                if self.right is None:
                    self.right = BinarySearchTree(value)
                else:
                    self.right.insert(value)
            else:
                if self.left is None:
                    self.left = BinarySearchTree(value)
                else:
                    self.left.insert(value)


        return

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        else:
            if target > self.value:
                if self.right is None:
                    return False
                elif self.right.value == target:
                    return True
                elif self.right is not None:
                    self.right.contains(target)

            else:
                if self.left is None:
                    return False
                elif self.left.value == target:
                    return True
                elif self.left is not None:
                    self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.right is not None:
            self.right.for_each(cb)
        if self.left is not None:
            self.left.for_each(cb)
        return

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
