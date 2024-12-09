import * as fs from "fs"

export interface GetArrangedDiskMap {
    (diskMap: string): string[][]
}

export interface GetMovedDiskMap {
    (arrangedDiskMap: string[][]): string[][]
}

export interface GetCheckSum {
    (diskMap: string[][]): number
}

fs.readFile("./input.txt", "utf8", (err, diskMap: string): void => {
    if (err) throw err;
    const arrangedDiskMap: string[][] = getArrangedDiskMap(diskMap)
    const movedDiskMap: string[][] = getMovedDiskMap(arrangedDiskMap)
    console.log(getCheckSum(movedDiskMap))
})

const getArrangedDiskMap: GetArrangedDiskMap = (diskMap: string): string[][] => {
    let ID: number = 0
    let arrangedBlock: string[][] = []
    for(let i: number = 0; i < diskMap.length; i++) {
        if (i & 1) {
            arrangedBlock.push(".".repeat(parseInt(diskMap[i])).split(""))
        } else {
            const blockString: string[] = `${ID}:`.repeat(parseInt(diskMap[i])).split(":")
            arrangedBlock.push(blockString.slice(0,blockString.length - 1))
            ID += 1
        }
    }
    return arrangedBlock
}

const getMovedDiskMap: GetMovedDiskMap = (arrangedDiskMap: string[][]): string[][] => {
    let leftIndex: number = 0;
    let rightIndex: number = arrangedDiskMap.length - 1;

    while (leftIndex < rightIndex) {
        while (leftIndex < arrangedDiskMap.length && !arrangedDiskMap[leftIndex].includes('.')) {
            leftIndex++;
        }
        while (rightIndex >= 0 && arrangedDiskMap[rightIndex].every(el => el === '.')) {
            rightIndex--;
        }
        if (leftIndex >= rightIndex) {
            break;
        }
        const block: string = arrangedDiskMap[rightIndex].pop() as string;
        const dotIndex: number = arrangedDiskMap[leftIndex].indexOf('.');
        arrangedDiskMap[leftIndex][dotIndex] = block;
        if (arrangedDiskMap[rightIndex].length === 0) {
            arrangedDiskMap[rightIndex] = ['.'];
        }
    }
    return arrangedDiskMap
}

const getCheckSum: GetCheckSum = (diskMap: string[][]): number => {
    let checkSum: number = 0
    let checkSumArr: string[] = []
    for (let i = 0; i < diskMap.length; i++) {
        checkSumArr = checkSumArr.concat(diskMap[i])
    }
    for (let i = 0; i < checkSumArr.length; i++) {
        if (checkSumArr[i] === '.') break
        checkSum += i * parseInt(checkSumArr[i])
    }
    return checkSum
}
