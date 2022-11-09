function plusOne(digits: number[]): number[] {
  return String(BigInt(digits.join("")) + 1n)
    .split("")
    .map((char) => Number(char));
}
