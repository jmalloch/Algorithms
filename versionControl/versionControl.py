import numpy as np

def f2ModHash(string):
    """
    Takes a string and returns an interger hash value between 0 - 100 000.
    """
    a = 7
    b = 100000

    result = 0

    for ch in string:
        result = (a*result + ord(ch)) % b

    return result

def polyRollHash(string):
    """
    Takes a string and returns an interger hash value between 0 - 10^9 + 9.
    """
    p = 100
    m = 10**9 + 9

    result = 0

    for i, ch in enumerate(string):
        result += ord(ch) * p**i % m

    return result

def stringHash(string):
    return(f2ModHash(string), polyRollHash(string))

def fileHash(array):
    """
    Takes a file in the form of an array of lines and returns an equal dim array of tuples (integer result of f2modhash, integer result of polyrollhash)
    """
    for i in range(len(array)):
        array[i] = stringHash(array[i])

    return array
        
#above this point are 2 string hashing functions & 2 functions that hash lines of a file returning an array of tuples w/ structure (func1hash, func2hash), both hashing functions are re-used from lab9

def modLCS(ar1, hash1, ar2, hash2):
    """
    Takes 2 arrays of file lines and 2 arrays of tuples holding the integer hash values of the lines when put through both of the above hashing functions.
    Returns 2 1D arrays of equal length w/ each value in both arrays holding the line number of all common lines in the 2 files passed in as arrays. 
    """
    n = len(ar1)
    m = len(ar2)
    
    LCS = np.zeros((n,m), dtype = int)                      #this will be a temporary 2D array, row 0 = file1 FIRST line & col m = file 2 LAST line
   
    for i in range(n):
        for j in range(m):
            if(hash1[i] == hash2[j]):                       #compare the tuples of doubly hashed lines and only resort to comparing strings directly if both lines have equal hashed values
                if(ar1[i] == ar2[j]):
                    LCS[i][j] = 1 + LCS[i-1][j-1]
            else:
                LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
    
    #Now I'll begin traversing back through the LCS to find the lines that make up the LCS
    
    lines1 = []
    lines2 = []
    n -= 1
    m -= 1                                                  #subtracting n&m by 1 to avoid accessing an element of the numpy array that is out of bounds
    while(True):
        if(n < 0 or m < 0 or LCS[n][m] == 0 ):
            break
        
        if(n == 0 and m == 0):
            lines1.insert(0, 1)                             #this is to handle a common line such that the line in question is the 1st line of File1 and/or the 1st line of File2 
            lines2.insert(0, 1)
        elif(n == 0):
            while(LCS[n][m] != 0):                          
                m -= 1                                      
            lines1.insert(0,1)                              
            lines2.insert(0, m+2)                           #m+2 since the LCS[n][m] == 0 to break out of while loop, hence the line prior is the common line AND since the array begins at index 0..

        elif(m == 0):                                       #.. where the file begins at line one (as explain below)
            while(LCS[n][m] != 0):
                n -= 1
            lines1.insert(0, n+2)                           #n+2 for the same reason as explained above
            lines2.insert(0, 1)

        if(LCS[n][m] > LCS[n-1][m] and LCS[n][m] > LCS[n][m-1]):
            lines1.insert(0, n+1)                           # using '+1' to ensure the line numbers are paired, not the indecies of the array elements that are indexed from zero unlike lines in files
            lines2.insert(0, m+1)
            n -= 1
            m -= 1
        elif(LCS[n][m] > LCS[n-1][m]):
            m -= 1
        elif(LCS[n][m] > LCS[n][m-1]):
            n -= 1
        else:                                               #this shouldn't ever occur based on the specific lab application but was included to leave the function extensible
            n -= 1
            m -= 1
    
    return lines1, lines2
    
def fileComp(f1, name1, f2, name2):
    File1 = f1.readlines()
    File2 = f2.readlines()
    
    hash1 = fileHash(File1)
    hash2 = fileHash(File2)

    lines1, lines2 = modLCS(File1, hash1, File2, hash2)
    
    ranges1 = []
    ranges2 = []
    
    if(lines1[0] + 1 == lines1[1]):
        ranges1.append(lines1[0])
        ranges2.append(lines2[0])

    for i in range(len(lines1) - 1):
        if(lines1[i] + 1 != lines1[i+1]):
            ranges1.append(lines1[i])
            ranges2.append(lines2[i])
            ranges1.append(lines1[i+1])
            ranges2.append(lines2[i+1])
    
    if(lines1[-2] + 1 == lines1[-1]):
        ranges1.append(lines1[-1])
        ranges2.append(lines2[-1])                          #ensures that if the last 2+ common lines are subsequent lines in the initial file, then the final line is added as the end of the last range
    
    if(ranges1[0] != 1 and ranges2[0] != 1):
        print("Mismatch:\t" + name1 + " : <1 .. " + str(ranges1[0] - 1) + ">\t\t\t" + name2 + " : <1 .. " + str(ranges2[0] - 1) + ">\n")
    elif(ranges1[0] != 1):
        print("Mismatch:\t" + name1 + " : <1 .. " + str(ranges1[0] - 1) + ">\t\t\t" + name2 + " : None\n")
    elif(ranges2[0] != 1):
        print("Mismatch:\t" + name1 + " : None\t\t\t" + name2 + " : <1 .. " + str(ranges2[0] - 1) + ">\n")
    
    #above I took care of the initial output for files with uncommon first lines as this won't fit easily into the loop structure below

    for i in range(0, len(ranges1) - 1, 2):
        print("Match:\t\t" + name1 + " : <" + str(ranges1[i]) + " .. " + str(ranges1[i+1]) + ">\t\t\t" + name2 + " : <"+ str(ranges2[i]) + " .. " + str(ranges2[i+1]) + ">\n")
        
        if(i != len(ranges1) - 2):
            if(ranges1[i+1] + 1 != ranges1[i+2] and ranges2[i+1] + 1 != ranges2[i+2]):
                print("Mismatch:\t" + name1 + " : <" + str(ranges1[i+1] + 1) + " .. " + str(ranges1[i+2] - 1) + ">\t\t\t" + name2 + " : <" + str(ranges2[i+1] + 1) + " .. " + str(ranges2[i+2] - 1) + ">\n")
            elif(ranges1[i+1] + 1 != ranges1[i+2]):
                print("Mismatch:\t" + name1 + " : <" + str(ranges1[i+1] + 1) + " .. " + str(ranges1[i+2] - 1) + ">\t\t\t" + name2 + " : None\n")
            else:
                print("Mismatch:\t" + name1 + " : None\t\t\t" + name2 + " : <" + str(ranges2[i+1] + 1) + " .. " + str(ranges2[i+2] - 1) + ">\n")
    
textName1 = input("What is the name of the first file: ")
File1 = open(textName1, "r")

textName2 = input("What is the name of the second file: ")
File2 = open(textName2, "r")

fileComp(File1, textName1, File2, textName2)

File1.close()
File2.close()
