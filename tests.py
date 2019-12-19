from threeMod import threeMod as tm
import unittest
import logging
import sys

class testThreeMod(unittest.TestCase):
    def testInitAssign(self):
        iArray = [1,2,3,4,5,6,7,8,9]
        threeModDec = tm.threeMod()
        self.assertNotEqual(iArray,threeModDec.iArr)
        threeModDec.assign(iArray)
        self.assertNotEqual(None,threeModDec.iArr)

class testMaxThree(unittest.TestCase):
    def testInit(self):
        iArray = [1,2,3,4,5,6,7,8,9]
        threeModDec = tm.maxThree(iArray)
        threeModDecGet = threeModDec.get()
        tv = tm.threeVal(24, 7, 8, 9)
        self.assertEqual(threeModDecGet.value,tv.value)

if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout,level=logging.DEBUG)
    unittest.main()