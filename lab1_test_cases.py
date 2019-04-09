import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        self.assertEqual(max_list_iter([10, 1, 3, 7, 5]), 10)
        self.assertEqual(max_list_iter([]), None)
        self.assertEqual(max_list_iter([3]), 3)

    def test_reverse_rec(self):
        tlist = None
        with self.assertRaises(ValueError):
            reverse_rec(tlist)
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([1]), [1])
        self.assertEqual(reverse_rec([]),[])
        

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )

        list_val2 =[1,2,3,4,7,8,9,10]
        low = 1
        high = len(list_val2)-1
        self.assertEqual(bin_search(7, 1, len(list_val2)-1, list_val2), 4 )

        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = 8
        self.assertEqual(bin_search(9, low, high, list_val), 7 )

       
if __name__ == "__main__":
        unittest.main()

    
