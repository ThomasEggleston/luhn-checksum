'''
    Luhn Checksum - Thomas Eggleston 2016

    This program checks to see whether a given integer validates using the Luhn
    formula. For a number to be valid, all of the digits in the number are
    summed together and must be divisible by 10. From the rightmost digit, every
    second digit is doubled and if the product is greater than or equal to 10,
    then the two digits are added together.

    In this implementation, the checksum is calculated after each digit of the
    number is processed, and the length of the number is assumed to be unknown
    as if there is a stream of digits.
'''

import sys, string

def luhnChecksum(string):
    valid = False
    digits = 0
    checksum1 = 0
    checksum2 = 0

    for n in string:
        digits += 1
        n = int(n)

        if digits % 2 == 1:
            checksum1 = addSingle(n, checksum1)
            checksum2 = addDouble(n, checksum2)
        else:
            checksum2 = addSingle(n, checksum2)
            checksum1 = addDouble(n, checksum1)

        valid = checkFinished(checksum1, checksum2, digits)

    return valid

def addSingle(n, checksum):
    checksum += n
    return checksum

def addDouble(n, checksum):
    if n < 5:
        checksum += 2 * n
    else:
        checksum +=  2 * n - 10 + 1
    return checksum

def checkFinished(checksum1, checksum2, digits):
    isFinished = False

    if digits % 2 == 1:
        if checksum1 % 10 == 0 and checksum1 > 0:
            isFinished = True
    else:
        if checksum2 % 10 == 0 and checksum2 > 0:
            isFinished = True

    return isFinished

def validateCharacter(char):
    if char in string.digits:
        return True
    else:
        return False

def validateString(inputString):
    valid = [validateCharacter(c) for c in inputString]
    if False not in valid:
        return True
    else:
        return False

if __name__ == '__main__':
    if len(sys.argv) == 2:
        inputText = sys.argv[1].strip()
        if validateString(inputText):
            print(luhnChecksum(inputText))
        else:
            print("Invalid string: Must only contain digits")
    else:
        print("No input given: Enter a number as a string")
