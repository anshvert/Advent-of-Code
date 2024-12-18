import { CalculateMinCost, GetButtonMoves, GetMinCost, GetPrizePosition } from "./part1";
import * as fs from "fs";

interface SolveEquations {
    (xA: number, xB: number, xPrize: number, yA: number, yB: number, yPrize: number): [number, number]
}

fs.readFile("./input.txt", "utf-8", (err, data) => {
    const gameData: string[] = data.trim().split("\n");
    const games: string[][] = [];
    for (let i: number = 3; i <= gameData.length; i += 4) {
        games.push(gameData.slice(i - 3, i));
    }
    console.log(getMinCost(games));
});

const getMinCost: GetMinCost = (games: string[][]): number => {
    let totalCost: number = 0;
    const convError: number = 10000000000000
    for (let game of games) {
        const [xA, yA]: [number, number] = getButtonMoves(game[0]);
        const [xB, yB]: [number, number] = getButtonMoves(game[1]);
        const [xPrize, yPrize]: [number, number] = getPrizePosition(game[2]);

        const minCost: number = calculateMinCost(xA, yA, xB, yB, xPrize + convError, yPrize + convError);
        if (minCost !== Infinity) {
            totalCost += minCost;
        }
    }
    return totalCost;
};

const calculateMinCost: CalculateMinCost = (xA: number, yA: number, xB: number, yB: number, xPrize: number, yPrize: number): number => {
    const ans: [number, number] = solveEquations(xA, xB, xPrize, yA, yB, yPrize)
    return ans[0] + ans[1]
};

const getButtonMoves: GetButtonMoves = (button: string, sep: string = "+"): [number, number] => {
    const parts: string[] = button.split(":")[1].split(",");
    const xMove: number = parseInt(parts[0].trim().split(sep)[1]);
    const yMove: number = parseInt(parts[1].trim().split(sep)[1]);
    return [xMove, yMove];
};

const getPrizePosition: GetPrizePosition = (prize: string): [number, number] => {
    return getButtonMoves(prize, "=")
};

const solveEquations: SolveEquations = (xA: number, xB: number, xPrize: number, yA: number, yB: number, yPrize: number): [number, number] => {
    const determinant: number = xA * yB - yA * xB;
    if (determinant === 0) {
        return [0,0]
    }
    const w: number = (xPrize * yB - yPrize * xB) / determinant;
    const v: number = (yA * xPrize - xA * yPrize) / determinant;
    if (Number.isInteger(w) && Number.isInteger(v)) {
        return [Math.abs(w) * 3, Math.abs(v)]
    }
    return [0,0]
}

