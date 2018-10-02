import unittest
from LCA import lca
from BinaryTree import bst


class TestLCA(unittest.TestCase):

    def test_answer(self):
        # Test numbers at both sides of root
        self.assertEqual(lca(bst, 5, 49), 11)
        # Test two of the same number
        self.assertEqual(lca(bst, 10, 10), 10)
        # Test if one of the Nodes does not exist
        self.assertEqual(lca(bst, 6, 9), None)
