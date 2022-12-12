function highestPeak(isWater: number[][]): number[][] {
  let arr = Array(isWater.length);
  let queue: Array<[number, number]> = [];
  let mr = isWater.length;
  let mc = isWater[0].length;
  for (let i = 0; i < mr; i++) {
    arr[i] = Array(mc).fill(-1);
    for (let j = 0; j < mc; j++) {
      if (isWater[i][j] === 1) {
        queue.push([i, j]);
        arr[i][j] = 0;
      } else {
        arr[i][j] = -1;
      }
    }
  }
  let moves = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];
  let i = 0;
  while (i < queue.length) {
    const [r, c] = queue[i];
    for (let move of moves) {
      const nr = r + move[0];
      const nc = c + move[1];
      if (nr < 0 || nc < 0 || nr >= mr || nc >= mc || arr[nr][nc] != -1) {
        continue;
      }
      arr[nr][nc] = arr[r][c] + 1;
      queue.push([nr, nc]);
    }
    i++;
  }
  return arr;
}
