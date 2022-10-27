function wordPattern(pattern: string, s: string): boolean {
  const patterns = pattern.split("");
  const strings = s.split(" ");
  if (patterns.length !== strings.length) return false;
  const string2pattern = new Map();
  const pattern2string = new Map();
  for (let i = 0; i < patterns.length; i++) {
    const pattern = patterns[i];
    const string = strings[i];
    if (string2pattern.has(string) && pattern2string.has(pattern)) {
      const patternFromString = string2pattern.get(string);
      const stringFromPattern = pattern2string.get(pattern);
      if (patternFromString !== pattern || stringFromPattern !== string) {
        return false;
      }
    } else if (!string2pattern.has(string) && !pattern2string.has(pattern)) {
      string2pattern.set(string, pattern);
      pattern2string.set(pattern, string);
    } else {
      return false;
    }
  }
  return true;
}
