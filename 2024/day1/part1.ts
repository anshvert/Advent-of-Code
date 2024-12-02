import * as fs from 'fs'

fs.readFile('./input.txt', 'utf8', (err: unknown, data: string): void => {
    if (err) {
        return console.log(err)
    }
    const rows: string[] = data.split("\n")
    const locations1: number[] = []
    const locations2: number[] = []
    let diff: number = 0

    for (let row in rows) {
        const locations: string[] = rows[row].split("   ")
        locations1.push(parseInt(locations[0],10))
        locations2.push(parseInt(locations[1],10))
    }
    locations1.sort((a: number, b: number): number => a - b)
    locations2.sort((a: number, b: number): number => a - b)
    for (let i: number = 0; i < locations1.length; i++) {
        diff += Math.abs(locations1[i] - locations2[i])
    }
    console.log(diff)
})