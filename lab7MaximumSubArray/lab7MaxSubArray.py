import random

'''
I wanted a function to generate the full arrays.
This takes:
 arrLen for the number of discreet items in the array
 arrMin for the minimum value an array item can be generated with 
  - if there are no negative numbers in the array the max sum will 
    just be the sum of every value in the array
 arrMax for the maximum value an array item can be generated with
'''
def genArr(arrLen = 10, arrMin = -10, arrMax = 10):
    newArr = []
    
    if arrMin > arrMax: #Random breaks if the min provided is greater than the max provided, so I swap them if necessary
        arrMin, arrMax = arrMax, arrMin
        
    for _ in range(arrLen): #Loop to add each array element
        newArr.append(random.randint(arrMin, arrMax))
    
    return newArr

def kadaneMaxSum(thisArr):
    '''
    Initializing the variables used during this method
    currRes stores the value of the current sub-array that has been checked
    result is the sub-array found to that point
    startInd and endInd are the beginning and ending indices for the sub-array that is found
     I wanted to be able to print these at the endInd - the values stored are as though a human counted, so starting from 1 instead of 0
    minLen is used to determine which sub-array should be returned in the event more than one makes up the max sum
     I don't think this is part of the traditional Kadane algorithm, but seemed value adding to me
    steps was used to track how many times a value was added and checked
    resStep is how many steps it took to find the result
    '''
    currRes = 0
    result = 0
    startInd = 0
    endInd = 0
    minLen = len( thisArr) #initialized to the full length of the string, reassigned if a shorter sub-array is found
    steps = 0
    resStep = 0
    
    i = 0
    while i < len( thisArr): #we're definitely going to have to check every array element
        #print(thisArr)
        currRes = thisArr[i] #adding the i'th element to the currently calculated result - anytime the code is here it is starting a new sub-array, so nothing to add to
        #print(f'Checking from element {i + 1}')
        
        steps += 1
        
        for j in range( i, len( thisArr)): #Start checking the subsequent elements
            
            #print(f'Checking to element {j + 1}')
            if not i == j: #this loop was started = i, so no additional step and the array element shouldn't be added again
                steps += 1
                currRes = currRes + thisArr[j]            
            
            #print(f'Steps: {steps}')
            #print(f'The current result is {currRes}')
            
            if (currRes > result) or (currRes == result and j - i < minLen): #if our new sum is larger than the old best, or equal to with a shorter length
                result = currRes #set the new best
                startInd = i + 1 # +1 to achieve the human style count
                endInd = j + 1
                minLen = j - i + 1 
                resStep = steps
            
            if currRes <= 0: #if the sum has gone negative it's always better to start new (according to Geeks for Geeks)
                i = j #we know that the last element added made the sum <0 so we obviously don't want to start with that element on our next go, but i is incremented later so we will start with the next element
                #print(f'Starting over? i: {j + 1}')
                break
                
            if j == len( thisArr) - 1: #j is 0 indexed, so when we reach the end of the array we don't want to circle back to the next starting element
                i = j
            
        i = i + 1 #for loops can't be controlled with an index, so I had to set this up as a while loop
        
    return startInd, endInd, result, steps, resStep #there's probably a better way to do this, but I wanted all the values returned

def naiveMaxSum(thisArr):
    #this was the first method I made but I'm going to refer you to the other one for comments on the variables, they're all the same
    
    currRes = 0
    result = 0
    startInd = 0
    endInd = 0
    minLen = len( thisArr)
    steps = 0
    resStep = 0
    
    for i in range( len( thisArr)): #this search is easy to implement, start searching from every element in the array and try adding every subsequent element to it
        #print('------')
        #print(f'Checking from startInd: {i + 1} ({thisArr[i]})')
        currRes = 0
        
        for j in range(i, len( thisArr)):
            #print(f'Checking endInd: {j + 1} ({thisArr[j]})')
            currRes = currRes + thisArr[j]
            #print(f'The current result is {currRes}')
            steps += 1
            
            if (currRes > result) or (currRes == result and j - i < minLen): #I think this is better
            #if (currRes > result) or (result == 0 and currRes < 0) or (currRes == result and j - i < minLen): 
                '''
                there's an additional or clause here.  Because we don't start over from the next element if we are <0, 
                I needed a way to initialize the sub-array when it starts with a negative...thinking about this now I think there is a problem
                I think I wanted to handle edge cases where all the values are negative and no result gets set, 
                but with this I could set an incorrect max sum if I reached 0 then saw a negative element next within a sub-array
                '''
                result = currRes
                startInd = i + 1
                endInd = j + 1
                minLen = endInd - startInd + 1
                resStep = steps
                    
    return startInd, endInd, result, steps, resStep
    
