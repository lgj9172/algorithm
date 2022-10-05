/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function (list1, list2) {
  const answer = new ListNode(0);
  let target = answer;
  while (true) {
    if (!list1 && !list2) {
      break;
    } else if (list1 && !list2) {
      target.next = new ListNode(list1.val);
      list1 = list1.next;
    } else if (!list1 && list2) {
      target.next = new ListNode(list2.val);
      list2 = list2.next;
    } else if (list1.val <= list2.val) {
      target.next = new ListNode(list1.val);
      list1 = list1.next;
    } else if (list1.val > list2.val) {
      target.next = new ListNode(list2.val);
      list2 = list2.next;
    }
    target = target.next;
  }
  return answer.next;
};
