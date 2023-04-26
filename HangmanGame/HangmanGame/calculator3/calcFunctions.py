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
    try:
        n = int(numStr)
    except:
        return 'Error!'

    if n >= 4000:
        return 'Error!'

    romans = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]

    result = ''
    for value, letters in romans:
        while n >= value:
            result += letters
            n -= value

    return result

def RomanTodec(numStr):

    s = numStr

    romans = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]

    result = 0

    if s.isalpha() :
        for value, letters in romans :
            while s.find(letters) == 0:
                s = s[1 :]
                result += value
    else :
        result = 'Error!'

    return result





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

        elif self.key == functionList[4]:
            return RomanTodec(n)