import os
import numpy as np
import urllib.request

urllib.request.urlretrieve(url = "http://sites.cs.queensu.ca/courses/cisc365/Labs/Week%201/Dijkstra_Data_6.txt", filename = "Dijkstra_Data_6.txt")
urllib.request.urlretrieve(url = "http://sites.cs.queensu.ca/courses/cisc365/Labs/Week%201/Dijkstra_Data_100.txt", filename = "Dijkstra_Data_100.txt")
urllib.request.urlretrieve(url = "http://sites.cs.queensu.ca/courses/cisc365/Labs/Week%201/Dijkstra_Data_200.txt", filename = "Dijkstra_Data_200.txt")
urllib.request.urlretrieve(url = "http://sites.cs.queensu.ca/courses/cisc365/Labs/Week%201/Dijkstra_Data_400.txt", filename = "Dijkstra_Data_400.txt")
urllib.request.urlretrieve(url = "http://sites.cs.queensu.ca/courses/cisc365/Labs/Week%201/Dijkstra_Data_800.txt", filename = "Dijkstra_Data_800.txt")
urllib.request.urlretrieve(url = "http://sites.cs.queensu.ca/courses/cisc365/Labs/Week%201/Dijkstra_Data_1600.txt", filename = "Dijkstra_Data_1600.txt")

six =  np.loadtxt(fname = "/home/jack/Documents/School/Y3/CMPE365/Lab1/Dijkstra_Data_6.txt", dtype = int, skiprows = 1)
oh =  np.loadtxt(fname = "/home/jack/Documents/School/Y3/CMPE365/Lab1/Dijkstra_Data_100.txt", dtype = int, skiprows = 1)
th = np.loadtxt(fname = "/home/jack/Documents/School/Y3/CMPE365/Lab1/Dijkstra_Data_200.txt", dtype = int, skiprows = 1)
fh = np.loadtxt(fname = "/home/jack/Documents/School/Y3/CMPE365/Lab1/Dijkstra_Data_400.txt", dtype = int, skiprows = 1)
eh = np.loadtxt(fname = "/home/jack/Documents/School/Y3/CMPE365/Lab1/Dijkstra_Data_800.txt", dtype = int, skiprows = 1)
sh = np.loadtxt(fname = "/home/jack/Documents/School/Y3/CMPE365/Lab1/Dijkstra_Data_1600.txt", dtype = int, skiprows = 1)

d = {
        6 : six,
        100 : oh,
        200 : th,
        400 : fh,
        800 : eh,
        1600 : sh,
    }

#numVert = int(input("Enter the number of vertecies desired: "))
for numVert in d:

    data = d[numVert]

    cost = np.zeros(numVert, dtype = float)
    estimate = np.zeros(numVert, dtype = float)

    reached = np.zeros(numVert, dtype = bool)
    candidate = np.zeros(numVert, dtype = bool)

    reached[0] = True
    cost[0] = 0


    for x in range(1,numVert):
        if data[0,x] != 0:
            candidate[x] = True
            estimate[x] = data[0,x]
        else:
            candidate[x] = False
            estimate[x] = float('inf')
    
    while np.all(reached) != True:
        bestCandid = float('inf')
        for x in range(numVert):
            if (candidate[x] == True) and (estimate[x] < bestCandid):
                v = x
                bestCandid = estimate[x]

        cost[v] = estimate[v]
        reached[v] = True
        candidate[v] = False

        for y in range(numVert):
            if data[v][y] != 0 and reached[y] == False:
                if cost[v] + data[v][y] < estimate[y]:
                    candidate[y] = True
                    estimate[y] = cost[v] + data[v][y]
    print("DataSet - " + str(numVert) + ": Vertex - " +  str(np.argmax(cost)) + ", Cost = " + str(np.amax(cost)))

