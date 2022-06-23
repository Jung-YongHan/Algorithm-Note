from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v+1)
graph = [[] for _ in range(v+1)]

for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = [] # 수행 결과를 담을 리스트
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]: # now와 연결된 노드들의 진입 차수 -1
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    print(*result)

topology_sort()