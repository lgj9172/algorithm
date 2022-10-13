function findTheCity(
  n: number,
  edges: number[][],
  distanceThreshold: number
): number {
  const MAX = Number.MAX_SAFE_INTEGER;
  const DB = [];

  for (const i of Array(n).keys()) {
    DB[i] = new Array(n).fill(MAX);
    DB[i][i] = 0;
  }

  for (const [from, to, distance] of edges) {
    DB[from][to] = distance;
    DB[to][from] = distance;
  }

  for (const k of Array(n).keys()) {
    for (const i of Array(n).keys()) {
      for (const j of Array(n).keys()) {
        DB[i][j] = Math.min(DB[i][j], DB[i][k] + DB[k][j]);
      }
    }
  }

  let answer = -1;
  let minimumCount = Number.MAX_SAFE_INTEGER;
  for (const i of Array(n).keys()) {
    let count = 0;
    for (const j of Array(n).keys()) {
      if (i === j) continue;
      if (DB[i][j] <= distanceThreshold) count++;
    }
    if (count <= minimumCount) {
      answer = i;
      minimumCount = count;
    }
  }
  return answer;
}

console.log(
  findTheCity(
    4,
    [
      [0, 1, 3],
      [1, 2, 1],
      [1, 3, 4],
      [2, 3, 1],
    ],
    4
  )
);
