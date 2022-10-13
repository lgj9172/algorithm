/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function (strs) {
  const answer = strs.reduce((result, str) => {
    while (true) {
      if (result === "") {
        return "";
      } else if (str.startsWith(result)) {
        return result;
      } else {
        console.log(result);
        result = result.slice(0, result.length - 1);
      }
    }
  }, strs[0]);
  return answer;
};
