def solution(s):
    tuple_list = s[2:-2].split("},{")
    tuple_list = [e.split(",") for e in tuple_list]
    tuple_list = sorted(tuple_list, key=lambda x: len(x))
    history_set = set()
    answer = []
    for tuple in tuple_list:
        result = set(tuple) - history_set
        answer.append(int(result.pop()))
        history_set = set(tuple)
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")==[2, 1, 3, 4])