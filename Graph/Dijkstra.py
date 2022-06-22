import heapq
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
start = int(input())
INF = int(1e9)

# 노드 간의 간선의 개수가 한 개인 경우
graph = [[] for _ in range(v+1)]
for i in range(1, n+1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

distance = [INF] * (v+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))

for i in distance[1:]:
    if i == INF:
        print('INF')
    else:
        print(i)