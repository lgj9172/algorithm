function trap(height: number[]): number {
  let dpFromFront: number[] = [];
  height.reduce((max, curr) => {
    const newMax = Math.max(max, curr);
    dpFromFront.push(newMax);
    return newMax;
  }, 0);

  let dpFromBack: number[] = [];
  height.reverse().reduce((max, curr) => {
    const newMax = Math.max(max, curr);
    dpFromBack.push(newMax);
    return newMax;
  }, 0);
  dpFromBack = dpFromBack.reverse();

  const answer = [];
  for (let i = 0; i < dpFromFront.length; i++) {
    answer.push(Math.min(dpFromFront[i], dpFromBack[i]));
  }
  return answer.reduce((s, c) => s + c, 0) - height.reduce((s, c) => s + c, 0);
}

console.log(trap([4, 2, 0, 3, 2, 5]));
