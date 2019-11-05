import math
import numpy as np
import matplotlib.pyplot as plt
import random
import copy

class Set:
    
    #attributes for set/subset elements and their summations
    elements = []
    setSum = sum(elements)

    #init
    def __init__(self, elements = []):
        self.elements = elements
        self.setSum = sum(elements)

    def __repr__(self):
        """
        organizing string output of Set type: elements - *list of elements*, sum = *setSum*
        """
        return "\nelements = " + str(self.elements) + ", sum = " + str(self.setSum)
    
    def retSum(self):
        return self.setSum
    
    def sumSet(self):
        self.setSum = sum(self.elements)

def BFIss(goalSum, testSet = []):
    """
    Sums all possible subsets checking for sumGoal. If found, returns STRING of subSet with sum = sumGoal, otherwise returns STRING failure statement.
    """
    count = 0
    subSets = [Set([])]                                             #adding the first subset, the null set
    for value in testSet:
        newSubSets = []
        for sets in subSets:
            newSet = Set()
            newSet.elements = copy.copy(sets.elements)
            newSet.elements.append(value)
            newSet.sumSet()
           
            newSubSets.append(sets)
            newSubSets.append(newSet) 
            
            count += 1                                              #counting operations    

            if newSet.setSum == goalSum:
                return count
        subSets = copy.deepcopy(newSubSets)
    return count

def modBFIss(goalSum, testSet = []):
    """
    Sums all possible subsets checking for sumGoal. If found, prints subSet with sum = sumGoal and returns TRUE, otherwise returns all subsets sorted by sum.
    """
    count = 0
    
    subSets = [Set([])]                                                 #adding the first subset, the null set
    for value in testSet:
        newSubSets = []
        for sets in subSets:
            newSet = Set()                                              #__init__ fails to sum newSet if sets.elements was empty, to combat this the elements are appended and the set is summed after 
            newSet.elements = copy.copy(sets.elements)
            newSet.elements.append(value)
            newSet.sumSet()

            newSubSets.append(sets)
            newSubSets.append(newSet)

            if newSet.setSum == goalSum:
                return count
        subSets = copy.deepcopy(newSubSets)
    return sorted(subSets, key = lambda x: x.setSum)

def pairSum(count, goalSum, setA = [], setB = []):
    """
    Checks summation of pairs of subsets or elements for goalSum value. Returns indA and indB as a list if goalSum is the sum of 2 elements, otherwise returns FALSE.
    """
    indA = 0
    indB = len(setB) - 1
    while indA < len(setA) and indB >= 1:
        val = setA[indA].setSum + setB[indB].setSum
        if val == goalSum:
            return count
        elif val < goalSum:
            indA+=1
        else:
            indB-=1
        
        count += 1

    return count

def HSss(goalSum, testSet =[]):
    """
    Sums all possible subsets checking for sumGoal. If found, returns STRING of subSet with sum = sumGoal, otherwise returns STRING failure statement.
    """
    sLeft = testSet[:int(len(testSet)/2)]
    sRight = testSet[int(len(testSet)/2):]

    setsLeft = modBFIss(goalSum, sLeft)
    setsRight = modBFIss(goalSum, sRight)

    if type(setsLeft) == int:
        return setsLeft
    if type(setsRight) == int:
        return setsRight
    else:
        countLeft = 3*len(setsLeft)*math.log(len(setsLeft)) +  2**(len(testSet)/2)               # 3*t*log(t) for sorting setsLeft + the 2^(n/2) for computing setsLeft
        countRight = 3*len(setsRight)*math.log(len(setsRight)) +  2**(len(testSet)/2)
        
        count = int(countLeft + countRight)
        pairResult = pairSum(count, goalSum, setsLeft, setsRight)
    
    return pairResult

#BODY OF CODE#
operationsBFI = []                                                     #the set size and num operations
opsForNBFI = []
opsForTestBFI = []

operationsHS = []           
opsForNHS = []
opsForTestHS = []
for i in range(4,16):                                               #num elements in random test set
    
    opsForNBFI = []
    opsForNHS = []
    for j in range(1,21):                                           #number of tests per set size
        testSet = []
        goalSet = []
        
        opsTestSetBFI = []
        opsTestSetHS = []

        for testVal in range(i):
            testSet.append(random.randint(0,10))
        
        for goalVal in range(10):
            goalSet.append(random.randint(0,100))

        for k in goalSet:    
            countBFI = BFIss(k, testSet)
            countHS = HSss(k, testSet)

            opsForTestBFI.append(countBFI)
            opsForTestHS.append(countHS)

        
        opsForNBFI.append(sum(opsForTestBFI)/len(opsForTestBFI))
        opsForNHS.append(sum(opsForTestHS)/len(opsForTestHS))

    
    operationsBFI.append(sum(opsForNBFI)/len(opsForNBFI))
    operationsHS.append(sum(opsForNHS)/len(opsForNHS))

        
setSizes = list(range(4,16))
x = np.arange(4,16,0.01)
y = 2**x
z = x*2**(x/2)
f, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2, 2, sharex=True)
ax1.plot(setSizes, operationsBFI)
ax1.set_title("BFI")

ax2.plot(setSizes, operationsHS)
ax2.set_title("HS")

ax3.plot(x, y)
ax3.set_title("2^n")

ax4.plot(x, z)
ax4.set_title("n*2^(n/2)")

plt.show()
