from collections import deque
N, K = map(int, input().split())
if N > K: # 동생이 더 앞에 있는 경우
    print(N-K)
else: # 동생이 뒤에 있는 경우
    db = dict()
    dq = deque([N])
    db[N] = 0
    while dq:
        target = dq.popleft()
        if target == K: # 뽑은 내용이 목표이면 보여주기
            print(db[target])
            break
        next_targets = [target*2, target-1, target+1]
        for i, next_target in enumerate(next_targets):
            if 0 <= next_target and next_target <= 100000 and next_target not in db.keys():
                if i == 0:
                    # 두배인 경우는 cost 0 증가
                    db[next_target] = db[target]
                    dq.appendleft(next_target)
                else:
                    # 앞뒤인 경우는 cost 1 증가
                    db[next_target] = db[target] + 1
                    dq.append(next_target)