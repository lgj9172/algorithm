function restoreString(s: string, indices: number[]): string {
  const answer = indices
    .map((order, index) => {
      return {
        order: order,
        char: s[index],
      };
    })
    .sort((a, b) => a.order - b.order)
    .map(({ char }) => char)
    .join("");
  return answer;
}
