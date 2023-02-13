function sortPeople(names: string[], heights: number[]): string[] {
  return Object.entries(heights)
    .sort((a, b) => b[1] - a[1])
    .map(([index, height]) => names[Number(index)]);
}
