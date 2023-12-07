from typing import *
filePath = "inputs/day5.txt"

def getData(fileInput) -> List[str]:
    data = []
    for text in fileInput:
        if len(text) != 1:
            data.append(text.rstrip("\n"))
    return data

def updateMap(mp,key,val,rlen):
    mp[(key,key+rlen)] = val

def getMapping(dic,mapMat,mapIndex):
    cMapsIndex = mapIndex + 1
    while cMapsIndex < len(mapMat) and mapMat[cMapsIndex][-1] != ":":
        cMaps = mapMat[cMapsIndex]
        soil, seed, rangeLength = cMaps.split(" ")
        updateMap(dic, int(seed), int(soil), int(rangeLength))
        cMapsIndex += 1

def findSeedLocation(seedNum: int, mapArr, mapIndex) -> int:
    if mapIndex == len(mapArr):
        return seedNum

    updatedSeedNum = seedNum
    for i,j in mapArr[mapIndex].keys():
        if i <= seedNum <= j:
            updatedSeedNum = mapArr[mapIndex][(i,j)] + seedNum - i
            break
    return findSeedLocation(updatedSeedNum, mapArr, mapIndex + 1)

def closeLocation(seedMat):
    seeds = []
    seedSoil,soilFert,fertWater,waterLight,lightTemp,tempHum,humLocation = dict(),dict(),dict(),dict(),dict(),dict(),dict()
    mapsArray = [seedSoil,soilFert,fertWater,waterLight,lightTemp,tempHum,humLocation]
    for ind,seedMap in enumerate(seedMat):
        if seedMap == "seed-to-soil map:":
            getMapping(seedSoil,seedMat,ind)
        elif seedMap == "soil-to-fertilizer map:":
            getMapping(soilFert,seedMat,ind)
        elif seedMap == "fertilizer-to-water map:":
            getMapping(fertWater,seedMat,ind)
        elif seedMap == "water-to-light map:":
            getMapping(waterLight,seedMat,ind)
        elif seedMap == "light-to-temperature map:":
            getMapping(lightTemp,seedMat,ind)
        elif seedMap == "temperature-to-humidity map:":
            getMapping(tempHum,seedMat,ind)
        elif seedMap == "humidity-to-location map:":
            getMapping(humLocation,seedMat,ind)
        elif seedMap[:5] == "seeds":
            colonIndex = seedMap.index(":")
            seeds = seedMap[colonIndex+2:].split(" ")

    minLocation = float("inf")
    #print(seedSoil,soilFert,fertWater,waterLight,lightTemp,tempHum,humLocation)
    for i in range(0,len(seeds),2):
        for seed in range(int(seeds[i]),int(seeds[i]) + int(seeds[i+1])):
            minLocation = min(minLocation,findSeedLocation(int(seed),mapsArray,0))
    return minLocation

with open(filePath,"r") as file:
    seedData = getData(file)
    print(closeLocation(seedData))