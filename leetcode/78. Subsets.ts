function subsets(nums: number[]): number[][] {
  let subsets = [[]];
  for (const num of nums) {
    const newSubsets = subsets.map((subset) => {
      return [...subset, num];
    });
    subsets = [...subsets, ...newSubsets];
  }
  return subsets;
}
