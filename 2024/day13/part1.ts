import * as fs from "fs";

export interface GetMinCost {
    (games: string[][]): number
}

export interface CalculateMinCost {
    (xA: number, yA: number, xB: number, yB: number, xPrize: number, yPrize: number): number
}

export interface GetButtonMoves {
    (button: string, sep?: string): [number, number]
}

export interface GetPrizePosition {
    (prize: string): [number, number]
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
    for (let game of games) {
        const [xA, yA]: [number, number] = getButtonMoves(game[0]);
        const [xB, yB]: [number, number] = getButtonMoves(game[1]);
        const [xPrize, yPrize]: [number, number] = getPrizePosition(game[2]);

        const minCost: number = calculateMinCost(xA, yA, xB, yB, xPrize, yPrize);
        if (minCost !== Infinity) {
            totalCost += minCost;
        }
    }
    return totalCost;
};

const calculateMinCost: CalculateMinCost = (xA: number, yA: number, xB: number, yB: number, xPrize: number, yPrize: number): number => {
    let minCost: number = Infinity;
    for (let w: number = 0; w <= 100; w++) {
        for (let v: number = 0; v <= 100; v++) {
            if (xA * w + xB * v === xPrize && yA * w + yB * v === yPrize) {
                const cost: number = w * 3 + v;
                minCost = Math.min(minCost, cost);
            }
        }
    }
    return minCost;
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



