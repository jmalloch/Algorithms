from heapq import heappush, heappop, heapify
import urllib.request
import numpy as np
import string

class Node:
    def __init__(self, huffCode, nodeCode):
            self.code = nodeCode
            self.char = huffCode[nodeCode]
            
            self.left = __init__(huffCode, '0' + nodeCode)
            self.right = __init__(huffCode, '1' + nodeCode)

urllib.request.urlretrieve(url = "http://sites.cs.queensu.ca/courses/cisc365/Labs/Week%207%20and%20Week%208/File1ASCII.txt", filename = "fileOne.txt")
urllib.request.urlretrieve(url = "http://sites.cs.queensu.ca/courses/cisc365/Labs/Week%207%20and%20Week%208/File2ASCII.txt", filename = "fileTwo.txt")
fileOne = open("fileOne.txt")
one = fileOne.read()
fileOne.close()
fileTwo = open("fileTwo.txt")
two = fileTwo.read()
fileTwo.close()

def codeBuild(inputFile):
    """
    Create Huffman code for the given file, opened in python
    """
    printables = string.printable
    printables = printables.replace('\t','')
    printables = printables.replace('\r','')        #creating a string of all the chars deemed 'printable' for this lab
    printables = printables.replace('\x0b','')
    printables = printables.replace('\x0c','')
    
    freqs = {}
    for char in printables:
        freqs[char] = 0
    for ch in inputFile:
        if ch in freqs:
            freqs[ch] += 1
    
    intFreqs={}
    for key in freqs.keys():
        intFreqs[ord(key)] = freqs[key]
    
    heapFreqs = [[freq, [char, ""]] for char, freq in intFreqs.items()]
    heapify(heapFreqs)
    while len(heapFreqs) >= 2:
        min1 = heappop(heapFreqs)
        for tup in min1[1:]:
            tup[1] = '0' + tup[1]
        
        min2 = heappop(heapFreqs)
        for tup in min2[1:]:
            tup[1] = '1' + tup[1]

        heappush(heapFreqs, [min1[0]+min2[0]] + min1[1:] + min2[1:])

    huffman = dict(sorted(heappop(heapFreqs)[1:], key = lambda x: (x[0])))
    
    outputFile = open("huffCode.txt", "x")
    for char, code in huffman.items():
        outputFile.write(str(char) + "\t" + str(code) + "\n")
    outputFile.close()
    
    return huffman

def encode(huffman):
    """
    Takes user input for the name of a textfile, encodes it with a huffman code (hard coded into the function because I didn't see a reason to take it as a param, OUTPUTS an encoded .txt file
    """
    textName = input("What is the name of the .txt file (do NOT include .txt): ")
    textFile = open(textName + ".txt", "r")
    text = textFile.read()
    textFile.close()
    codedText = open(textName + "Coded.txt", "x")
    
    for char in text:
        codedText.write(huffman[ord(char)])
    
    codedText.close()

def decode(huffman):
    """
    Takes user input for the name of a textfile, encodes it with a huffman code (hard coded into the function because I didn't see a reason to take it as a param, OUTPUTS an encoded .txt file
    """
    decoder = {}
    for char, code in huffman.items():
        decoder[code] = char                             #this huffman code dictionary is constructed oppositely from the version in code builder, key = bit code & value = ascii char
    
    textName = input("What is the name of the .txt file (do NOT include .txt): ")
    textFile = open(textName + ".txt", "r")
    text = textFile.read()
    textFile.close()
    
    outputFile = open(textName + "Decoded.txt", "x")
    
    subset = []
    sBit = 0
    eBit = 0
    
    while eBit < len(text):
        string = ""
        string = string.join(subset)                    #brings together current subset of bits into a string to check for a match in decoder
        
        if sBit == eBit:
            subset = [text[sBit], text[eBit+1]]
            eBit += 1

        if string in decoder.keys():
            outputFile.write(chr(decoder[string]))
            eBit += 1
            sBit = eBit
            if eBit+1 < len(text):
                subset = [text[sBit], text[eBit+1]]
                eBit += 1
        
        else:
            eBit += 1
            subset.append(text[eBit])

    outputFile.close()





huffCode = codeBuild(one)
#encode(huffCode)
decode(huffCode)

