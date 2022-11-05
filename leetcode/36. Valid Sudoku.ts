function isValidSudoku(board: string[][]): boolean {
  const DB = new Set();
  for (let i = 0; i < 9; i++) {
    for (let j = 0; j < 9; j++) {
      const value = board[i][j];
      if (value !== ".") {
        const row = `r${i}/${value}`;
        const col = `c${j}/${value}`;
        const sqr = `s${Math.floor(i / 3) * 3 + Math.floor(j / 3)}/${value}`;
        if (DB.has(row) || DB.has(col) || DB.has(sqr)) {
          return false;
        } else {
          [row, col, sqr].forEach((e) => DB.add(e));
        }
      }
    }
  }
  return true;
}
