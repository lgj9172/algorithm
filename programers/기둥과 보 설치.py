def is_valid(snapshot):
    for x, y, object_type in snapshot:
        # 기둥인 경우 바닥이거나, 아래에 기둥이 있거나, 앞 또는 현재 위치에 보가 있는 경우
        if object_type == 0:
            if (
                y == 0
                or (x, y - 1, 0) in snapshot
                or (x - 1, y, 1) in snapshot
                or (x, y, 1) in snapshot
            ):
                continue
            else:
                return False
        # 보인 경우 아래에 기둥이 있거나, 아래 오른쪽에 기둥이 있거나, 양쪽에 보가 있는 경우
        if object_type == 1:
            if (
                (x, y - 1, 0) in snapshot
                or (x + 1, y - 1, 0) in snapshot
                or ((x - 1, y, 1) in snapshot and (x + 1, y, 1) in snapshot)
            ):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    db = set()
    for build in build_frame:
        (
            x,
            y,
            object_type,
            order_type,
        ) = build  # 좌표(1~), 종류(0: 기둥, 1: 보), 명령(0: 삭제, 1: 설치)
        # 설치인 경우
        if order_type == 1:
            db.add((x, y, object_type))
            if not is_valid(db):
                db.discard((x, y, object_type))
        # 삭제인 경우
        if order_type == 0:
            db.discard((x, y, object_type))
            if not is_valid(db):
                db.add((x, y, object_type))
    answer = list(db)
    answer = sorted(answer, key=lambda x: (x[0], x[1], x[2]))
    return answer


print(
    solution(
        5,
        [
            [1, 0, 0, 1],
            [1, 1, 1, 1],
            [2, 1, 0, 1],
            [2, 2, 1, 1],
            [5, 0, 0, 1],
            [5, 1, 0, 1],
            [4, 2, 1, 1],
            [3, 2, 1, 1],
        ],
    )
)
