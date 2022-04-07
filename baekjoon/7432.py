import sys

def count_same_length(arr1, arr2):
  count = 0
  for i in range(min(len(arr1),len(arr2))):
    if arr1[i] == arr2[i]:
      count += 1
    else:
      break
  return count

def solution():
  input = sys.stdin.readline
  print = sys.stdout.write
  N = int(input())
  files = [input().rstrip().split("\\") for _ in range(N)]
  files = sorted(files)
  before_file = []
  for current_file in files:
    same_length = count_same_length(before_file, current_file)
    space = " " * same_length
    for i in range(same_length, len(current_file)):
      print(space + current_file[i])
      space += " "
    before_file = current_file
  
solution()