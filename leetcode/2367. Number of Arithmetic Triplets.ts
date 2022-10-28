function arithmeticTriplets(nums: number[], diff: number): number {
  const nums_set = new Set(nums);
  let count = 0;
  nums_set.forEach((num: number) => {
    if (nums_set.has(num + diff) && nums_set.has(num + diff * 2)) count++;
  });
  return count;
}
