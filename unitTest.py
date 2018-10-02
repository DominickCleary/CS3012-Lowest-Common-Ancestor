import unittest
from LCA import lca, bst


class TestLCA(unittest.TestCase):

    def test_bst(self):
        # Test numbers at both sides of root
        self.assertEqual(lca(bst, 5, 49), 11)
        # Test two of the same number
        self.assertEqual(lca(bst, 10, 10), 10)
        # Test if where one or two of the Nodes do not exist (9)
        self.assertEqual(lca(bst, 6, 9), None)
        self.assertEqual(lca(bst, 48, 2), None)
        # Test if one number is a direct descendant of the other
        self.assertEqual(lca(bst, 49, 19), 19)
        self.assertEqual(lca(bst, 5, 6), 6)
        # Test with invalid inputs, eg. Strings & floats
        self.assertEqual(lca(bst, "TEST", 19), None)
        self.assertEqual(lca(bst, 1.923, 20), None)
