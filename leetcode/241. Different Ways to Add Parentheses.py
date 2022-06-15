from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        operator = {"+", "-", "*"}
        def get_available_list(string:str) -> set:
            available_list = list()
            if string.isdigit():
                available_list.append(int(string))
            else:
                for i, e in enumerate(string):
                  if e in operator:
                    for left in get_available_list(string[:i]):
                      for right in get_available_list(string[i+1:]):
                        if e == "+":
                          available_list.append(left + right)
                        elif e == "-":
                          available_list.append(left - right)
                        elif e == "*":
                          available_list.append(left * right)
            return available_list
        return get_available_list(expression)

print(Solution().diffWaysToCompute("2-1-1"))