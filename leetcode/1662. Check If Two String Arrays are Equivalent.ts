function arrayStringsAreEqual(word1: string[], word2: string[]): boolean {
  const string1 = word1.reduce((str, chr) => str + chr, "");
  const string2 = word2.reduce((str, chr) => str + chr, "");
  return string1 === string2;
}
