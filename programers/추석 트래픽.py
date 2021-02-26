import pprint


def solution(lines):
    db = []
    for line in lines:
        hour = int(line[11:13])
        minute = int(line[14:16])
        second = float(line[17:23])
        period = float(line.split()[-1][:-1])
        finish_sec = hour * 3600 + minute * 60 + second
        start_sec = finish_sec - period + 0.001
        db.append((start_sec, "start"))
        db.append((finish_sec, "finish"))
    db = sorted(sorted(db, key=lambda x: x[1], reverse=True), key=lambda x: x[0])
    answer = 0
    count = 0
    for time, sign in db:
        if sign == "start":
            count += 1
        count2 = len([e for e in db if time < e[0] < time + 1 and e[1] == "start"])
        answer = max(answer, count + count2)
        if sign == "finish":
            count -= 1
    pprint.pprint(db)
    return answer


print(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))
