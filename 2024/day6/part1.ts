import * as fs from "fs"

interface FindGuard {
    (matrix: string[]): number[]
}
interface SimulateGuard {
    (matrix: string[], currentPos: number[], visited: Set<string>, dir: number[]): void
}

fs.readFile("./input.txt", "utf8", (err, data: string): void => {
    if (err) throw err;
    const matrix: string[] = data.split("\n")
    const visited = new Set<string>()
    const guardCoords: number[] = findGuard(matrix)
    visited.add(JSON.stringify(guardCoords))
    simulateGuardIterative(matrix, guardCoords, visited, [-1,0])
})

const findGuard: FindGuard = (matrix: string[]): number[] => {
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

const simulateGuard: SimulateGuard = (matrix: string[], currentPos: number[], visited: Set<string>, dir: number[]) => {
    let [x,y] = currentPos
    const nextX: number = x + dir[0]
    const nextY: number = y + dir[1]
    if ((nextX >= 0 && nextX < matrix.length) && (nextY >= 0 && nextY < matrix[0].length)) {
        if (matrix[nextX][nextY] === "#") {
            const [rotatedX, rotatedY] = [x + dir[1], y-dir[0]]
            visited.add(JSON.stringify([rotatedX, rotatedY]))
            simulateGuard(matrix, [rotatedX,rotatedY], visited,[dir[1],-dir[0]])
        } else {
            visited.add(JSON.stringify([nextX, nextY]))
            simulateGuard(matrix, [nextX, nextY], visited,dir)
        }
    } else {
        console.log(visited.size)
        return
    }
}

const simulateGuardIterative: SimulateGuard = (matrix: string[], currentPos: number[], visited: Set<string>, dir: number[]) => {
    let [x,y] = currentPos
    let [dx,dy] = dir
    while (true) {
        visited.add(JSON.stringify([x,y]))
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
    console.log(visited.size)
}
