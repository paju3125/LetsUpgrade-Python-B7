import prime_check
import unittest
class CheckPrimeNumber(unittest.TestCase):
    def TestSingleNumber(self):
        num=7
        result=check_Prime(num)
        self.assertEquals(result,"Not prime number")

if __name__=="__main__":
    unittest.main()
    
