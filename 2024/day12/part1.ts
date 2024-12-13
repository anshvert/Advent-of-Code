import * as fs from 'fs'

export interface GetFencingCost {
    (gardenPlot: string[]): number
}

export interface TravelGarden {
    (position: number[], gardenPlot: string[], visited: Set<string>): [number, number]
}

interface GetPerimeter {
    (coordinates: number[], gardenPlot: string[]): number
}

export interface ValidCoordinate {
    (coordinate: number[], matrix: string[]): boolean
}

fs.readFile("./input.txt", 'utf-8', (_, data) => {
    const gardenPlot: string[] = data.split("\n")
    console.log(getFencingCost(gardenPlot))
})

const getFencingCost: GetFencingCost  = (gardenPlot: string[]): number => {
    const visited: Set<string> = new Set()
    let totalCost: number = 0

    for (let rowIndex: number = 0; rowIndex < gardenPlot.length; rowIndex ++) {
        for (let colIndex: number = 0; colIndex < gardenPlot[0].length; colIndex ++) {
            if (visited.has(JSON.stringify([rowIndex, colIndex]))) {
                continue
            }
            const [area, perimeter]: [number, number] = travelGarden([rowIndex, colIndex], gardenPlot, visited)
            totalCost += area * perimeter
        }
    }
    return totalCost
}

const travelGarden: TravelGarden = (position: number[], gardenPlot: string[], visited: Set<string>): [number, number] => {
    let [x,y]: number[] = position
    let [area, perimeter]: number[] = [0,0]
    const coords: number[][] = [[0,1],[0,-1],[1,0],[-1,0]]
    visited.add(JSON.stringify(position))
    for (let coordinate: number = 0; coordinate < coords.length; coordinate ++) {
        const newX: number = x + coords[coordinate][0]
        const newY: number = y + coords[coordinate][1]
        if (validCoordinate([newX,newY], gardenPlot) && gardenPlot[newX][newY] === gardenPlot[x][y] && !visited.has(JSON.stringify([newX, newY]))) {
            let [newArea, newPerimeter] = travelGarden([newX, newY], gardenPlot, visited)
            area += newArea
            perimeter += newPerimeter
        }
    }
    return [area + 1, perimeter + getPerimeter([x,y], gardenPlot)]
}

const getPerimeter: GetPerimeter = (coordinates: number[], gardenPlot: string[]): number => {
    let [x,y]: number[] = coordinates
    const coords: number[][] = [[0,1],[0,-1],[1,0],[-1,0]]
    let perimeter: number = 0
    for (let coordinate: number = 0; coordinate < coords.length; coordinate ++) {
        const newX: number = x + coords[coordinate][0]
        const newY: number = y + coords[coordinate][1]
        if (!validCoordinate([newX,newY], gardenPlot) || gardenPlot[newX][newY] !== gardenPlot[x][y]) {
            perimeter += 1
        }
    }
    return perimeter
}

const validCoordinate: ValidCoordinate = (coordinate: number[], matrix: string[]): boolean => {
    return (coordinate[0] >= 0 && coordinate[0] < matrix.length) && (coordinate[1] >= 0 && coordinate[1] < matrix.length);
}