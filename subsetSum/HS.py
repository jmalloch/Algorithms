import copy
import math
class Set:

    #attributes for set/subset are a list of integer elements and their interger summation
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
        return "\nelements = " + str(self.elements) + ", sum = " + str(self.setSum)                 #this was used whilst writing the code & can be used to check correctness

    def sumSet(self):
        self.setSum = sum(self.elements)

def modBFIss(goalSum, testSet = []):
    """
    Sums all possible subsets checking for sumGoal. If found, prints subSet with sum = sumGoal and returns TRUE, otherwise returns all subsets sorted by sum.
    """
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
                print(str(goalSum) + " is the sum of set: ")
                print(newSet.elements)
                return True
        subSets = copy.deepcopy(newSubSets)
    return sorted(subSets, key = lambda x: x.setSum)

def pairSum(goalSum, setA = [], setB = []):
    """
    Checks summation of pairs of subsets or elements for goalSum value. Returns indA and indB as a list if goalSum is the sum of 2 elements, otherwise returns FALSE.
    """
    indA = 0
    indB = len(setB) - 1
    while indA < len(setA) and indB >= 1:
        val = setA[indA].setSum + setB[indB].setSum
        if val == goalSum:
            return [indA, indB]
        elif val < goalSum:
            indA+=1
        else:
            indB-=1
    return False

def HSss(goalSum, testSet =[]):
    """
    Sums all possible subsets checking for sumGoal. If found, returns STRING of subSet with sum = sumGoal, otherwise returns STRING failure statement.
    """
    sLeft = testSet[:int(len(testSet)/2)]
    sRight = testSet[int(len(testSet)/2):]
    
    setsLeft = modBFIss(goalSum, sLeft)
    setsRight = modBFIss(goalSum, sRight)

    #if setsLeft == True or setsRight == True:
    if type(setsLeft) == int: 
        return setsLeft
    elif type(setsRight) == int:
        return setsRight
    else:
        pairResult = pairSum(goalSum, setsLeft, setsRight)
        
        if pairResult == False:
            print("No subsets sum to the target value")

        else:
            print(str(goalSum) + " is the sum of set:")
            print(setsLeft[pairResult[0]].elements + setsRight[pairResult[1]].elements)
#BODY OF CODE#

goal = 41
testSet = [1,2,3,4,5,6,7,8,9]
print("Test set = " + str(testSet))
print("Goal: " + str(goal))

count = HSss(goal, testSet)
