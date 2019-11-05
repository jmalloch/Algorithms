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
            
            if newSet.setSum == goalSum:
                print(str(goalSum) + " is the sum of set: ")
                print(str(newSet.elements))
                return True
        subSets = copy.deepcopy(newSubSets)
    print("No subset sums to the target value")

#BODY OF CODE#
testSet = [1,2,3,4,5,6,7]
goal = 26
print("Test set: " + str(testSet) + "   Goal: " + str(goal))
BFIss(goal, testSet)

