interface Trie {
  [key: string]: Trie | string | null;
}

const dfs = (
  node: Trie,
  board: string[][],
  row: number,
  col: number,
  result: string[]
): void => {
  if (node.word) {
    result.push(node.word as string);
    node.word = null;
  }

  if (row < 0 || row >= board.length || col < 0 || col >= board[0].length) {
    return;
  }

  if (!node[board[row][col]]) {
    return;
  }

  const char = board[row][col];

  board[row][col] = "-";

  dfs(node[char] as Trie, board, row + 1, col, result);
  dfs(node[char] as Trie, board, row - 1, col, result);
  dfs(node[char] as Trie, board, row, col + 1, result);
  dfs(node[char] as Trie, board, row, col - 1, result);

  board[row][col] = char;
};

const trie = function (words: string[]): Trie {
  const root: Trie = {};

  for (const word of words) {
    let target: Trie = root;

    for (const char of word) {
      if (!target[char]) {
        target[char] = {} as Trie;
      }

      target = target[char] as Trie;
    }

    target.word = word;
  }

  return root;
};

function findWords(board: string[][], words: string[]): string[] {
  const result: string[] = [];

  const root = trie(words);

  for (let i: number = 0; i < board.length; i += 1) {
    for (let j: number = 0; j < board[0].length; j += 1) {
      dfs(root, board, i, j, result);
    }
  }

  return result;
}
