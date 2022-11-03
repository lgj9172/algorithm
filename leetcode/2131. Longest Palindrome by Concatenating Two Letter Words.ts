function longestPalindrome(words: string[]): number {
  const counter = words.reduce(
    (counter, word) => counter.set(word, (counter.get(word) || 0) + 1),
    new Map()
  );
  let length = 0;
  let longest = 0;
  counter.forEach((count, word, map) => {
    const reversedWord = word.split("").reverse().join("");
    if (word === reversedWord) {
      if (count % 2 === 0) {
        length += count * word.length;
      } else {
        length += (count - 1) * word.length;
        longest = Math.max(longest, word.length);
      }
    } else if (map.has(reversedWord)) {
      const reversedWordCount = map.get(reversedWord);
      length += Math.min(count, reversedWordCount) * word.length;
    }
  });
  return length + longest;
}
