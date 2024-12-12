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
        
        corners = 0 # corners == sides

        for i, j in region:
            t = i == 0   or (i-1, j) not in region
            b = i == M-1 or (i+1, j) not in region
            l = j == 0   or (i, j-1) not in region
            r = j == N-1 or (i, j+1) not in region

            # outside corners
            if t and l: corners += 1
            if b and l: corners += 1
            if t and r: corners += 1
            if b and r: corners += 1
            
            # inside corners
            if not t and not l and (i-1, j-1) not in region: corners += 1
            if not b and not l and (i+1, j-1) not in region: corners += 1
            if not t and not r and (i-1, j+1) not in region: corners += 1
            if not b and not r and (i+1, j+1) not in region: corners += 1

        ans += corners * len(region)
print(ans)
