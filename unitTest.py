import unittest
from LCA import lca_bst
from BinaryTree import bst_root


class TestLCA(unittest.TestCase):

    def test_answer(self):
        # Test numbers at both sides of root
        self.assertEqual(str(lca_bst(bst_root, 5, 49)), "11")
