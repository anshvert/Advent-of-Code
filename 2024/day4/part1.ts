import * as fs from 'fs'

interface ValidXMAS {
    (i: number, j: number, puzzleMatrix: string[]): number
}

interface ValidCoords {
    (x: number, y: number, matrix: string[]): boolean
}

interface GetString {
    (initialPoint: number[], x: number, y: number, matrix: string[]): string
}

fs.readFile('./input.txt', 'utf8', (err: unknown, data: string): void => {
    if (err) {
        console.log(err)
        return
    }
    let ans: number = 0
    const puzzleMatrix: string[] = data.split("\n")
    for (let i: number = 0; i < puzzleMatrix.length; i++) {
        for (let j: number = 0; j < puzzleMatrix[i].length; j++) {
            if (puzzleMatrix[i][j] === "X") {
                ans += validXMAS(i,j,puzzleMatrix)
            }
        }
    }
    console.log(ans)
})

const validXMAS: ValidXMAS = (x: number,y: number,matrix: string[]): number => {
    const dirs: number[][] = [[0,1],[0,-1],[1,0],[-1,0],[-1,-1],[1,-1],[-1,1],[1,1]]
    let count: number = 0
    for (let i: number = 0; i < dirs.length; i++) {
        const newString: string = getString(dirs[i], x, y, matrix)
        if (newString === "XMAS") {
            count += 1
        }
    }
    return count
}

const getString: GetString = (initialPoint: number[], x: number, y: number, matrix: string[]): string => {
    let string: string = ""
    let xx: number = x
    let yy: number = y
    for (let i: number = 0; i < 4; i++) {
        if (validCoords(xx,yy,matrix)) {
            string += matrix[xx][yy]
            xx += initialPoint[0]
            yy += initialPoint[1]
        } else {
            return string
        }
    }
    return string
}

const validCoords: ValidCoords = (x: number, y: number, matrix: string[]): boolean => {
    return (x >= 0 && x < matrix.length) && (y >= 0 && y < matrix[0].length);
}
