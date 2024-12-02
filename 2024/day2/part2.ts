import * as fs from 'fs'

interface SafeLevel {
    (level: string[]): boolean
}

fs.readFile('./input.txt', 'utf8', (err: unknown, data: string): void => {
    if (err) {
        return console.log(err)
    }
    let count: number = 0
    const rows: string[] = data.split('\n')
    for (let row of rows) {
        const level: string[] = row.split(" ")
        if (safeLevel(level) || madeSafeLevel(level)) {
            count += 1
        }
    }
    console.log(count)
})

const safeLevel: SafeLevel = (level: string[]): boolean => {
    const isIncreasing: boolean = parseInt(level[1],10) - parseInt(level[0],10) >= 0
    for (let i: number = 1; i < level.length; i++) {
        const diff: number = parseInt(level[i], 10) - parseInt(level[i-1],10)
        if (Math.abs(diff) < 1 || Math.abs(diff) > 3) {
            return false
        } else if ((isIncreasing && diff < 0) || (!isIncreasing && diff > 0)) {
            return false
        }
    }
    return true
}

const madeSafeLevel: SafeLevel = (level: string[]): boolean => {
    for (let i: number = 0; i < level.length; i++) {
        const newLevel: string[] = level.slice(0,i).concat(level.slice(i+1, level.length))
        if (safeLevel(newLevel)) {
            return true
        }
    }
    return false
}