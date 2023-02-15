# from itertools import count, product


# def solution(n):
#     P = product(["(", ")"], repeat=n * 2)
#     answer = 0
#     for candidate in filter(lambda e: e.count("(") == n, P):
#         start = 0
#         finish = 0
#         fail = False
#         for character in candidate:
#             if character == "(":
#                 start += 1
#             elif character == ")":
#                 finish += 1
#             if start < finish or start > n:
#                 fail = True
#                 break
#         if fail == False and start == finish:
#             answer += 1
#     return answer


# print(solution(12))

# ------------------------------------------------------------

answer = 0


def solution(n):
    dfs(0, 0, n)
    global answer
    return answer


def dfs(start, finish, n):
    if start < finish or start > n:
        return
    if start == n and finish == n:
        global answer
        answer += 1
    dfs(start + 1, finish, n)
    dfs(start, finish + 1, n)


print(solution(14))


# -------------------------------------------------------


# def solution(n):
#     answer = [[] for _ in range(n + 1)]
#     answer[1] = [1, 1]
#     for i in range(2, n + 1):
#         temp = [1]
#         for j in range(1, len(answer[i - 1])):
#             temp.append(answer[i - 1][j] + temp[j - 1])
#         temp.append(answer[i - 1][j] + temp[j - 1])
#         answer[i] = temp
#     print(answer)
#     return answer[n][-1]


# print(solution(3))