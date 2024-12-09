import * as fs from "fs"
import {GetArrangedDiskMap, GetCheckSum, GetMovedDiskMap} from "./part1";

fs.readFile("./input.txt", "utf8", (err, diskMap: string): void => {
    if (err) throw err;
    const arrangedDiskMap: string[][] = getArrangedDiskMap(diskMap)
    const movedDiskMap: string[][] = getMovedDiskMap(arrangedDiskMap)
    console.log(getCheckSum(movedDiskMap))
})

const getArrangedDiskMap: GetArrangedDiskMap = (diskMap: string): string[][] => {
    let ID: number = 0
    let arrangedBlock: string[][] = []
    for(let i = 0; i < diskMap.length; i++) {
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
    let rightIndex: number = arrangedDiskMap.length - 1;

    while (rightIndex >= 0) {
        while (rightIndex >= 0 && arrangedDiskMap[rightIndex].includes('.')) {
            rightIndex -= 1
        }
        let leftIndex = 0
        while (leftIndex < arrangedDiskMap.length && arrangedDiskMap[leftIndex].filter((x) => x === '.').length < arrangedDiskMap[rightIndex].length) {
            leftIndex += 1
        }
        if (leftIndex >= rightIndex) {
            rightIndex -= 1
            continue
        }
        let li: number = 0
        for (let ri: number = 0; ri < arrangedDiskMap[rightIndex].length; ri++) {
            while(arrangedDiskMap[leftIndex][li] !== '.') {
                li += 1
            }
            [arrangedDiskMap[leftIndex][li], arrangedDiskMap[rightIndex][ri]] =
                [arrangedDiskMap[rightIndex][ri],arrangedDiskMap[leftIndex][li]]
        }
        rightIndex -= 1
    }
    return arrangedDiskMap
}

const getCheckSum: GetCheckSum = (diskMap: string[][]): number => {
    let checkSum: number = 0
    let checkSumArr: string[] = []
    for (let i: number = 0; i < diskMap.length; i++) {
        checkSumArr = checkSumArr.concat(diskMap[i])
    }
    for (let i: number = 0; i < checkSumArr.length; i++) {
        if (checkSumArr[i] === '.' || checkSumArr[i] === '#') continue
        checkSum += i * parseInt(checkSumArr[i])
    }
    return checkSum
}
