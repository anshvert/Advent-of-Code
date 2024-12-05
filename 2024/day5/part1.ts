import * as fs from 'fs'

fs.readFile('./input.txt', 'utf8', (err: unknown, data: string): void => {
    if (err) {
        console.log(err)
        return
    }
    const orderMap: Map<string, string[]> = new Map()
    const updates: string[][] = []
    const printData: string[] = data.split("\n")

    for (let i: number = 0; i < printData.length; i ++) {
        if (!printData[i].length) {
            continue
        } if (printData[i].includes("|")) {
            const pages: string[] = printData[i].split("|")
            const currentPages: string[] | undefined = orderMap.get(pages[0])
            if (currentPages?.length) {
                currentPages.push(pages[1])
            }
            orderMap.set(pages[0], currentPages ?? [pages[1]])
        } else {
            updates.push(printData[i].split(","))
        }
    }
    let middleCount: number = 0
    for (let i: number = 0; i < updates.length; i ++) {
        const update: string[] = updates[i]
        const visited: Set<string> = new Set()
        let validUpdate: boolean = true
        for (let i: number = 0; i < update.length; i ++) {
            const updateKey: string = update[i]
            const secondPages: string[] | undefined = orderMap.get(updateKey)
            if (!secondPages) {
                visited.add(updateKey)
                continue
            }
            let validKey: boolean = true
            for (let page: number = 0; page < secondPages.length; page ++) {
                if (visited.has(secondPages[page])) {
                    validKey = false
                    break
                }
            }
            if (!validKey) {
                validUpdate = false
                break
            }
            visited.add(updateKey)
        }
        if (validUpdate) {
            middleCount += getMiddle(update)
        }
    }
    console.log(middleCount)
})

const getMiddle = (update: string[]): number => {
    return parseInt(update[Math.floor(update.length / 2)])
}