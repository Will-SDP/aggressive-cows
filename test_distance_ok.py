import unittest 
from distance_ok import distance_ok

class TestCalass(unittest.TestCase):
    def test_case_one(self):
        stalls = [1, 4, 6, 7,10]
        cows = 3 
        distance = 4
        self.assertTrue(distance_ok(stalls, cows, distance))        

if __name__=='__main__':
    unittest.main()            