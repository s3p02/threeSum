import logging

class threeVal:
    def __init__(self, value, e1, e2, e3):
        self.value = value
        self.e1 = e1
        self.e2 = e2
        self.e3 = e3
        logging.debug("CLASS threeVal METHOD __init__ value={0} e1={1} e2={2} e3={3}".format(self.value, self.e1, self.e2, self.e3))

class threeMod:
    def __init__(self, iArr=None):
        self.iArr = iArr
        logging.debug("CLASS threeMod METHOD __init__ iArr={}".format(self.iArr))

    def assign(self, inputArray):
        self.iArr = inputArray
        logging.debug("CLASS threeMod METHOD assign iArr={}".format(self.iArr))


class maxThree(threeMod):
    def __init__(self, iArray):
        super().__init__(iArray)
        logging.debug("CLASS maxThree METHOD __init__ iArray={}".format(iArray))
    
    def get(self):
        iArrayLength = len(self.iArr)
        sumOf3 = self.iArr[0] + self.iArr[1] + self.iArr[2]
        logging.debug("CLASS maxThree METHOD get iter={0} sumOf3={1}".format(1, sumOf3))
        maxVal = threeVal(sumOf3, self.iArr[0], self.iArr[1], self.iArr[2])
        logging.debug("CLASS maxThree METHOD get sum3={0} maxVal.value={1}".format(sumOf3, maxVal.value))
        for element in range(2, iArrayLength - 1):
            sum3 = self.iArr[element - 1] + self.iArr[element] + self.iArr[element + 1]
            logging.debug("CLASS maxThree METHOD get iter={0} sum3={1}".format(element, sum3))
            if(sum3 > maxVal.value):
                logging.debug("CLASS maxThree METHOD get sum3 > maxVal.value : {0} > {1}".format(sum3, maxVal.value))
                maxVal = threeVal(sum3, self.iArr[element - 1], self.iArr[element], self.iArr[element + 1])
        return maxVal