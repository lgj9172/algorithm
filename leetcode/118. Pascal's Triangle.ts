function generate(numRows: number): number[][] {
  const answer: number[][] = [];
  for (let i = 0; i < numRows; i++) {
    if (i === 0) {
      answer.push([1]);
    } else {
      const lastRow = answer[answer.length - 1];
      const row = [];
      for (let j = 0; j <= lastRow.length; j++) {
        if (j === 0) row.push(1);
        else if (j === lastRow.length) row.push(1);
        else row.push(lastRow[j - 1] + lastRow[j]);
      }
      answer.push(row);
    }
  }
  return answer;
}
