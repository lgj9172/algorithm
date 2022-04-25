from collections import deque


def push_num(descend_queue, index, num):
    if descend_queue[0][1] <= num:
        descend_queue.clear()
        descend_queue.extend([(index, num)])
    elif descend_queue[-1][1] <= num:
        while descend_queue[-1][1] <= num:
            descend_queue.pop()
        descend_queue.append((index, num))
    elif descend_queue[-1][1] > num:
        descend_queue.append((index, num))


def shift_num(descend_queue, index, k):
    if len(descend_queue) > k or index - descend_queue[0][0] >= k:
        descend_queue.popleft()


def make_answer(answer, descend_queue):
    answer.append(descend_queue[0][1])


def get_answer(answer, k):
    return answer[k-1:]


class Solution:
    def maxSlidingWindow(self, nums, k):
        descend_queue = deque([(0, nums[0])])
        answer = []
        for i, n in enumerate(nums):
            push_num(descend_queue, i, n)
            shift_num(descend_queue, i, k)
            make_answer(answer, descend_queue)
        return get_answer(answer, k)


print(Solution().maxSlidingWindow([1, 3, 1, 2, 0, 5], 3))
print([3, 3, 2, 5])
