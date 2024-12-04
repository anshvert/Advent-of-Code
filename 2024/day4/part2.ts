import * as fs from 'fs'

interface ValidMAS {
    (i: number, j: number, puzzleMatrix: string[]): boolean
}

interface ValidCoords {
    (x: number, y: number, matrix: string[]): boolean
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
            if (puzzleMatrix[i][j] === "A") {
                if (validMAS(i,j,puzzleMatrix)) {
                    ans += 1
                }
            }
        }
    }
    console.log(ans)
})

const validMAS: ValidMAS = (i: number,j: number,puzzleMatrix: string[]): boolean => {
    if (validCoords(i, j, puzzleMatrix)) {
        const first: boolean = (puzzleMatrix[i-1][j+1] !== puzzleMatrix[i+1][j-1])
            && (puzzleMatrix[i-1][j+1] === "M" || puzzleMatrix[i-1][j+1] === "S")
            && (puzzleMatrix[i+1][j-1] === "M" || puzzleMatrix[i+1][j-1] === "S")
        const second: boolean = (puzzleMatrix[i-1][j-1] !== puzzleMatrix[i+1][j+1])
            && (puzzleMatrix[i-1][j-1] === "M" || puzzleMatrix[i-1][j-1] === "S")
            && (puzzleMatrix[i+1][j+1] === "M" || puzzleMatrix[i+1][j+1] === "S")
        return first && second
    }
    return false
}

const validCoords: ValidCoords = (x: number, y: number, matrix: string[]): boolean => {
    return (x >= 1 && x < matrix.length - 1) && (y >= 1 && y < matrix[0].length - 1);
}
