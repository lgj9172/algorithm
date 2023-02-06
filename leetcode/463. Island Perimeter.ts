function islandPerimeter(grid: number[][]): number {
  const row = grid.length;
  const col = grid[0].length;
  let answer = 0;
  for (let i = 0; i < row; i++) {
    for (let j = 0; j < col; j++) {
      const target = grid[i][j];
      if (target === 1) {
        let count = 4;
        if (i - 1 >= 0 && grid[i - 1][j] === 1) count--;
        if (i + 1 < row && grid[i + 1][j] === 1) count--;
        if (j - 1 >= 0 && grid[i][j - 1] === 1) count--;
        if (j + 1 < col && grid[i][j + 1] === 1) count--;
        answer += count;
      }
    }
  }
  return answer;
}
