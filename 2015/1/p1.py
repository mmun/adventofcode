import sys


line = sys.stdin.readline().strip()

floor = 0
for c in line:
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1
print(floor)
