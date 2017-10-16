from linked_binary_tree import LinkedBinaryTree
from linked_queue import Empty
class ExtendedBinaryTree(LinkedBinaryTree):
    def __init__(self):
        super().__init__()

    def preorder_next(self, p):
        '''Return the position visited after p in a preorder traversal of T (or None if p is the
        last node visited)
        '''
        if self.is_empty():  # Raise exception if the tree is empty.
            raise Empty("Tree is empty")
        current_node = p  # Otherwise, set the given position to current_node.
        if self.left(current_node) is not None:  # If the current_node has a left child, return it.
            return self.left(current_node)
        elif self.right(current_node) is not None:  # If the current_node has a right child, return it.
            return self.right(current_node)
        else:
            parent_node = self.parent(current_node)  # Set parent_node to the parent of the current node.
            if self.left(parent_node) == current_node and self.sibling(
                    current_node):  # If the current_node is a left child and has a sibling, return its sibling.
                return self.right(parent_node)
            elif self.num_children(current_node) == 0 and self.right(parent_node) == current_node or self.left(
                    parent_node) == current_node:  # Else if the current node is right child (leaf) of the parent node, or a left child
                if parent_node == self.right(
                        self.parent(parent_node)):  # If the parent_node is the right child of its parent
                    parent_node = self.parent(parent_node)  # Set the parent_node to parent_node's parent.
                    if self.parent(parent_node) == None:  # Return 'None' if it's the alst node visited.
                        return None
                return self.right(self.parent(parent_node))  # Return the right child of parent_node's parent.

    def inorder_next(self, p):
        '''Return the position visited after p in an inorder traversal of T (or None if p is the
        last node visited).
        '''
        if self.is_empty():  # Check if the tree is empty.
            raise Empty("Tree is empty")
        else:
            current_node = p  # If the tree isn't empty, set current_node to p, and current_node's right child to right.
            right = self.right(current_node)
            if (right != None) and self.num_children(
                    right) == 0:  # If the right child exists, and has no children, return it.
                return right
            elif right and self.left(
                    right):  # If the right child exists, and has a left child, set the current_node to the right child.
                current_node = right
                while self.left(
                        current_node):  # As long as the current_node has a left child, set the current node to it's left child.
                    current_node = self.left(current_node)
                return current_node  # If current_node does not have a left child, return it.
            elif (self.left(current_node) == None and right == None) or (self.left(
                    current_node) and right == None):  # If the current node has no children, or only has a left child, set the current node to it's parent.
                current_node = self.parent(current_node)
                if self.left(current_node) == p:  # If the left child of the current node is P, return it.
                    return current_node
                else:
                    while current_node == self.right(
                            self.parent(current_node)):  # Otherwise, look for it's parent, and return it.
                        current_node = self.parent(current_node)
                        if self.parent(current_node) == None:  # Return None if it's the last node visited.
                            return None
                    return self.parent(current_node)

    def postorder_next(self, p):
        '''Return the position visited after p in a postorder traversal of T (or None if p is
        the last node visited)
        '''
        if self.is_empty():  # Check if the tree is empty. If it is, raise an exception.
            raise Empty("Tree is empty!")
        else:
            current_node = p  # Otherwise set the current_node to p.
            if self.is_root(current_node):  # If the current_node is the root (last node visited), return 'None'.
                return None
            if self.sibling(current_node) is None:  # If the current_node has no sibling, return its parent.
                return self.parent(current_node)
            elif self.sibling(
                    current_node):  # Otherwise, if it has a sibling, set parent_node to the parent of current_node.
                parent_node = self.parent(current_node)
                if self.left(
                        parent_node) == current_node:  # If the current_node is the left child, and current_node's sibling is a leaf, return the sibling.
                    if self.num_children(self.right(parent_node)) == 0:
                        return self.right(parent_node)
                    else:  # Otherwise, set parent node to the right child of parent_node.
                        parent_node = self.right(parent_node)
                        while self.num_children(
                                parent_node) > 0:  # As long as parent_node has children, if it has a left child, set parent_node to the left child.
                            if self.left(parent_node):
                                parent_node = self.left(parent_node)
                            else:
                                parent_node = self.right(parent_node)  # Otherwise set it to the right child.
                        return parent_node  # Then return it.

                elif self.right(
                        parent_node) == current_node:  # If the current_node is its parent's right child, return the parent.
                    return parent_node

    def delete_subtree(self, p):
        '''Remove the entire subtree rooted at position p, making sure to maintain the
        count on the size of the tree.
        '''
        if self.is_empty():
            raise Empty("Queue is empty")  # Check if the tree is empty. If it is, raise an exception.
        else:
            current_node = self._validate(p)  # Validate p's position, and set it to current_node.
            parent_node = current_node._parent  # Set parent_node to current_node's parent.

            if parent_node._left is current_node:  # If current_node is a left child, delete the subtree.
                parent_node._left = None
            else:
                parent_node._right = None  # Else, if it's a right child, delete the subtree.

            x = self._subtree_inorder(p)  # Maintain the count on the size of the tree by using inorder traversal.
            num_deleted = 0
            for i in x:
                num_deleted += 1
            self._size -= num_deleted
            return self._size

    def tree_v1(self):
        """Creating 4 different types of test trees to cover all the possible cases"""
        Q = ExtendedBinaryTree()
        # Example of a improper binary tree
        t_0 = Q._add_root(23)
        t_1 = Q._add_left(t_0, 15)
        t_2 = Q._add_right(t_0, 63)
        t_3 = Q._add_left(t_1, 8)
        t_4 = Q._add_right(t_1, 20)
        t_5 = Q._add_left(t_2, 32)
        t_6 = Q._add_right(t_2, 80)
        t_7 = Q._add_left(t_4, 19)
        t_8 = Q._add_right(t_4, 22)
        t_9 = Q._add_right(t_5, 60)
        t_10 = Q._add_left(t_9, 50)
        return Q, t_0, t_1, t_2, t_3, t_4, t_5, t_6, t_7, t_8, t_9, t_10  # return Tree first and all the other nodes afterwards

    def tree_v2(self):
        P = ExtendedBinaryTree()
        # Example of a improper binary tree with only left children
        t_0 = P._add_root("A")
        t_1 = P._add_left(t_0, 'B')
        t_2 = P._add_left(t_1, 'C')
        t_3 = P._add_left(t_2, 'D')
        t_4 = P._add_left(t_3, 'E')
        t_5 = P._add_left(t_4, 'F')
        t_6 = P._add_left(t_5, 'G')
        return P, t_0, t_1, t_2, t_3, t_4, t_5, t_6

    def tree_v3(self):
        T = ExtendedBinaryTree()
        # Example of a binary tree with only a root
        t_0 = T._add_root("Root")
        return T, t_0

    def tree_v4(self):
        I = ExtendedBinaryTree()
        # Example of a proper binary tree
        t_0 = I._add_root(0)
        t_1 = I._add_left(t_0, 1)
        t_2 = I._add_right(t_0, 2)
        t_3 = I._add_left(t_2, 5)
        t_4 = I._add_right(t_2, 6)
        t_5 = I._add_left(t_4,7)
        t_6 = I._add_right(t_4,8)
        return I, t_0, t_1, t_2, t_3, t_4, t_5, t_6

