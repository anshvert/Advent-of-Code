import * as fs from "fs"

fs.readFile("./input.txt", 'utf-8', (err,data) => {
    const inputData = data.split("\n")
    const [map, steps] = [inputData.slice(0, inputData.indexOf("")).map((row: string) => row.split("")),
        inputData.slice(inputData.indexOf("")+1, inputData.length).join("")]
    console.log(getBoxesGPS(map, steps))
})

const getBoxesGPS = (map: string[][], steps: string): number => {
    let [initialX, initialY] = getInitialRobotPosition(map)
    const dirMap: Record<string, number[]> = { "<": [0,-1], ">": [0,1], "^": [-1,0], "v": [1,0]}
    for (let step of steps) {
        let [dx,dy] = [dirMap[step][0], dirMap[step][1]]
        let [nextX, nextY] = [initialX + dx, initialY + dy]
        switch (map[nextX][nextY]) {
            case 'O':
                let [firstEmptySpaceX, firstEmptySpaceY] = [nextX, nextY]
                while (map[firstEmptySpaceX][firstEmptySpaceY] !== '.') {
                    firstEmptySpaceX += dx
                    firstEmptySpaceY += dy
                    if (map[firstEmptySpaceX][firstEmptySpaceY] === '#') {
                        break
                    }
                }
                if (map[firstEmptySpaceX][firstEmptySpaceY] === '.') {
                    map[firstEmptySpaceX][firstEmptySpaceY] = 'O'
                    map[initialX][initialY] = '.'
                    map[nextX][nextY] = '@'
                    initialX += dx
                    initialY += dy
                }
                break
            case '.':
                [map[initialX][initialY], map[nextX][nextY]] = [map[nextX][nextY], map[initialX][initialY]]
                initialX += dx
                initialY += dy
                break
            default:
        }
    }
    // printMatrix(map)
    return getGPS(map)
}

const getGPS = (map: string[][]): number => {
    let gpsCoordinate: number = 0
    for (let i = 0; i < map.length; i++) {
        for (let j = 0; j < map[0].length; j++) {
            if (map[i][j] === 'O') {
                gpsCoordinate += 100*i + j
            }
        }
    }
    return gpsCoordinate
}

const getInitialRobotPosition = (map: string[][]): number[] => {
    let position = [0, 0]
    for (let i = 0; i < map.length; i++) {
        if (map[i].includes("@")) {
            position[0] = i
            position[1] = map[i].indexOf("@")
        }
    }
    return position
}

const printMatrix = (matrix: string[][]): void => {
    console.log(matrix.map((row) => row.join("")).join("\n"))
}