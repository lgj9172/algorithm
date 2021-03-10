def minute(time_text):
    minute = int(time_text[0:2]) * 60
    minute += int(time_text[3:5])
    return minute


def solution(n, t, m, timetable):
    bus_timetable = [minute("09:00") + num * t for num in range(n)]
    crew_timetable = [minute(time) for time in sorted(timetable)]
    crew_index = 0
    answer = 0
    for bus_time in bus_timetable:
        count = 0
        # 현재 버스시간보다 빨리 도착해 있는 사람은 모두 탑승
        while crew_index <= len(crew_timetable) - 1:
            crew_time = crew_timetable[crew_index]
            if count < m and crew_time <= bus_time:
                count += 1
                crew_index += 1
            else:
                break
        # 이 버스가 가득차지 않았으면, 버스도착할때 동시에 도착하면된다.
        if count < m:
            answer = bus_time
        # 이 버스가 가득찼으면, 마지막 사람 오기 1분전에 줄선다.
        elif count == m:
            answer = crew_timetable[crew_index - 1] - 1
    h = answer // 60
    m = answer % 60
    return f"{h:02}:{m:02}"


print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))