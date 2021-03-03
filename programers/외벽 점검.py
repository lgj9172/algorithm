from itertools import permutations
from copy import deepcopy

# 리스트에서 첫 원소로부터 일정 거리 이하의 숫자는 모두 삭제합니다.
def remove_element_under(list, distance):
    start = list[0]
    finish = start + distance
    return [e for e in list if e > finish]


def solution(n, weak, dist):
    # 사이거리를 모두 기록합니다.
    between = []
    for i in range(len(weak)):
        if i == len(weak) - 1:
            between.append((n - weak[i]) + weak[0])
        else:
            between.append(weak[i + 1] - weak[i])
    # 사이거리가 가장 큰 부분의 인덱스를 구합니다.
    MAX = max(between)
    max_index = -1
    for i, e in enumerate(between):
        if e == MAX:
            max_index = i
            break
    # 사이거리가 가장 큰 부분의 다음 인덱스를 구합니다.
    max_index_next = max_index + 1 if max_index < len(weak) - 1 else 0
    # 사이거리가 가장 큰 부분이 끝나는 부분부터 다시 배열을 만듭니다.
    list1 = []
    list2 = []
    list1_offset = weak[max_index_next]
    list2_offset = n - weak[max_index_next]
    for i, e in enumerate(weak):
        if i < max_index_next:
            list2.append(weak[i] + list2_offset)
        elif i >= max_index_next:
            list1.append(weak[i] - list1_offset)
    new_weak = list1 + list2

    # dist에서 상위 1개, 2개, ... , k개를 뽑아서 순열을 얻고,
    # 그 순열로 새로운 배열이 모두 삭제 될 수 있는지 확인합니다.
    # 그 순열로 기존 배열이 모두 삭제 될 수 있는지 확인합니다.
    for k in range(1, len(dist) + 1):
        p_list = permutations(dist[::-1][:k], k)
        for pk_list in p_list:
            now_weak = deepcopy(new_weak)
            for number in pk_list:
                now_weak = remove_element_under(now_weak, number)
            if len(now_weak) == 0:
                return k
            now_weak = deepcopy(weak)
            for number in pk_list:
                now_weak = remove_element_under(now_weak, number)
            if len(now_weak) == 0:
                return k

    return -1


# print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
# print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
print(solution(30, [0, 3, 11, 21], [10, 4]))
# print(solution(200, [0, 100], [1, 1]))
# print(solution(200, [1, 100], [1]))
