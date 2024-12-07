import * as fs from "fs"
import { GetTrueEquationsResult, TrueEquation } from "./part1";

fs.readFile("./input.txt", "utf8", (err, data: string): void => {
    if (err) throw err;
    const equations: string[] = data.split("\n")
    const equationMap = new Map<number, number[]>()
    equations.forEach(equation => {
        const eqs: string[] = equation.split(":")
        let [key,value] = [parseInt(eqs[0]), eqs[1].trim().split(" ").map((num: string) => parseInt(num))]
        equationMap.set(key, value)
    })
    console.log(getTrueEquationsResult(equationMap))
})

const getTrueEquationsResult: GetTrueEquationsResult = (eqMap: Map<number, number[]>): number => {
    let ans: number = 0
    eqMap.forEach((value: number[], key: number): void => {
        if (trueEquation(key,value, 1, value[0])) {
            ans += key
        }
    })
    return ans
}

const trueEquation: TrueEquation = (key: number,value: number[], index: number, currentVal: number): boolean => {
    if (index === value.length) {
        return currentVal === key;
    }
    return trueEquation(key, value, index + 1, currentVal + value[index])
        || trueEquation(key, value, index + 1, currentVal * value[index])
        || trueEquation(key, value, index + 1, parseInt(currentVal.toString() + value[index].toString()))
}
