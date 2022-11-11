function summaryRanges(nums) {
  const answer: Array<string> = [];
  let last = nums[0];
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] + 1 !== nums[i + 1]) {
      let string = "";
      if (last === nums[i]) {
        string += nums[i];
      } else {
        string += `${last}->${nums[i]}`;
      }
      answer.push(string);
      last = nums[i + 1];
    }
  }
  return answer;
}
