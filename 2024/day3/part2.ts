import * as fs from 'fs'

interface CheckValidMul {
    (memory: string, data: string, firstInd: number): ValidMul
}

interface HandleEnable {
    (data: string, index: number, enabled: boolean): boolean
}

type ValidMul = {
    status: boolean,
    result: number,
}

fs.readFile('./input.txt', 'utf8', (err: unknown, data: string): void => {
    if (err) {
        return console.log(err)
    }
    const memory: [number,string][] = []
    let ans: number = 0
    let enabled: boolean = true

    for (let i: number = 0; i < data.length; i++) {
        if (data[i] == "(") {
            memory.push([i,"("])
        } else if (data[i] == ")") {
            const lastVal: [number, string] | undefined = memory.pop()
            if (lastVal) {
                enabled = handleEnable(data, lastVal[0], enabled)
                if (enabled) {
                    const validMul: ValidMul = checkValidMul(data.slice(lastVal[0]+1,i), data, lastVal[0])
                    if (validMul.status) {
                        ans += validMul.result
                    }
                }
            }
        }
    }
    console.log(ans)
})

const handleEnable: HandleEnable = (data: string, index: number, enabled: boolean): boolean => {
    try {
        if (data[index-1] + data[index-2] === "od") {
            return true
        } else if (data[index-1] + data[index-2] + data[index-3] + data[index-4] + data[index-5] === "t'nod") {
            return false
        }
        return enabled
    } catch (err) {
        return enabled
    }
}

const checkValidMul: CheckValidMul = (memory: string, data: string, fistInd: number): ValidMul => {
    try {
        if (data[fistInd-1] + data[fistInd-2] + data[fistInd-3] === "lum") {
            const numbers: string[] = memory.split(",")
            const num1: number = Number(numbers[0])
            const num2: number = Number(numbers[1])
            if (Number.isFinite(num1) && Number.isFinite(num2) && numbers.length === 2) {
                return {
                    status: true,
                    result: num1 * num2
                }
            } else {
                return { status: false, result: 0 }
            }
        } else {
            return { status: false, result: 0 }
        }
    } catch (err) {
        return { status: false, result: 0 }
    }
}
