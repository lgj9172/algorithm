function minimumTotal(triangle: number[][]): number {
  return triangle
    .reduce(
      (lastRow, currentRow) =>
        currentRow.map((number, colIndex) => {
          if (colIndex === 0) {
            return number + lastRow[0];
          } else if (colIndex === currentRow.length - 1) {
            return number + lastRow[colIndex - 1];
          } else {
            return Math.min(
              number + lastRow[colIndex - 1],
              number + lastRow[colIndex]
            );
          }
        }),
      [0]
    )
    .reduce((minimumTotal, total) => {
      return Math.min(minimumTotal, total);
    }, Number.MAX_SAFE_INTEGER);
}

console.log(minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]));
