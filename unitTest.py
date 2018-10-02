import unittest
from LCA import lca, bst


class UnitTests(unittest.TestCase):

    def test_lca(self):
        # Test numbers at both sides of root
        self.assertEqual(11, lca(bst, 5, 49))
        # Test two of the same number
        self.assertEqual(10, lca(bst, 10, 10))
        # Test if where one or two of the Nodes do not exist (9)
        self.assertEqual(None, lca(bst, 6, 9))
        self.assertEqual(None, lca(bst, 48, 2))
        # Test if one number is a direct descendant of the other
        self.assertEqual(19, lca(bst, 49, 19))
        self.assertEqual(6, lca(bst, 5, 6))
        # Test with invalid inputs, eg. Strings & floats
        self.assertEqual(None, lca(bst, "TEST", 19))
        self.assertEqual(None, lca(bst, 1.923, 20))

    def test_bst(self):
        # Test printing
        self.assertEqual("11 (6 (4 (None, 5), 8 (None, 10)), 19 (17, 43 (31, 49)))", str(bst))
