import sys


line = sys.stdin.readline().strip()

floor = 0
for i, c in enumerate(line):
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1
    if floor == -1:
        print(i + 1)
        break
