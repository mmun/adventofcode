import sys

ans = 0
while line := sys.stdin.readline().strip():
    l, w, h = map(int, line.split('x'))
    ans += 2*(l*w + l*h + w*h) + min(l*w, w*h, h*l)
print(ans)
