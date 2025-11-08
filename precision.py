from decimal import Decimal

def genBinary(num):
    
    if not isinstance(num, (int)):
        raise TypeError(f'Must be an integer, got {num}')
        return null, null
        
    startBit = 16
    
    while 2**startBit < int(num):
        startBit += 4
    
    numArr = [[0] for _ in range(startBit + 2)] #+1 for sign, +1 for 0 exponent

    if num < 0:
        numArr[0] = ['neg', 1]
    else:
        numArr[0] = ['pos', 1]
    
    exp = startBit
    while exp >= 0:
        arrInd = startBit - exp + 1
        if 2**exp <= num:
            numArr[arrInd] = [exp, 1]
            num = num - 2**exp
        
        else:
            numArr[arrInd] = [exp, 0]
            
        exp += -1
    
    return numArr
        
def addBinary(firstNum, secNum):
    newNum = [[0] for _ in range(max(len(firstNum), len(secNum)) + 1)]
    carry = [[0] for _ in range(len(newNum))]
    
    '''start here
    firstNumNorm = [[0] for _ in range(len(newNum))]
    
    secNumNorm = [[0] for _ in range(len(newNum))]
    
    print(len(newNum))
    print(len(carry))
    
    exp = len(newNum)
    while exp > 0:
        firstNumBit = firstNum[exp][1]
        secNumBit = secNum[exp][1]
        carrBit = carry[exp][1]
        print(firstnum[exp][0])

        if firstNumBit == 1 and secNumBit == 1:
            
            if carry[exp][1] == 1:
                newNum[exp] = [firstNum[exp][0], 1]
            else:
                newNum[exp] = [firstNum[exp][0], 0]
            
            carry[exp - 1][1] = 1
        elif firstNumBit == 0 and secNumBit == 0:
            
            if carry[exp][1] == 1:
                newNum[exp] = [firstNum[exp][0], 1]
            else:
                newNum[exp] = [firstNum[exp][0], 0]
        
        else:
            
            if carry[exp][1] == 1:
                newNum[exp] = [firstNum[exp][0], 0]
            else:
                newNum[exp] = [firstNum[exp][0], 1]
        
        exp += -1
    
    return newNum
    
firstNum = genBinary(18)
secNum = genBinary(6)

print(addBinary(firstNum, secNum))


'''
def showPrec(num):
    precNum = num
    expSum = Decimal(0)
    expVal = []
    print(num)
    for _ in range(98):
        if precNum >= Decimal(2**(-_ + 1)):
            precNum = precNum % Decimal(2**(-_ + 1))
            expSum = expSum + Decimal(2**(-_ + 1))
            expVal.append([_ + 1, 1])
            
            if expSum == num:
                break
        else:
            expVal.append([_ + 1, 0])
                
    print(expSum)
    return expVal
'''

#expVal = showPrec(Decimal(1/17))

#print(*expVal, sep='\n')

