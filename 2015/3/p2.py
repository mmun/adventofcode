import sys


line = sys.stdin.readline().strip()

ps = [[0, 0], [0, 0]]
seen = {(0, 0)}

for i, c in enumerate(line):
    p = ps[i % 2]
    
    if c == '^':
        p[1] += 1
    elif c == 'v':
        p[1] -= 1
    elif c == '>':
        p[0] += 1
    elif c == '<':
        p[0] -= 1
    
    seen.add(tuple(p))
    
print(len(seen))
