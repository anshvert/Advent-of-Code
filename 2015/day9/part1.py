"""
--- Day 9: All in a Single Night ---
Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants,
but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?

For example, given the following distances:

London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
The possible routes are therefore:

Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982
The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

What is the distance of the shortest route?
"""
from collections import defaultdict

filePath = "./input9.txt"

def travel(city,adj,vis):
    minDistance = float('inf')
    for des,dist in adj[city]:
        if des not in vis or vis[des] == 0:
            vis[des] = 1
            minDistance = min(minDistance,dist + travel(des, adj,vis))
            vis[des] = 0
    return minDistance if minDistance != float('inf') else 0

def handleTravel(file):
    distanceMap = defaultdict(list)
    minTravelDistance = float('inf')
    for route in file:
        cities,distance = route.strip().split("=")
        source,destination = cities.split("to")
        source,destination,distance = source.strip(),destination.strip(),int(distance)
        distanceMap[source].append((destination,distance))
        distanceMap[destination].append((source,distance))
    for city in distanceMap.keys():
        totalDistance = travel(city, distanceMap, {city: 1})
        minTravelDistance = min(minTravelDistance,totalDistance)
    return minTravelDistance


with open(filePath,"r") as file:
    print(handleTravel(file))



