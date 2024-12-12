import sys

ans = 0
while line := sys.stdin.readline().strip():
    l, w, h = map(int, line.split('x'))
    ans += l*w*h + 2*min(l+w, w+h, h+l)
print(ans)
