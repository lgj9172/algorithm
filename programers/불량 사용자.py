def is_same(exp, target):
    if len(exp) == len(target):
        for i, c in enumerate(exp):
            if c != "*" and exp[i] != target[i]:
                return False
    else:
        return False
    return True

def solution(user_id, banned_id):
    result = 1
    for bid in banned_id:
        count = 0
        for uid in user_id:
            if is_same(bid, uid):
                count += 1
        if count > 0:
            result *= count
    print(result)
    answer = result
    return answer

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"])==2)
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"])==2)
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"])==3)