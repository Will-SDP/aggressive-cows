import unittest 
from aggressive_cows import aggressive_cows 

class TestClass(unittest.TestCase):
    def test_example_from_brief(self):
        stalls = [1, 4, 6, 7,10]
        cows = 3 
        self.assertEqual(aggressive_cows(stalls, cows), 4)


if __name__=='__main__':
    unittest.main()        