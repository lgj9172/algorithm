/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  const stack = [];
  const starts = "({[";
  const startForEnd = {
    ")": "(",
    "}": "{",
    "]": "[",
  };
  for (bracket of s) {
    if (starts.indexOf(bracket) > -1) {
      stack.push(bracket);
    } else {
      const lastElement = stack.pop();
      const expectStart = startForEnd[bracket];
      if (lastElement !== expectStart) {
        return false;
      }
    }
  }
  if (stack.length > 0) {
    return false;
  }
  return true;
};
