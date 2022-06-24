from collections import deque

# 순서대로 정점의 개수, 간선의 개수, 시작 정점의 번호
n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) # 양방향

for j in range(1, n+1):
    graph[j].sort() # 정점 번호가 작은 순서대로 방문

visited = [False] * (n+1)
result = []
def bfs(start):
    q = deque([start])
    visited[start] = True
    result.append(start)

    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                result.append(i)

bfs(v)
print(*result)