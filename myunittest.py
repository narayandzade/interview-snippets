import unittest

def reverse_list(lst):
    if len(lst) <= 1:
        return lst
    return reverse_list(lst[1:]) + [lst[0]]


class TestReverselist(unittest.TestCase):

    def test_reverse_function(self):
        self.assertEqual(reverse_list([1,2,3,4,5]),[5,4,3,2,1])





unittest.main()