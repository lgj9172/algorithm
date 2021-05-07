from itertools import permutations


def solution(expression):
    nexpression = []
    operand = ""
    # 식을 배열로 구분하기
    for index, char in enumerate(expression):
        if char in "0123456789":
            operand += char
        elif char in "+-*":
            nexpression.append(operand)
            nexpression.append(char)
            operand = ""
        if index == len(expression) - 1:
            nexpression.append(operand)
    # 모든 경우의수에서 최대값 구하기
    MAX = 0
    for priority in permutations("+-*"):
        nnexpression = nexpression[:]
        for operation in priority:
            while operation in nnexpression:
                operation_index = nnexpression.index(operation)
                result = eval("".join(nnexpression[operation_index-1:operation_index+2]))
                nnexpression = nnexpression[:operation_index-1] + [str(result)] + nnexpression[operation_index+2:]
        MAX = max(MAX, abs(int(nnexpression[0])))
    answer = MAX
    return answer

print(solution("100-200*300-500+20") == 60420)
print(solution("50*6-3*2") == 300)