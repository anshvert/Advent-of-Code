import * as fs from "fs"

export interface CountAntiNodes {
    (matrix: string[], antennaData: Map<string, number[][]>): number
}

export interface ValidCoordinate {
    (matrix: string[], coordinate: number[]): boolean
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
                const [a1C,a2C] = [value[i], value[j]]
                const [xDiff, yDiff] = [a1C[0] - a2C[0], a1C[1] - a2C[1]]
                const [atn1,atn2] = [[a1C[0] + xDiff, a1C[1] + yDiff],[a2C[0] - xDiff, a2C[1] - yDiff]]
                validCoordinate(matrix, atn1) ? antiNodeSet.add(JSON.stringify(atn1)) : []
                validCoordinate(matrix, atn2) ? antiNodeSet.add(JSON.stringify(atn2)) : []
            }
        }
    })
    return antiNodeSet.size
}

const validCoordinate: ValidCoordinate = (matrix: string[], coordinate: number[]): boolean => {
    return (coordinate[0] >= 0 && coordinate[0] < matrix.length) && (coordinate[1] >= 0 && coordinate[1] < matrix.length);
}
