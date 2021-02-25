from collections import defaultdict
from bisect import bisect_left

language = {"-": 0, "java": 1, "python": 2, "cpp": 3}

part = {"-": 0, "frontend": 1, "backend": 2}

level = {"-": 0, "junior": 1, "senior": 2}

food = {
    "-": 0,
    "pizza": 1,
    "chicken": 2,
}


def solution(info, query):
    answer = []
    info_dict = defaultdict(list)
    for i in info:
        i = i.split()
        for a in range(2):
            for b in range(2):
                for c in range(2):
                    for d in range(2):
                        aa = "-" if a == 0 else i[0]
                        bb = "-" if b == 0 else i[1]
                        cc = "-" if c == 0 else i[2]
                        dd = "-" if d == 0 else i[3]
                        info_dict[language[aa], part[bb], level[cc], food[dd]].append(
                            int(i[4])
                        )
    for key, value in info_dict.items():
        info_dict[key] = sorted(value)
    for q in query:
        q = q.split()
        point_list = info_dict[language[q[0]], part[q[2]], level[q[4]], food[q[6]]]
        count = len(point_list) - bisect_left(point_list, int(q[7]))
        answer.append(count)
    return answer


# def solution(info, query):
#     answer = []
#     nquery = []
#     for q in query:
#         q = q.split()
#         q = [language[q[0]], part[q[2]], level[q[4]], food[q[6]], int(q[7])]
#         nquery.append(q)
#     ninfo = []
#     for i in info:
#         i = i.split()
#         i = [language[i[0]], part[i[1]], level[i[2]], food[i[3]], int(i[4])]
#         ninfo.append(i)
#     for q in nquery:
#         count = 0
#         for i in ninfo:
#             if q[4] > i[4]:
#                 continue
#             if not (q[0] == i[0] or q[0] == 0):
#                 continue
#             if not (q[1] == i[1] or q[1] == 0):
#                 continue
#             if not (q[2] == i[2] or q[2] == 0):
#                 continue
#             if not (q[3] == i[3] or q[3] == 0):
#                 continue
#             count += 1
#         answer.append(count)
#     return answer


info = [
    "java backend junior pizza 150",
    "python frontend senior chicken 210",
    "python frontend senior chicken 150",
    "cpp backend senior pizza 260",
    "java backend junior chicken 80",
    "python backend senior chicken 50",
]
query = [
    "java and backend and junior and pizza 100",
    "python and frontend and senior and chicken 200",
    "cpp and - and senior and pizza 250",
    "- and backend and senior and - 150",
    "- and - and - and chicken 100",
    "- and - and - and - 150",
]
print(solution(info, query))