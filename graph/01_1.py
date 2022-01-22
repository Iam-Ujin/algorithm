# 음료수 얼려 먹기
from collections import deque


def ice_dfs_stack(grid):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    rows, cols = len(grid), len(grid[0])
    cnt = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '1' :
                continue

            cnt += 1
            stack = [(row,col)]

            while stack:
                x, y = stack.pop()
                grid[x][y] = '1'
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if nx < 0 or nx >= rows or ny < 0 or ny > cols :
                        continue
                    stack.append((nx, ny))

    return cnt




def ice_bfs(grid):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    rows, cols = len(grid), len(grid[0])
    cnt = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '1':
                continue

            cnt += 1
            q = deque([(row, col)])

            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx = x + dx[0]
                    ny = y + ny[0]

                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                        continue

                    grid[nx][ny] = '1'
                    q.append((nx, ny))
                    
    return cnt

