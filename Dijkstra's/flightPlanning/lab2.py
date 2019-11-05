import os
import numpy as np
import urllib.request

urllib.request.urlretrieve(url = "http://sites.cs.queensu.ca/courses/cisc365/Labs/Week%202/2019_Lab_2_flights_test_data.txt", filename = "2019_Lab_2_flights_test_data4.txt")
urllib.request.urlretrieve(url = "http://sites.cs.queensu.ca/courses/cisc365/Labs/Week%202/2019_Lab_2_flights_real_data.txt", filename = "2019_Lab_2_flights_real_data200.txt")

four =  np.loadtxt(fname = "/home/jack/Documents/School/Y3/CMPE365/Lab2/2019_Lab_2_flights_test_data4.txt", dtype = int, skiprows = 1)
twoHundred =  np.loadtxt(fname = "/home/jack/Documents/School/Y3/CMPE365/Lab2/2019_Lab_2_flights_real_data200.txt", dtype = int, skiprows = 1)

data = twoHundred

def findSubset(startingCity, arrivalTime = 0):
    """
    This returns a np array of all flights departing from the startingCity, excluding any with a departure time less than or equal to 'arrivalTime'.
    """
    cityStart = 0
    cityEnd = 0
    cityNum = 0


    while cityNum != startingCity+1:
        if cityNum != startingCity:
            cityStart += 1
        cityEnd += 1
        if cityEnd < np.size(data, 0):
            cityNum = data[cityEnd,0]
        else:
            cityNum = startingCity + 1
    dataSubset = data[range(cityStart, cityEnd),:]
    rowCount = 0
    for flight in dataSubset:
        if flight[2] <= arrivalTime:
            dataSubset = np.delete(dataSubset, rowCount, axis = 0)
        else:    
            rowCount += 1
    return dataSubset

sCity = int(input("Enter the starting city: "))
dCity = int(input("Enter the destination: "))


#Column values: Candidate City, Arrival time in city, previous city, TEMPORARY Arrival time(used to find next search) - if infinite then the candidate has been searched
candidates = np.array([[sCity, 0, np.inf, 0]])

while dCity not in candidates[:,0]:
    nextSearch = candidates[np.argmin(candidates[:,3]),:]
    candidates[np.argmin(candidates[:,3]),3] = np.inf
    dataSubset = findSubset(nextSearch[0], nextSearch[1])
    for flight in dataSubset:
        if flight[1] in candidates[:,0]:
            duplicateCity = int(np.argwhere(candidates[:,0] == flight[1]))
            if flight[3] < candidates[duplicateCity,1]:
                candidates = np.delete(candidates, duplicateCity, 0)
                candidates = np.vstack((candidates, np.array([flight[1], flight[3], flight[0], flight[3]])))
        else:
            candidates = np.vstack((candidates, np.array([flight[1], flight[3], flight[0], flight[3]])))

dCityCandid = candidates[np.argwhere(candidates[:,0] == dCity),:].flatten()
for city in candidates:
    if city[1] < dCityCandid[1]:
        dataSubset = findSubset(city[0], city[1])
    
        for flight in dataSubset:
            if flight[1] in candidates[:,0]:
                duplicateCity = int(np.argwhere(candidates[:,0] == flight[1]))
                if flight[3] < candidates[duplicateCity,1]:
                    candidates = np.delete(candidates, duplicateCity, 0)
                    candidates = np.vstack((candidates, np.array([flight[1], flight[3], flight[0], flight[3]])))
            else:
                candidates = np.vstack((candidates, np.array([flight[1], flight[3], flight[0], flight[3]])))


optimalRoute = [dCity]

dCityCandid = candidates[np.argwhere(candidates[:,0] == dCity),:].flatten()
pastCity = dCityCandid[2]

while pastCity < np.inf:
    optimalRoute.insert(0, pastCity)
    pastCity = candidates[np.argwhere(candidates[:,0] == pastCity),:].flatten()[2]

print("\nOptimal route from " + str(sCity)+ " to " + str(dCity) + "\n")

for i in range(1,len(optimalRoute)):
    print("Fly from " + str(int(optimalRoute[i-1])) + " to " + str(int(optimalRoute[i])))

print("\nArrive at " + str(dCity) + " at time " + str(int(dCityCandid[1])))



