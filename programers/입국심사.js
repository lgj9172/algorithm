function solution(n, times) {
  times = times.sort((a, b) => a - b);
  let left = 1;
  let right = times[times.length - 1] * n;
  let mid = Math.floor((left + right) / 2);
  while (left <= right) {
    const count = times.reduce((prev, curr) => {
      return prev + Math.floor(mid / curr);
    }, 0);
    if (count >= n) right = mid - 1;
    else if (count < n) left = mid + 1;
    mid = Math.floor((left + right) / 2);
  }
  return left;
}
