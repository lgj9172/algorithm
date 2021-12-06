def solution(array, order):
    count = 0
    order_set = set(order)
    narray = []
    for e in array:
        # 순서를 바꿔야 하는 원소면 order에 있는 값으로 변경
        if e in order_set:
            narray.append(order[count])
            count += 1
        # 바꾸지 않아도 되면 그대로
        else:
            narray.append(e)
    return narray


print(solution(["a", "e", "g", "h", "j", "w",
      "s", "d", "q"], ["s", "w", "q", "h"]))
