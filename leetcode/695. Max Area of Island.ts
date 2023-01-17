function maxAreaOfIsland(grid: number[][]): number {
  const m = grid.length;

  const n = grid[0].length;

  const visited = Array.from({ length: m }, () =>
    Array.from({ length: n }, () => false)
  );

  let max = 0;

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (grid[i][j] === 0) continue;

      const queue: Array<[number, number]> = [[i, j]];

      let count = 0;

      while (queue.length) {
        const element = queue.shift();
        if (!element) continue;
        const [row, col] = element;

        if (grid[row][col] === 0) continue;

        if (visited[row][col]) continue;

        visited[row][col] = true;
        count += 1;

        for (const [rowOffset, colOffset] of [
          [0, 1],
          [0, -1],
          [1, 0],
          [-1, 0],
        ]) {
          const newRow = row + rowOffset;
          const newCol = col + colOffset;
          if (newRow >= 0 && newRow < m && newCol >= 0 && newCol < n) {
            queue.push([newRow, newCol]);
          }
        }
      }

      max = Math.max(max, count);
    }
  }

  return max;
}
