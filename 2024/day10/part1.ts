import * as fs from "fs"

export interface GetAllTrailHeadScore {
    (topographicMap: number[][]): number
}

export interface GetTRailScore {
    (i: number, j: number, map: number[][], visited: Set<string>): number
}

fs.readFile("./input.txt", 'utf-8', (err, data: string) => {
    if (err) throw err
    const topographicMap: string[] = data.split("\n")
    console.log(getAllTrailHeadScore(topographicMap.map((x: string) => x.split("").map((y: string) => parseInt(y)))))
})

const getAllTrailHeadScore: GetAllTrailHeadScore = (topographicMap: number[][]): number => {
    let totalScore: number = 0
    for (let i: number = 0; i < topographicMap.length; i ++ ) {
        for (let j: number = 0; j < topographicMap.length; j ++) {
            if (topographicMap[i][j] === 0) {
                totalScore += getTrailScore(i,j,topographicMap, new Set<string>())
            }
        }
    }
    return totalScore
}

const dirs: number[][] = [[0,1],[1,0],[0,-1],[-1,0]]

const getTrailScore: GetTRailScore = (i: number, j: number, map: number[][], visited: Set<string>): number => {
    if (map[i][j] === 9) {
        if (visited.has(JSON.stringify([i,j]))) {
            return 0
        }
        visited.add(JSON.stringify([i,j]))
        return 1
    }

    let currentScore: number = 0
    for (let dir of dirs) {
        let [nextX,nextY] = [i + dir[0], j + dir[1]]
        if (validCoordinate([nextX, nextY], map) && validTrail(map[nextX][nextY], map[i][j])) {
            currentScore += getTrailScore(nextX, nextY, map, visited)
        }
    }
    return currentScore
}

const validCoordinate = (coordinate: number[], matrix: number[][]) => {
    return (coordinate[0] >= 0 && coordinate[0] < matrix.length) && (coordinate[1] >= 0 && coordinate[1] < matrix.length);
}

const validTrail = (nextTrail: number, currentTrail: number): boolean => {
    return nextTrail - currentTrail == 1
}