import * as fs from "fs"
import { GetQuadrantScore, GetSafetyFactor } from "./part1";

interface GetEasterEgg {
    (robots: string[]): number
}

fs.readFile("./input.txt", 'utf-8', (err, data: string): void => {
    const robots: string[] = data.split("\n")
    console.log(getEasterEgg(robots))
})

const getEasterEgg: GetEasterEgg = (robots: string[]): number => {
    let [row, col, seconds]: [number, number, number] = [103,101,10000]
    let [minSafetyFactor, minSeconds]: [number, number] = [Infinity, -1]
    for (let second: number = 1; second <= seconds; second ++) {
        let positionMatrix: string[][] = createMatrix(row, col, '.')
        for (let robot of robots) {
            const robotPV: string[] = robot.split(" ")
            let [position, velocity]: [string, string] = [robotPV[0].split("=")[1], robotPV[1].split("=")[1]]
            let [positionX,positionY]: string[] = position.split(",").reverse()
            let [velocityX, velocityY]: string[] = velocity.split(",").reverse()
            let [newX, newY]: [number, number] = [Number(positionX) + second*parseInt(velocityX),Number(positionY) + second*parseInt(velocityY)]
            let [finalPositionX, finalPositionY]: [number, number] = [
                newX < 0 ? (row + (newX % row)) % row : newX % row,
                newY < 0 ? (col + (newY % col)) % col : newY % col
            ];
            positionMatrix[finalPositionX][finalPositionY] === '.' ? positionMatrix[finalPositionX][finalPositionY] = '1'
                : positionMatrix[finalPositionX][finalPositionY] = (parseInt(positionMatrix[finalPositionX][finalPositionY]) + 1).toString()
        }
        const safetyFactor: number = getSafetyFactor(positionMatrix)
        if (safetyFactor < minSafetyFactor) {
            minSafetyFactor = safetyFactor
            minSeconds = second
        }
    }
    return minSeconds
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
