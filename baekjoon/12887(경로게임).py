import sys

# get data
M = int(sys.stdin.readline())
DB = []
for _ in range(2):
  row = list(sys.stdin.readline())
  DB.append(row)
# get answer
answer = 0
before = "none"
for i in range(M):
  top = DB[0][i]
  bot = DB[1][i]
  if top=="#" and bot==".":
    if before == "top":
      answer -= 1
    before = "bot"
  elif top=="." and bot=="#":
    if before == "bot":
      answer -= 1
    before = "top"
  elif top=="." and bot==".":
    answer += 1
print(answer)