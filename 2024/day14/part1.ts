import * as fs from "fs"

interface GetPositionMatrix {
    (robots: string[]): string[][]
}

export interface GetSafetyFactor {
    (matrix: string[][]): number
}

export interface GetQuadrantScore {
    (matrix: string[][], rowStart: number, rowEnd: number, colStart: number, colEnd: number): number
}

fs.readFile("./input.txt", 'utf-8', (err, data: string): void => {
    const robots: string[] = data.split("\n")
    const positionMatrix: string[][] = getPositionMatrix(robots)
    console.log(getSafetyFactor(positionMatrix))
})

const getPositionMatrix: GetPositionMatrix = (robots: string[]): string[][] => {
    let [row, col, seconds]: [number, number, number] = [103,101,100]
    let positionMatrix: string[][] = createMatrix(row, col, '.')
    for (let robot of robots) {
        const robotPV: string[] = robot.split(" ")
        let [position, velocity]: [string, string] = [robotPV[0].split("=")[1], robotPV[1].split("=")[1]]
        let [positionX,positionY]: string[] = position.split(",").reverse()
        let [velocityX, velocityY]: string[] = velocity.split(",").reverse()
        let [newX, newY]: [number, number] = [Number(positionX) + seconds*parseInt(velocityX),Number(positionY) + seconds*parseInt(velocityY)]
        let [finalPositionX, finalPositionY]: [number, number] = [
            newX < 0 ? (row + (newX % row)) % row : newX % row,
            newY < 0 ? (col + (newY % col)) % col : newY % col
        ];
        positionMatrix[finalPositionX][finalPositionY] === '.' ? positionMatrix[finalPositionX][finalPositionY] = '1'
            : positionMatrix[finalPositionX][finalPositionY] = (parseInt(positionMatrix[finalPositionX][finalPositionY]) + 1).toString()
    }
    return positionMatrix
}

const getSafetyFactor: GetSafetyFactor = (matrix: string[][]): number => {
    let score: number = 1
    const midRow: number = Math.floor(matrix.length / 2);
    const midCol: number = Math.floor(matrix[0].length / 2);
    score *= getQuadrantScore(matrix, 0, midRow, 0, midCol);
    score *= getQuadrantScore(matrix, 0, midRow, midCol+1, matrix[0].length);
    score *= getQuadrantScore(matrix, midRow+1, matrix.length, 0, midCol);
    score *= getQuadrantScore(matrix, midRow+1, matrix.length, midCol+1, matrix[0].length);
    return score
}

const getQuadrantScore: GetQuadrantScore = (matrix: string[][], rowStart: number, rowEnd: number, colStart: number, colEnd: number): number => {
    let score: number = 0
    for (let i: number = rowStart; i < rowEnd; i++) {
        for (let j: number = colStart; j < colEnd; j++) {
            if (matrix[i][j] !== '.') {
                score += Number(matrix[i][j])
            }
        }
    }
    return score
}

const createMatrix = (rows: number, cols: number, initialValue: string) => {
    return Array.from({ length: rows }, () => Array(cols).fill(initialValue))
}

const printMatrix = (matrix: string[][]): void => {
    console.log(matrix.map((row) => row.join("")).join("\n"))
}