import unittest
class TestGroupProject(unittest.TestCase):
    """Unittest Class starts here"""
    def test_preorder_tree1(self):
        """Check if preorder traversal is the same as preorder_next on every node for tree 1"""
        Tree = ExtendedBinaryTree()
        Q = Tree.tree_v1()[0]

        positional_list = []
        myList1 = [] # List will contain preorder traversal values
        myList2 = [] # This one will contain preorder_next on every node

        for i in Q.preorder():
            positional_list.append(i)
        for i in Q.preorder():
            myList1.append(i.element())
        myList2.append(positional_list[0].element()) # Add the very first node manually to keep all the elements
        for e in positional_list[:-1]:
            myList2.append(Q.preorder_next(e).element())
        self.assertEqual(myList1, myList2)

    def test_preorder_tree2(self):
        """Check if preorder traversal is the same as preorder_next on every node for tree 2"""
        Tree = ExtendedBinaryTree()
        Q = Tree.tree_v2()[0]

        positional_list = []
        myList1 = []
        myList2 = []

        for i in Q.preorder():
            positional_list.append(i)

        for i in Q.preorder():
            myList1.append(i.element())

        myList2.append(positional_list[0].element())
        for e in positional_list[:-1]:
            myList2.append(Q.preorder_next(e).element())

        self.assertEqual(myList1, myList2)

    def test_preorder_tree3(self):
        """Check if preorder traversal is the same as preorder_next on every node for tree 3"""
        Tree = ExtendedBinaryTree()
        Q = Tree.tree_v3()[0]

        positional_list = []
        myList1 = []
        myList2 = []

        for i in Q.preorder():
            positional_list.append(i)

        for i in Q.preorder():
            myList1.append(i.element())

        myList2.append(positional_list[0].element())
        for e in positional_list[:-1]:
            myList2.append(Q.preorder_next(e).element())

        self.assertEqual(myList1, myList2)

    def test_preorder_tree4(self):
        """Check if preorder traversal is the same as preorder_next on every node for tree 4"""
        Tree = ExtendedBinaryTree()
        Q = Tree.tree_v4()[0]

        positional_list = []
        myList1 = []
        myList2 = []

        for i in Q.preorder():
            positional_list.append(i)

        for i in Q.preorder():
            myList1.append(i.element())

        myList2.append(positional_list[0].element())
        for e in positional_list[:-1]:
            myList2.append(Q.preorder_next(e).element())

        self.assertEqual(myList1, myList2)

    def test_inorder_tree1(self):
        """Check if inorder traversal is the same as inorder_next on every node for tree 1"""
        Tree = ExtendedBinaryTree()
        Q = Tree.tree_v1()[0]

        positional_list = []
        myList1 = []
        myList2 = []

        for i in Q.inorder():
            positional_list.append(i)

        for i in Q.inorder():
            myList1.append(i.element())

        myList2.append(positional_list[0].element())
        for e in positional_list[:-1]:
            myList2.append(Q.inorder_next(e).element())

        self.assertEqual(myList1, myList2)

    def test_inorder_tree2(self):
        """Check if inorder traversal is the same as inorder_next on every node for tree 2"""
        Tree = ExtendedBinaryTree()
        Q = Tree.tree_v2()[0]

        positional_list = []
        myList1 = []
        myList2 = []

        for i in Q.inorder():
            positional_list.append(i)

        for i in Q.inorder():
            myList1.append(i.element())

        myList2.append(positional_list[0].element())
        for e in positional_list[:-1]:
            myList2.append(Q.inorder_next(e).element())

        self.assertEqual(myList1, myList2)

    def test_inorder_tree3(self):
        """Check if inorder traversal is the same as inorder_next on every node for tree 3"""
        Tree = ExtendedBinaryTree()
        Q = Tree.tree_v3()[0]

        positional_list = []
        myList1 = []
        myList2 = []

        for i in Q.inorder():
            positional_list.append(i)

        for i in Q.inorder():
            myList1.append(i.element())

        myList2.append(positional_list[0].element())
        for e in positional_list[:-1]:
            myList2.append(Q.inorder_next(e).element())

        self.assertEqual(myList1, myList2)

    def test_inorder_tree4(self):
        """Check if inorder traversal is the same as inorder_next on every node for tree 4"""
        Tree = ExtendedBinaryTree()
        Q = Tree.tree_v4()[0]

        positional_list = []
        myList1 = []
        myList2 = []

        for i in Q.inorder():
            positional_list.append(i)

        for i in Q.inorder():
            myList1.append(i.element())

        myList2.append(positional_list[0].element())
        for e in positional_list[:-1]:
            myList2.append(Q.inorder_next(e).element())

        self.assertEqual(myList1, myList2)

    def test_postorder_tree1(self):
        """Check if postorder traversal is the same as postorder_next on every node for tree 1"""
        Tree = ExtendedBinaryTree()
        Q = Tree.tree_v1()[0]

        positional_list = []
        myList1 = []
        myList2 = []

        for i in Q.postorder():
            positional_list.append(i)

        for i in Q.postorder():
            myList1.append(i.element())

        myList2.append(positional_list[0].element())
        for e in positional_list[:-1]:
            myList2.append(Q.postorder_next(e).element())

        self.assertEqual(myList1, myList2)

    def test_postorder_tree2(self):
        """Check if postorder traversal is the same as postorder_next on every node for tree 2"""
        Tree = ExtendedBinaryTree()
        Q = Tree.tree_v2()[0]

        positional_list = []
        myList1 = []
        myList2 = []

        for i in Q.postorder():
            positional_list.append(i)

        for i in Q.postorder():
            myList1.append(i.element())

        myList2.append(positional_list[0].element())
        for e in positional_list[:-1]:
            myList2.append(Q.postorder_next(e).element())

        self.assertEqual(myList1, myList2)

    def test_postorder_tree3(self):
        """Check if postorder traversal is the same as postorder_next on every node for tree 3"""
        Tree = ExtendedBinaryTree()
        Q = Tree.tree_v3()[0]

        positional_list = []
        myList1 = []
        myList2 = []

        for i in Q.postorder():
            positional_list.append(i)

        for i in Q.postorder():
            myList1.append(i.element())

        myList2.append(positional_list[0].element())
        for e in positional_list[:-1]:
            myList2.append(Q.postorder_next(e).element())

        self.assertEqual(myList1, myList2)

    def test_postorder_tree4(self):
        """Check if postorder traversal is the same as postorder_next on every node for tree 4"""
        Tree = ExtendedBinaryTree()
        Q = Tree.tree_v4()[0]

        positional_list = []
        myList1 = []
        myList2 = []

        for i in Q.postorder():
            positional_list.append(i)

        for i in Q.postorder():
            myList1.append(i.element())

        myList2.append(positional_list[0].element())
        for e in positional_list[:-1]:
            myList2.append(Q.postorder_next(e).element())

        self.assertEqual(myList1, myList2)

    def test_preorder_TypeError(self):
        """Checking if TypeError is raised for invalid position types for preorder_next"""
        Tree = ExtendedBinaryTree()
        # Q1, Q2, Q3 and Q4 are different types of trees and we cover all the possible cases
        Q1 = Tree.tree_v1()[0]
        Q2 = Tree.tree_v2()[0]
        Q3 = Tree.tree_v3()[0]
        Q4 = Tree.tree_v4()[0]

        self.assertRaises(TypeError, Q1.preorder_next, 5)
        self.assertRaises(TypeError, Q1.preorder_next, "Test1")
        self.assertRaises(TypeError, Q1.preorder_next, 0.0001)
        self.assertRaises(TypeError, Q1.preorder_next, [7,9,2])

        self.assertRaises(TypeError, Q2.preorder_next, 6)
        self.assertRaises(TypeError, Q2.preorder_next, "Test2")
        self.assertRaises(TypeError, Q2.preorder_next, -2.7)
        self.assertRaises(TypeError, Q2.preorder_next, [])

        self.assertRaises(TypeError, Q3.preorder_next, 7)
        self.assertRaises(TypeError, Q3.preorder_next, "Test3")
        self.assertRaises(TypeError, Q3.preorder_next, 2.2)
        self.assertRaises(TypeError, Q3.preorder_next, [2,1.5])

        self.assertRaises(TypeError, Q4.preorder_next, 8)
        self.assertRaises(TypeError, Q4.preorder_next, "Test4")
        self.assertRaises(TypeError, Q4.preorder_next, )
        self.assertRaises(TypeError, Q4.preorder_next, ["Earlham", "+", "College"])

    def test_postorder_TypeError(self):
        """Checking if TypeError is raised for invalid position types for postorder_next"""
        Tree = ExtendedBinaryTree()
        Q1 = Tree.tree_v1()[0]
        Q2 = Tree.tree_v2()[0]
        Q3 = Tree.tree_v3()[0]
        Q4 = Tree.tree_v4()[0]

        self.assertRaises(TypeError, Q1.postorder_next, 5)
        self.assertRaises(TypeError, Q1.postorder_next, "Test1")
        self.assertRaises(TypeError, Q1.postorder_next, 0.0001)
        self.assertRaises(TypeError, Q1.postorder_next, [7, 9, 2])

        self.assertRaises(TypeError, Q2.postorder_next, 6)
        self.assertRaises(TypeError, Q2.postorder_next, "Test2")
        self.assertRaises(TypeError, Q2.postorder_next, -2.7)
        self.assertRaises(TypeError, Q2.postorder_next, [])

        self.assertRaises(TypeError, Q3.postorder_next, 7)
        self.assertRaises(TypeError, Q3.postorder_next, "Test3")
        self.assertRaises(TypeError, Q3.postorder_next, 2.2)
        self.assertRaises(TypeError, Q3.postorder_next, [2, 1.5])

        self.assertRaises(TypeError, Q4.postorder_next, 8)
        self.assertRaises(TypeError, Q4.postorder_next, "Test4")
        self.assertRaises(TypeError, Q4.postorder_next, )
        self.assertRaises(TypeError, Q4.postorder_next, ["Earlham", "+", "College"])

    def test_inorder_TypeError(self):
        """Checking if TypeError is raised for invalid position types for inorder_next"""
        Tree = ExtendedBinaryTree()
        Q1 = Tree.tree_v1()[0]
        Q2 = Tree.tree_v2()[0]
        Q3 = Tree.tree_v3()[0]
        Q4 = Tree.tree_v4()[0]

        self.assertRaises(TypeError, Q1.inorder_next, 5)
        self.assertRaises(TypeError, Q1.inorder_next, "Test1")
        self.assertRaises(TypeError, Q1.inorder_next, 0.0001)
        self.assertRaises(TypeError, Q1.inorder_next, [7, 9, 2])

        self.assertRaises(TypeError, Q2.inorder_next, 6)
        self.assertRaises(TypeError, Q2.inorder_next, "Test2")
        self.assertRaises(TypeError, Q2.inorder_next, -2.7)
        self.assertRaises(TypeError, Q2.inorder_next, [])

        self.assertRaises(TypeError, Q3.inorder_next, 7)
        self.assertRaises(TypeError, Q3.inorder_next, "Test3")
        self.assertRaises(TypeError, Q3.inorder_next, 2.2)
        self.assertRaises(TypeError, Q3.inorder_next, [2, 1.5])

        self.assertRaises(TypeError, Q4.inorder_next, 8)
        self.assertRaises(TypeError, Q4.inorder_next, "Test4")
        self.assertRaises(TypeError, Q4.inorder_next, )
        self.assertRaises(TypeError, Q4.inorder_next, ["Earlham", "+", "College"])

    def test_deletesubtree_TypeError(self):
        """Checking if TypeError is raised for invalid position types for delete_subtree"""
        Tree = ExtendedBinaryTree()
        Q1 = Tree.tree_v1()[0]
        Q2 = Tree.tree_v2()[0]
        Q3 = Tree.tree_v3()[0]
        Q4 = Tree.tree_v4()[0]

        self.assertRaises(TypeError, Q1.delete_subtree, 5)
        self.assertRaises(TypeError, Q1.delete_subtree, "Test1")
        self.assertRaises(TypeError, Q1.delete_subtree, 0.0001)
        self.assertRaises(TypeError, Q1.delete_subtree, [7, 9, 2])

        self.assertRaises(TypeError, Q2.delete_subtree, 6)
        self.assertRaises(TypeError, Q2.delete_subtree, "Test2")
        self.assertRaises(TypeError, Q2.delete_subtree, -2.7)
        self.assertRaises(TypeError, Q2.delete_subtree, [])

        self.assertRaises(TypeError, Q3.delete_subtree, 7)
        self.assertRaises(TypeError, Q3.delete_subtree, "Test3")
        self.assertRaises(TypeError, Q3.delete_subtree, 2.2)
        self.assertRaises(TypeError, Q3.delete_subtree, [2, 1.5])

        self.assertRaises(TypeError, Q4.delete_subtree, 8)
        self.assertRaises(TypeError, Q4.delete_subtree, "Test4")
        self.assertRaises(TypeError, Q4.delete_subtree, )
        self.assertRaises(TypeError, Q4.delete_subtree, ["Earlham", "+", "College"])

    def test_ValueError(self):
        """Checking if ValueError is raised for invalid positions"""
        Tree = ExtendedBinaryTree()
        Q1 = Tree.tree_v1()[0]
        Q2 = Tree.tree_v2()[0]
        Q3 = Tree.tree_v3()[0]
        Q4 = Tree.tree_v4()[0]

        TestPosition = ExtendedBinaryTree()
        p_1 = TestPosition._add_root(0)
        p_2 = TestPosition._add_left(p_1, 4)
        p_3 = TestPosition._add_right(p_1, 6)
        p_4 = TestPosition._add_right(p_3, 6)

        self.assertRaises(ValueError, Q1.preorder_next, p_1)
        self.assertRaises(ValueError, Q2.inorder_next, p_2)
        self.assertRaises(ValueError, Q3.postorder_next, p_3)
        self.assertRaises(ValueError, Q4.delete_subtree, p_4)

    def test_deletesubtree_tree1(self):
        """Checking if deletesbutree works for tree1"""
        Q = ExtendedBinaryTree()
        t_0 = Q._add_root(23)
        t_1 = Q._add_left(t_0, 15)
        t_2 = Q._add_right(t_0, 63)
        t_3 = Q._add_left(t_1, 8)
        t_4 = Q._add_right(t_1, 20)
        t_5 = Q._add_left(t_2, 32)
        t_6 = Q._add_right(t_2, 80)
        t_7 = Q._add_left(t_4, 19)
        t_8 = Q._add_right(t_4, 22)
        t_9 = Q._add_right(t_5, 60)
        t_10 = Q._add_left(t_9, 50)
        del_myList = [] # This list will contain all the values that were not deleted in inorder traversal
        new_myList = [] # This list will contain all the values until the node that we removed in inorder traversal

        # And these two lists should be the same

        remove_node = t_2

        Q.delete_subtree(remove_node)

        for i in Q.inorder():
            del_myList.append(i.element())

        for i in Q.inorder():
            new_myList.append(i.element())
            if i.element() == remove_node:
                break

        self.assertEqual(del_myList, new_myList)

    def test_deletesubtree_tree2(self):
        """Checking if deletesbutree works for tree2"""
        Q = ExtendedBinaryTree()
        t_0 = Q._add_root("A")
        t_1 = Q._add_left(t_0, 'B')
        t_2 = Q._add_left(t_1, 'C')
        t_3 = Q._add_left(t_2, 'D')
        t_4 = Q._add_left(t_3, 'E')
        t_5 = Q._add_left(t_4, 'F')
        t_6 = Q._add_left(t_5, 'G')
        del_myList = []
        new_myList = []

        remove_node = t_2

        Q.delete_subtree(remove_node)

        for i in Q.inorder():
            del_myList.append(i.element())

        for i in Q.inorder():
            new_myList.append(i.element())
            if i.element() == remove_node:
                break

        self.assertEqual(del_myList, new_myList)

    def test_deletesubtree_tree3(self):
        """Checking if deletesbutree works for tree3"""

        Q = ExtendedBinaryTree()
        t_0 = Q._add_root("Root")
        t_1 = Q._add_left(t_0, "Left Node")
        del_myList = []
        new_myList = []

        remove_node = t_1

        Q.delete_subtree(remove_node)

        for i in Q.inorder():
            del_myList.append(i.element())

        for i in Q.inorder():
            new_myList.append(i.element())
            if i.element() == remove_node:
                break

        self.assertEqual(del_myList, new_myList)

    def test_deletesubtree_tree4(self):
        """Checking if deletesbutree works for tree4"""
        Q = ExtendedBinaryTree()
        t_0 = Q._add_root(0)
        t_1 = Q._add_left(t_0, 1)
        t_2 = Q._add_right(t_0, 2)
        t_3 = Q._add_left(t_2, 5)
        t_4 = Q._add_right(t_2, 6)
        t_5 = Q._add_left(t_4, 7)
        t_6 = Q._add_right(t_4, 8)
        del_myList = []
        new_myList = []

        remove_node = t_2

        Q.delete_subtree(remove_node)
        for i in Q.inorder():
            del_myList.append(i.element())

        for i in Q.inorder():
            new_myList.append(i.element())
            if i.element() == remove_node:
                break

        self.assertEqual(del_myList, new_myList)

    def test_empty(self):
        """Check is code raises Empty when we use empty tree with all the methods"""
        Tree = ExtendedBinaryTree()
        self.assertRaises(Empty, Tree.preorder_next, 1)
        self.assertRaises(Empty, Tree.inorder_next, 1)
        self.assertRaises(Empty, Tree.postorder_next, 1)
        self.assertRaises(Empty, Tree.delete_subtree, 1)

    def test_None_preorder(self):
        """Check if we get none for preorder_next function on the very last position of the preoder list"""
        Tree = ExtendedBinaryTree()
        Q = Tree.tree_v1()[0]
        myList = []
        for i in Q.preorder():
            myList.append(i)
        self.assertEqual(Q.preorder_next(myList[-1]), None)

    def test_None_inorder(self):
        """Check if we get none for inorder_next function on the very last position of the inorder list"""
        Tree = ExtendedBinaryTree()
        Q = Tree.tree_v1()[0]
        myList = []
        for i in Q.inorder():
            myList.append(i)
        self.assertEqual(Q.inorder_next(myList[-1]), None)

    def test_None_postorder(self):
        """Check if we get none for postorder_next function on the very last position of the postorder list"""
        Tree = ExtendedBinaryTree()
        Q = Tree.tree_v1()[0]
        myList = []
        for i in Q.postorder():
            myList.append(i)
        self.assertEqual(Q.postorder_next(myList[-1]), None)

if __name__ == '__main__':

    unittest.main()

