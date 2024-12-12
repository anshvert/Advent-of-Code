import * as fs from "fs"

interface NumberStones {
    (stoneMap: Map<string, number>, blinks: number): number
}

interface SetMap {
    (map: Map<string, number>, key: string, val: number): Map<string, number>
}

fs.readFile("./input.txt",'utf-8', (err, data) => {
    if (err) throw err
    const stones: string[] = data.split(" ")
    let stoneMap: Map<string, number> = new Map()
    for (let i = 0; i < stones.length; i++) {
        stoneMap = setMap(stoneMap, stones[i], 1)
    }
    console.log(numberStones(stoneMap,75))
})

const numberStones: NumberStones = (stoneMap: Map<string, number>, blinks: number): number => {
    if (blinks === 0) {
        return Array.from(stoneMap.values()).reduce((sum,val) => sum + val, 0)
    }
    let blinkedStones: Map<string, number> = new Map()
    stoneMap.forEach((val: number, key: string) => {
        if (key === '0') {
            const newVal = '1'
            blinkedStones = setMap(blinkedStones, newVal, val)
        } else if (key.length % 2 === 0) {
            const stone1 = Number(key.slice(0, Math.floor(key.length / 2))).toString()
            const stone2 = Number(key.slice(Math.floor(key.length / 2), key.length)).toString()
            blinkedStones = setMap(blinkedStones, stone1, stoneMap.get(key) ?? 1)
            blinkedStones = setMap(blinkedStones, stone2, stoneMap.get(key) ?? 1)
        } else {
            const newVal = (parseInt(key) * 2024).toString()
            blinkedStones = setMap(blinkedStones, newVal, val)
        }
    })
    return numberStones(blinkedStones, blinks - 1)
}

const setMap: SetMap = (map: Map<string, number>, key: string, val: number): Map<string, number> => {
    map.set(key, (map.get(key) ?? 0) + val)
    return map
}