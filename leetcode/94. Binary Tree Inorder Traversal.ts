class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

function recursiveInorder(node: TreeNode, result: number[]) {
  if (node.left) recursiveInorder(node.left, result);
  result.push(node.val);
  if (node.right) recursiveInorder(node.right, result);
}

function inorderTraversal(root: TreeNode | null): number[] {
  const answer: number[] = [];
  if (root) recursiveInorder(root, answer);
  return answer;
}
