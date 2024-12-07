import * as fs from "fs"

interface FindGuard {
    (matrix: string[][]): number[]
}
interface SimulateGuard {
    (matrix: string[][], currentPos: number[], visited: Set<string>, dir: number[]): boolean
}
interface TimeParadox {
    (matrix: string[][], currentPos: number[], visited: Set<string>, dir: number[]): number
}

fs.readFile("./input.txt", "utf8", (err, data): void => {
    if (err) throw err;
    let matrix: string[][] = data.split("\n").map((row: string) => row.split(""))
    const visited = new Set<string>()
    const guardCoords: number[] = findGuard(matrix)
    console.log(timeParadox(matrix, guardCoords, visited, [-1,0]))
})

const findGuard: FindGuard = (matrix: string[][]): number[] => {
    let x: number = 0
    let y: number = 0

    for (let row of matrix) {
        const indexOfGuard = row.indexOf("^")
        if (indexOfGuard !== -1) {
            y = indexOfGuard
            x = matrix.indexOf(row)
        }
    }
    return [x,y]
}

const simulateGuard: SimulateGuard = (matrix: string[][], currentPos: number[], visited: Set<string>, dir: number[]): boolean => {
    let [x,y] = currentPos
    let [dx,dy] = dir
    const haveBeenHereBefore: Set<string> = new Set()
    while (true) {
        if (haveBeenHereBefore.has(JSON.stringify([x,y]) + JSON.stringify([dx,dy]))) {
            return true
        }
        visited.add(JSON.stringify([x,y]))
        haveBeenHereBefore.add(JSON.stringify([x,y]) + JSON.stringify([dx,dy]))
        const nextX: number = x + dx
        const nextY: number = y + dy
        if ((nextX >= 0 && nextX < matrix.length) && (nextY >= 0 && nextY < matrix[0].length)) {
            if (matrix[nextX][nextY] === "#") {
                [dx,dy] = [dy,-dx]
            } else {
                [x,y] = [x + dx, y + dy]
            }
        } else {
            break
        }
    }
    return false
}

const timeParadox: TimeParadox = (matrix: string[][], currentPos: number[], visited: Set<string>, dir: number[]): number => {
    let numObstacles: number = 0
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[i].length; j++) {
            if (matrix[i][j] === ".") {
                matrix[i][j] = '#' // made an obstacle
                if (simulateGuard(matrix, currentPos, visited, dir)) {
                    numObstacles += 1
                }
                matrix[i][j] = '.' // remove obstacle
            }
        }
    }
    return numObstacles
}
