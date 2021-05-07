def solution(gems):
    gems_count = {k: 0 for k in (set(gems))}
    pos1, pos2 = 0, 0
    gems_count[gems[pos1]] += 1
    min_length = len(gems) + 1
    answer = []
    while True:
        if 0 in gems_count.values():
            if pos2+1 == len(gems): # 포인터가 범위를 벗어난 경우
                break
            elif pos2 - pos1 == min_length: # 이미 더 적은 길이가 있어서 궂이 더 긴 길이가 확인이 필요없는 경우
                gems_count[gems[pos1]] -= 1
                pos1 += 1
                pos2 += 1
                gems_count[gems[pos2]] += 1
            else:
                pos2 += 1
                gems_count[gems[pos2]] += 1
        else:
            if pos2-pos1 < min_length:
                answer = [pos1+1, pos2+1]
                min_length = pos2-pos1
            gems_count[gems[pos1]] -= 1
            pos1 += 1
    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]) == [3, 7])
print(solution(["AA", "AB", "AC", "AA", "AC"]) == [1, 3])
print(solution(["XYZ", "XYZ", "XYZ"]) == [1, 1])
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]) == [1, 5])
