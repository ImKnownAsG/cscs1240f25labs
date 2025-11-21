from item import Item

def fact(n): #calculates n!
    fact = 1
    while n > 0:
        fact *= n
        n -= 1
    
    return fact
    

def swaps(n = 1): #n = number of permuted items
    '''swaps generates the required series of element swaps to 
    facilitate a Heap permutation algorithm'''
    
    c = Item()
    ind = list(range(1, n + 1))
    swapCount = [0] * n
    i = 0
        
    while True:
        if i >= n:
            break
            
        if swapCount[i] < i:
            if i % 2 == 1:
                swapInd = swapCount[i]
            else:
                swapInd = 0
            
            indOne = min(swapInd, i) + 1
            indTwo = max(swapInd, i) + 1
            c.append(Item([indOne, indTwo]))
            ind[swapInd], ind[i] = ind[i], ind[swapInd]
            swapCount[i] += 1
            i = 0
        else:
            swapCount[i] = 0
            i += 1
        
#        while t > 0: #check from the largest factorial to the smallest for elements n
#            fn = fact(t) #behavior changes dependent on if the swap step is a multiple of factorials from 1 to n
#            if i % 2 == 1: #every odd swap is the same, no need to check anything here
#                c.append(Item([1,2]))
#                break
#            elif i % fn == 0: #the swap step is a multiple of one of the factorials
#                if t == 2: # multiples of 2! are treated the same
#                    c.append(Item([1, t + 1]))
#                else: # otherwise the swap is calculated with respect to which factorial multiple was found
#                    c.append(Item([(i // fn) % (t + 1), t + 1]))
#                break
            
#            t -= 1

    return c

def swap(list, swap):
    newList = list[:]
    newList[swap[0] - 1], newList[swap[1] - 1] = list[swap[1] - 1], list[swap[0] - 1]
    return newList
    

def perm(elem, swapList):        
    permList = Item(elem)
    if swapList.object() != None:
        for _ in swapList:
            tempList = permList.object()
            thisSwap = _.object()
            newPerm = swap(tempList, thisSwap)
            permList = permList.append(newPerm)
    
    
    return permList

'''
elements = 4
swapList = swaps(elements)

for _ in swapList:
    print(_.object())
    
listCount = 0

elementListCount = []

elementList = []
for _ in range(elements):
    elementList.append(_)
    elementListCount.append(0)

permutation = perm(elementList, swapList)

for _ in permutation:
    for i in range(elements):
        if i == _[i]:
            elementListCount[i] += 1
    print(_)

print(f'elementList: {elementListCount}')
'''