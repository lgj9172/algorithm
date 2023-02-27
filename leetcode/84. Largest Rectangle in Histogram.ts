function peek(list: number[]) {
  return list[list.length - 1];
}

function largestRectangleArea(heights: number[]): number {
  let answer = 0;
  let stack = [0];
  heights.push(0);
  heights.forEach((height) => {
    if (height >= peek(stack)) {
      stack.push(height);
    } else {
      let width = 1;
      while (peek(stack) > height) {
        const last = stack.pop()!;
        const size = last * width;
        answer = Math.max(answer, size);
        width += 1;
      }
      for (let i = 0; i < width; i++) {
        stack.push(height);
      }
    }
  });
  return answer;
}
