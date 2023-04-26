from keypad import constantList, functionList

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    return 'dec -> Roman'



def constant(self):
        if self.key == constantList[0]:
            return '3.141592'
        elif self.key == constantList[1]:
            return '3E+8'
        elif self.key == constantList[2]:
            return '340'
        elif self.key == constantList[3]:
            return '1.5E+8'

def function(self):
        n = self.display.text()

        if self.key == functionList[1]:
            return decToBin(n)

        elif self.key == functionList[2]:
            return binToDec(n)

        elif self.key == functionList[3]:
            return decToRoman(n)