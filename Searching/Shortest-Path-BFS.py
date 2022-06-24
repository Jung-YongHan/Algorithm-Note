# 이 소스코드는 각 노드 간의 거리가 일정할 시에 사용할 수 있음 (1이라 가정)
from collections import deque
INF = int(1e9)

# 맵
n = int(input())
array = []
for i in range(n):
    array.append(list(map(int, input().split)))

# 현재 위치 및 방향
now_x, now_y = 0, 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#1. 현재 위치에서 모든 위치까지의 최단거리 테이블을 계산하여 리턴하는 함수
def bfs1():
    # 값이 -1이라면 도달할 수 없다는 의미
    dist = [[-1] * n for _ in range(n)]
    q = deque([(now_x, now_y)])
    dist[now_x][now_y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if dist[nx][ny] != -1: # 방문하지 않은 곳이라면
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

    return dist

#2. 0,0 에서 n,n까지 도달하는 최단거리를 리턴하는 함수 (출력 시 1을 더해야 함)
def bfs2(arr):
    q = deque([(0, 0)])
    arr[0][0] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= n-1 and 0 <= ny <= n-1:
                if arr[nx][ny] == 1: # 1은 이동 가능한 경로
                    arr[nx][ny] = arr[x][y] + 1
                    q.append((nx, ny))
    
    return arr[n-1][n-1] + 1

print(bfs2(array))
