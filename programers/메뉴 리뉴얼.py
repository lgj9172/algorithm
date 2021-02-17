from collections import defaultdict
import itertools


def solution(orders, course):
    db = defaultdict(int)
    length_rank = defaultdict(int)
    # 어떤 오더를 불러와서
    for order in orders:
        order = "".join(sorted(order))
        order_length = len(order)
        # 그 오더로 구할수 있는 모든 조합을 구합니다.
        for n in range(2, min(11, order_length + 1)):
            # 그 조합을 사전에 추가해줍니다.
            for c in itertools.combinations(order, n):
                count = db[c] + 1
                db[c] = count
                # 조합 길이별로 가장 많이 등장한 횟수를 기록합니다.
                length_rank[n] = max(count, length_rank[n])
    # 두번 이상 등장했고, 요구하는 길이조건에도 포함되며, 가장 많이 등장한 경우로 필터링합니다.
    db = {
        key: value
        for key, value in db.items()
        if len(key) in course and value >= 2 and length_rank[len(key)] == value
    }
    return sorted(["".join(key) for key in db.keys()])


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))