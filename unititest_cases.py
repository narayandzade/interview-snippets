



import unittest



class Mytestcase(unittest.TestCase):
    def test_add(self):
        return self.assertEqual(add(1,3),4)
    





if __name__ == "__main__":
    unittest.main()