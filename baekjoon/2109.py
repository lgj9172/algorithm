import sys

input = sys.stdin.readline

n = int(input())
pay_day_list = [tuple(map(int, input().split())) for _ in range(n)]


print(pay_day_list)
