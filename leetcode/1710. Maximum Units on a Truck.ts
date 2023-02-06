function maximumUnits(boxTypes: number[][], truckSize: number): number {
  return boxTypes
    .sort((a, b) => b[1] - a[1])
    .reduce(
      (prev, curr) => {
        const [answer, leftSpace] = prev;
        const [numberOfBoxes, unitsPerBox] = curr;
        const useSpace = Math.min(leftSpace, numberOfBoxes);
        const newAnswer = answer + useSpace * unitsPerBox;
        const newLeftSpace = leftSpace - useSpace;
        return [newAnswer, newLeftSpace];
      },
      [0, truckSize]
    )[0];
}
