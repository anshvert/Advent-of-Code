import * as fs from 'fs'
import { GetFencingCost, TravelGarden, ValidCoordinate } from "./part1";

fs.readFile("./input.txt", 'utf-8', (_, data: string): void => {
    const gardenPlot: string[] = data.split("\n")
    console.log(getFencingCost(gardenPlot))
})

const getFencingCost: GetFencingCost = (gardenPlot: string[]): number => {
    const visited: Set<string> = new Set()
    let totalCost: number = 0

    for (let rowIndex: number = 0; rowIndex < gardenPlot.length; rowIndex ++) {
        for (let colIndex: number = 0; colIndex < gardenPlot[0].length; colIndex ++) {
            if (visited.has(JSON.stringify([rowIndex, colIndex]))) {
                continue
            }
            const [area, sides]: [number, number] = travelGarden([rowIndex, colIndex], gardenPlot, visited)
            totalCost += area * sides
        }
    }
    return totalCost
}

const travelGarden: TravelGarden = (position: number[], gardenPlot: string[], visited: Set<string>): [number, number] => {
    let [x,y]: number[] = position
    let [area, sides]: number[] = [0,0]
    const coords: number[][] = [[0,1],[0,-1],[1,0],[-1,0]]
    visited.add(JSON.stringify(position))
    for (let coordinate: number = 0; coordinate < coords.length; coordinate ++) {
        const newX: number = x + coords[coordinate][0]
        const newY: number = y + coords[coordinate][1]
        if (validCoordinate([newX,newY], gardenPlot) && gardenPlot[newX][newY] === gardenPlot[x][y] && !visited.has(JSON.stringify([newX, newY]))) {
            let [newArea, newSides]: [number, number] = travelGarden([newX, newY], gardenPlot, visited)
            area += newArea
            sides += newSides
        }
    }
    sides += getSides([x,y], gardenPlot)
    return [area + 1, sides]
}

const getSides = (coordinates: number[], gardenPlot: string[]): number => {
    let [x,y]: number[] = coordinates
    const coords: number[][] = [[0,1],[0,-1],[1,0],[-1,0]]
    let sides: number = 0
    for (let coordinate: number = 0; coordinate < coords.length; coordinate ++) {
        const dx: number = coords[coordinate][0]
        const dy: number = coords[coordinate][1]
        const newX: number = x + dx
        const newY: number = y + dy
        if (!validCoordinate([newX,newY], gardenPlot) || gardenPlot[newX][newY] !== gardenPlot[x][y]) {
            const leftContinuationX: number = dy != 0 ? x - dy : x
            const leftContinuationY: number = dx != 0 ? y + dx : y
            const leftContinuationNewX: number = leftContinuationX + dx
            const leftContinuationNewY: number = leftContinuationY + dy
            if (!(gardenPlot[x][y] === getMockCoordinate([leftContinuationX, leftContinuationY], gardenPlot))
                || (getMockCoordinate([leftContinuationNewX, leftContinuationNewY], gardenPlot) === gardenPlot[x][y])) {
                sides += 1
            }
        }
    }
    return sides
}

const validCoordinate: ValidCoordinate = (coordinate: number[], matrix: string[]): boolean => {
    return (coordinate[0] >= 0 && coordinate[0] < matrix.length) && (coordinate[1] >= 0 && coordinate[1] < matrix.length);
}

const getMockCoordinate = (pos: number[], grid: string[]): string => {
    try {
        return grid[pos[0]][pos[1]]
    } catch (err) {
        return '7' // thala for a reason !
    }
}