def getSubArr(thisArr, startInd, endInd): #this takes care of identifying the elements in the sub-array
    subArr = []
    
    #not sure why I complicated this
    '''if startInd == endInd:
        subArr.append(thisArr[startInd - 1])
    else:
        for _ in range(startInd - 1, endInd):
            subArr.append([_ + 1, thisArr[_]])
    '''
    #when this works just as well
    for _ in range(startInd - 1, endInd):
        subArr.append([_ + 1, thisArr[_]]) #I wanted to see the (human count) index number as well as the value in the sub-array
        
    return subArr

#various counters for the summary details
allNaiveSteps = 0
allNaiveResSteps = 0
allKadSteps = 0
allKadResSteps = 0

#run this however you would like - each cycle is a new array to review and the other variables are used to generate the arrays
cycles = 1
arrLen = 20
minArr = -10
maxArr = 10

#When I was running 100+ cycles I wanted to have an easier way of checking for mismatched results between the naive and Kadane approach
#so if one was found I appended it to this array then printed at the end
misMatch = []

for _ in range(cycles):
    thisArr = genArr(arrLen, minArr, maxArr)
    
    '''
    these were various arrays that I had trouble with, 
    so I would comment out the random generator
    and hard code them until I identified the problem.
    I'm sorry to say I don't remember most of the problemative details
    '''
    #thisArr = [-9, -10, -6, -6, 0, -3, -2, 6, -1, 0]
    #thisArr = [3, 1, -6, 3, -10, 4, -1, -10, 2, -2]
    #thisArr = [0, 10, -2, 5, 2, 10, -8, 6, -4, 0]
    #thisArr = [4, -1, 2, -7, 3, 4, -2, 9, -10, 2, 5]
        
    naiveStartInd, naiveEndInd, naiveResult, naiveSteps, naiveResStep = naiveMaxSum( thisArr)
    naiveSubArr = getSubArr(thisArr, naiveStartInd, naiveEndInd)

    print(f'\nFor the array: {thisArr}')

    print(f'Naive:  Result: {naiveResult}, Sub-array: {naiveSubArr}, Search Steps: {naiveSteps}, Result steps: {naiveResStep}')
    

    kadStartInd, kadEndInd, kadResult, kadSteps, kadResStep = kadaneMaxSum( thisArr)
    kadSubArr = getSubArr(thisArr, kadStartInd, kadEndInd)

    print(f'Kadane: Result: {kadResult}, Sub-array: {kadSubArr}, Search steps: {kadSteps}, Result steps: {kadResStep}')
    
    if not naiveResult == kadResult: #checking for mismatched results
        misMatch.append(thisArr)
    
    allNaiveSteps = allNaiveSteps + naiveSteps #aggregating the step counts
    allNaiveResSteps = allNaiveResSteps + naiveResStep

    allKadSteps = allKadSteps + kadSteps
    allKadResSteps = allKadResSteps + kadResStep

print(f'\nFor {cycles} searches of a {arrLen} element array')

#I don't think this averages actually mean anything, but at the time I was interested to see them
#The actual step counts are what's important for processing time, where the result is in the array is irrelevant
print(f'Naive: Average steps: {int(round(allNaiveSteps / cycles, 0))}, Average Result Steps: {int(round(allNaiveResSteps / cycles, 0))}') #This step count should always equal (arrLen * (arrLen + 1))/2
print(f'Kadane: Average steps: {int(round(allKadSteps / cycles, 0))}, Average Result Steps: {int(round(allKadResSteps / cycles, 0))}') #This step count should always equal arrLen - the exponential growth of the line above vs the linear growth of this number is where the work savings is
print(f'The mismatched results are:\n{misMatch}')
