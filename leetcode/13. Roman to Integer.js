/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function (s) {
  const symbolToValue = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
  };
  const numbers = s.split("").map((symbol) => symbolToValue[symbol]);
  const answer = numbers.reduce((sum, number, index, numbers) => {
    const minus =
      index > 0 && numbers[index - 1] < number ? numbers[index - 1] * -2 : 0;
    return sum + number + minus;
  }, 0);
  return answer;
};
