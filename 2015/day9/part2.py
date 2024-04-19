"""
--- Part Two ---
The next year, just to show off, Santa decides to take the route with the longest distance instead.

He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.

For example, given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.

What is the distance of the longest route?
"""


from collections import defaultdict

filePath = "./input9.txt"

def travel(city,adj,vis):
    maxDistance = 0
    for des,dist in adj[city]:
        if des not in vis or vis[des] == 0:
            vis[des] = 1
            maxDistance = max(maxDistance,dist + travel(des, adj,vis))
            vis[des] = 0
    return maxDistance if maxDistance != float('inf') else 0

def handleTravel(file):
    distanceMap = defaultdict(list)
    maxTravelDistance = 0
    for route in file:
        cities,distance = route.strip().split("=")
        source,destination = cities.split("to")
        source,destination,distance = source.strip(),destination.strip(),int(distance)
        distanceMap[source].append((destination,distance))
        distanceMap[destination].append((source,distance))
    for city in distanceMap.keys():
        totalDistance = travel(city, distanceMap, {city: 1})
        maxTravelDistance = max(maxTravelDistance,totalDistance)
    return maxTravelDistance


with open(filePath,"r") as file:
    print(handleTravel(file))