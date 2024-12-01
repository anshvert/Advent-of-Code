import * as fs from 'fs'

fs.readFile('./input.txt', 'utf8', (err: unknown, data: string): void => {
    if (err) {
        return console.log(err)
    }
    const rows: string[] = data.split("\n")
    const locations1: number[] = []
    let diff: number = 0
    let map: Map<any, any> = new Map()

    for (let row in rows) {
        const locations: string[] = rows[row].split("   ")
        locations1.push(parseInt(locations[0],10))
        map.set(locations[1], map.get(locations[1]) ? map.get(locations[1]) + 1: 1)
    }
    for (let i: number = 0; i < locations1.length; i++) {
        diff += locations1[i] * (map.get(locations1[i].toString()) || 0 )
    }
    console.log(diff)
})