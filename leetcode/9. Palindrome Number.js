/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
  const original = x.toString();
  const reversed = x.toString().split("").reverse().join("");
  if (original === reversed) {
    return true;
  } else {
    return false;
  }
};
