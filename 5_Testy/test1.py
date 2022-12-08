import unittest 

def add(x, y):
    return x + y

class SimpleTest(unittest.TestCase):
    
    def test_add(self): 
        self.assertEqual(add(3, 4), 7, msg='Powinno być 7')
               
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)