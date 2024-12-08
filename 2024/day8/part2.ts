import * as fs from "fs"
import { CountAntiNodes, ValidCoordinate } from "./part1";

interface DebugMatrix {
    (matrix: string[][], antiNodes: Set<string>): void
}

fs.readFile("./input.txt", "utf8", (err, data: string): void => {
    if (err) throw err;
    const matrix: string[] = data.split("\n")
    const antennaData = new Map<string, number[][]>()
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[i].length; j++) {
            if (matrix[i][j] !== '.') {
                antennaData.set(matrix[i][j], antennaData.get(matrix[i][j])?.concat([[i,j]]) || [[i,j]]);
            }
        }
    }
    console.log(countAntiNodes(matrix,antennaData))
})

const countAntiNodes: CountAntiNodes = (matrix: string[], antennaData: Map<string, number[][]>): number => {
    const antiNodeSet = new Set<string>()
    antennaData.forEach((value: number[][]) => {
        for (let i = 0; i < value.length; i++) {
            for (let j = i+1; j < value.length; j++) {
                let cordMultiple: number = 1
                antiNodeSet.add(JSON.stringify(value[i]))
                antiNodeSet.add(JSON.stringify(value[j]))
                while (1) {
                    const [a1C,a2C] = [value[i], value[j]]
                    const [xDiff, yDiff] = [(a1C[0] - a2C[0]) * cordMultiple, (a1C[1] - a2C[1]) * cordMultiple]
                    const [atn1,atn2] = [[a1C[0] + xDiff, a1C[1] + yDiff],[a2C[0] - xDiff, a2C[1] - yDiff]]
                    const validAtn1 = validCoordinate(matrix, atn1)
                    const validAtn2 = validCoordinate(matrix, atn2)
                    if (validAtn1) {
                        antiNodeSet.add(JSON.stringify(atn1))
                    } if (validAtn2) {
                        antiNodeSet.add(JSON.stringify(atn2))
                    }
                    if (!validAtn1 && !validAtn2) {
                        break
                    } else {
                        cordMultiple += 1
                    }
                }
            }
        }
    })
    debugMatrix(matrix.map((row) => row.split("")), antiNodeSet)
    return antiNodeSet.size
}

const validCoordinate: ValidCoordinate = (matrix: string[], coordinate: number[]): boolean => {
    return (coordinate[0] >= 0 && coordinate[0] < matrix.length) && (coordinate[1] >= 0 && coordinate[1] < matrix.length);
}

const debugMatrix: DebugMatrix = (matrix: string[][], antiNodes: Set<string>) => {
    antiNodes.forEach(antiNode => {
        const cords = antiNode.slice(1, antiNode.length -1 ).split(",").map((cord) => parseInt(cord))
        matrix[cords[0]][cords[1]] === "." ? matrix[cords[0]][cords[1]] = '#' : []
    })
    console.log(matrix.map((row) => row.join("")).join("\n"))
}