def get_second(time):
    hour_minute_second = list(map(int, time.split(":")))
    second = (
        hour_minute_second[0] * 3600
        + hour_minute_second[1] * 60
        + hour_minute_second[2]
    )
    return second


def get_time(second):
    hour = second // 3600
    minute = (second % 3600) // 60
    second = (second % 3600) % 60
    return f"{hour:02d}:{minute:02d}:{second:02d}"


def solution(play_time, adv_time, logs):
    db = [0] * get_second("100:0:0")
    play_sec = get_second(play_time)
    adv_sec = get_second(adv_time)

    for log in logs:
        start_finish_time = log.split("-")
        start_sec = get_second(start_finish_time[0])
        finish_sec = get_second(start_finish_time[1])
        db[start_sec] += 1
        db[finish_sec] -= 1

    for sec in range(0, play_sec):
        db[sec + 1] = db[sec] + db[sec + 1]

    start_sec = 0
    max_point = sum(db[0:adv_sec])
    current_point = max_point

    for sec in range(1, play_sec - adv_sec + 1):
        current_point -= db[sec - 1]
        current_point += db[adv_sec + sec - 1]
        if current_point > max_point:
            max_point = current_point
            start_sec = sec

    answer = get_time(start_sec)
    return answer


# def solution(play_time, adv_time, logs):
#     db = [0] * get_second("100:0:0")
#     play_sec = get_second(play_time)
#     adv_sec = get_second(adv_time)
#     logs = sorted(logs)
#     for log in logs:
#         start_finish_time = log.split("-")
#         start_sec = get_second(start_finish_time[0])
#         finish_sec = get_second(start_finish_time[1])
#         period_sec = finish_sec - start_sec
#         for sec in range(period_sec):
#             db[start_sec + sec] += 1

#     start_sec = 0
#     max_point = sum(db[start_sec:adv_sec])
#     current_point = max_point

#     for sec in range(1, play_sec - adv_sec + 1):
#         current_point -= db[sec - 1]
#         current_point += db[adv_sec + sec]
#         if current_point > max_point:
#             max_point = current_point
#             start_sec = sec

#     answer = get_time(start_sec)
#     return answer


print(
    solution(
        "02:03:55",
        "00:14:15",
        [
            "01:20:15-01:45:14",
            "00:40:31-01:00:00",
            "00:25:50-00:48:29",
            "01:30:59-01:53:29",
            "01:37:44-02:02:30",
        ],
    )
)
