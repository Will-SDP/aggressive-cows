import unittest 
from aggressive_cows_method2 import aggressive_cows

class TestClass(unittest.TestCase):
    # Test case from breif
    def test_example_from_brief(self):
        stalls = [1, 4, 6, 7,10]
        cows = 3 
        self.assertEqual(aggressive_cows(stalls, cows), 4)

    # Test large numbers
    def test_big_numbers(self):
        stalls = [1,1000]
        cows = 2 
        self.assertEqual(aggressive_cows(stalls, cows), 999)

    # Test equal cows and stalls 
    def test_equal_cows_stalls(self):
        stalls = [1,2,3,4,5]
        cows = 5 
        self.assertEqual(aggressive_cows(stalls, cows), 1)    
        



if __name__=='__main__':
    unittest.main()        