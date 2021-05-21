def solution(n, k, cmd):
    db = [e for e in range(n)]
    db2 = ["O" for e in range(n)]
    cursor = k
    delete_stack = []
    for command in cmd:
        if command.startswith("D"):
            cursor += int(command[2:])
        elif command.startswith("U"):
            cursor -= int(command[2:])
        elif command.startswith("C"):
            target = db[cursor]
            del(db[cursor])
            delete_stack.append(target)
            if cursor == len(db):
                cursor -= 1
        elif command.startswith("Z"):
            current = db[cursor]
            target = delete_stack.pop()
            if target < current:
                cursor += 1
            db.append(target)
            db = sorted(db)
    answer = ["X" for i in range(n)]
    for data in db:
        answer[data] = "O"
    return "".join(answer)


# print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))