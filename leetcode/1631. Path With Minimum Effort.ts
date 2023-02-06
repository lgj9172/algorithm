import { MinPriorityQueue } from "@datastructures-js/priority-queue";

function minimumEffortPath(heights: number[][]): number {
  const r = heights.length;
  const c = heights[0].length;
  const visited = Array.from({ length: r }, () =>
    Array.from({ length: c }, () => false)
  );
  const heap = new MinPriorityQueue({
    priority: (e) => e[2],
  });
  heap.enqueue([0, 0, 0]);

  while (heap.size()) {
    const [i, j, max] = heap.dequeue().element;

    if (i === r - 1 && j === c - 1) return max;

    if (visited[i][j]) continue;
    visited[i][j] = true;

    for (let [x, y] of [
      [0, 1],
      [0, -1],
      [1, 0],
      [-1, 0],
    ]) {
      const ni = i + x,
        nj = j + y;
      if (ni >= 0 && nj >= 0 && ni < r && nj < c) {
        heap.enqueue([
          ni,
          nj,
          Math.max(Math.abs(heights[i][j] - heights[ni][nj]), max),
        ]);
      }
    }
  }
}
