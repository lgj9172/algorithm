from collections import defaultdict, deque
from copy import deepcopy


def solution(n, start, end, roads, traps):
    way = defaultdict(list)
    cost = defaultdict(lambda: 3001)
    available = defaultdict(lambda: False)
    for road in roads:
        s, e, c = road
        way[s].append(e)
        way[e].append(s)
        cost[(s,e)] = min(c, cost[(s,e)])
        available[(s,e)] = True
    MIN = float("inf")
    ncost = deepcopy(cost)
    navailable = deepcopy(available)
    nhistory = set()
    ntotal_cost = 0
    queue = deque([(start, ncost, navailable, nhistory, ntotal_cost)])
    while queue:
        target = queue.popleft()
        current, cost, available, history, total_cost = target
        if current == end and len(history) == n-1:
            MIN = min(MIN, total_cost)
            continue
        if total_cost >= MIN:
            continue
        if current in traps:
            nexts = way[current]
            for next in nexts:
                cost[(next,current)], cost[(current,next)] = cost[(current,next)], cost[(next,current)]
                available[(next, current)], available[(current,next)] = available[(current,next)], available[(next,current)]
        history.add(current)
        for next in way[current]:
            if available[(current,next)]==True:
                ncost = deepcopy(cost)
                navailable = deepcopy(available)
                nhistory = deepcopy(history)
                ntotal_cost = total_cost + cost[(current,next)]
                queue.append((next, ncost, navailable, nhistory, ntotal_cost))

    return MIN

print(solution(3,1,3,[[1, 2, 2],[3, 2, 3]],[2]))
print(solution(4,1,4,[[1, 2, 1],[3, 2, 1],[2, 4, 1]],[2, 3]))