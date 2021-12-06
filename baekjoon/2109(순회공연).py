import heapq

n = int(input())
pay_day_list = [tuple(map(int, input().split())) for _ in range(n)]
pay_day_list.sort(key=lambda e: e[1])
pay_list = []
delete_count = 0
day_count = 0
for pay, day in pay_day_list:
    day_count += 1
    heapq.heappush(pay_list, pay)
    if day_count-delete_count > day:
        heapq.heappop(pay_list)
        delete_count += 1
print(sum(pay_list))
