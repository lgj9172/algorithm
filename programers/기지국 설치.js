function solution(n, stations, w) {
  let answer = 0,
    start = 1;
  const power = w * 2 + 1;
  for (const station of stations) {
    const left = station - w,
      right = station + w;
    if (left > start) answer += Math.ceil((left - start) / power);
    start = right + 1;
  }
  if (start <= n) answer += Math.ceil((n - start + 1) / power);
  return answer;
}
