const fs = require("fs");
const input = fs
  // .readFileSync(`${process.cwd()}/12887.txt`)
  .readFileSync("/dev/stdin")
  .toString()
  .split("\n");

// get data
const M = Number(input[0]);
const DB = [input[1].trim().split(""), input[2].trim().split("")];

// get answer
let answer = 0;
let before = "none";
for (let i = 0; i < M; i++) {
  const top = DB[0][i];
  const bot = DB[1][i];
  if (top === "#" && bot === ".") {
    if (before === "top") {
      answer -= 1;
    }
    before = "bot";
  } else if (top === "." && bot === "#") {
    if (before === "bot") {
      answer -= 1;
    }
    before = "top";
  } else if (top === "." && bot === ".") {
    answer += 1;
  }
}
console.log(answer);
