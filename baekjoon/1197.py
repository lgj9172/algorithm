import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
edges = []
roots = [e for e in range(V+1)]

for _ in range(E):
    v1, v2, w = map(int, sys.stdin.readline().split())
    heapq.heappush(edges, (w, v1, v2))


def get_root(v):
    if v == roots[v]:
        return v
    else:
        roots[v] = get_root(roots[v])
        return roots[v]


answer = 0
while edges:
    w, v1, v2 = heapq.heappop(edges)
    v1_root = get_root(v1)
    v2_root = get_root(v2)
    if v1_root != v2_root:
        roots[v2_root] = v1_root
        answer += w

print(answer)
