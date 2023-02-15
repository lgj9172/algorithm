function isFit(uid, bid) {
  return RegExp(`^${bid.replace(/\*/g, ".")}$`).test(uid);
}

function solution(user_id, banned_id) {
  const candidates = [];
  for (const bid of banned_id) {
    const candidate = [];
    for (const uid of user_id) {
      if (isFit(uid, bid)) {
        candidate.push(uid);
      }
    }
    candidates.push(candidate);
  }
  const queue = [[-1, new Set()]];
  const history = new Set();
  const answerSet = new Set();
  while (queue.length > 0) {
    const [index, bag] = queue.shift();
    const bagString = [...bag].sort().join(",");
    if (index === candidates.length - 1) {
      if (bag.size === banned_id.length) {
        answerSet.add(bagString);
      }
      continue;
    }
    if (history.has(bagString)) {
      continue;
    }
    history.add(bagString);
    for (word of candidates[index + 1]) {
      queue.push([index + 1, new Set([...bag, word])]);
    }
  }
  return answerSet.size;
}
