/**
 * --- Part Two ---
 *
 * The Historians sure are taking a long time. To be fair, the infinite corridors are very large.
 *
 * How many stones would you have after blinking a total of 75 times?
 */

import * as fs from "fs"

fs.readFile("./input.txt",'utf-8', (err, data) => {
    if (err) throw err
    const stones: string[] = data.split(" ")
    console.log(numberStones(stones,75))
})

const numberStones = (stones: string[], blinks: number): number => {
    if (blinks === 0) {
        return stones.length
    }
    let blinkedStones: string[] = []
    let stoneInd: number = 0
    for (let i: number = 0; i < stones.length; i ++) {
        if (stones[i] === '0') {
            blinkedStones[stoneInd] = '1'
        } else if (stones[i].length % 2 === 0) {
            blinkedStones[stoneInd] = Number(stones[i].slice(0, Math.floor(stones[i].length / 2))).toString()
            blinkedStones[stoneInd+1] = Number(stones[i].slice(Math.floor(stones[i].length / 2), stones[i].length)).toString()
            stoneInd += 1
        } else {
            blinkedStones[stoneInd] = (parseInt(stones[i]) * 2024).toString()
        }
        stoneInd += 1
    }
    return numberStones(blinkedStones, blinks - 1)
}