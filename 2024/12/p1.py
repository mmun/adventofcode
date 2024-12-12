import sys

grid = []
while line := sys.stdin.readline().strip():
    grid.append(list(line))

M = len(grid)
N = len(grid[0])
DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(start, seen):
    region = set()
    
    queue = [start]
    while queue:
        i, j = queue.pop()

        if (i, j) in seen:
            continue
        
        seen.add((i, j))
        region.add((i, j))
        for di, dj in DIRS:
            ni, nj = i + di, j + dj
            if 0 <= ni < M and 0 <= nj < N and grid[ni][nj] == grid[i][j]:
                if (ni, nj) not in seen:
                    queue.append((ni, nj))

    return region

seen = set()
ans = 0
for i0 in range(M):
    for j0 in range(N):
        if (i0, j0) in seen:
            continue

        region = dfs((i0, j0), seen)
        
        perimeter = 0

        for i, j in region:
            t = i == 0   or (i-1, j) not in region
            b = i == M-1 or (i+1, j) not in region
            l = j == 0   or (i, j-1) not in region
            r = j == N-1 or (i, j+1) not in region

            if t: perimeter += 1
            if b: perimeter += 1
            if l: perimeter += 1
            if r: perimeter += 1

        ans += perimeter * len(region)
print(ans)