import sys
import collections
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
edges = []
dist = [INF] * (n+1)

for _ in range(m):
    u, v, w = map(int, input().split()) # 노드, 인접 노드, 가중치
    edges.append((u, v, w))

def bf(start):
    dist[start] = 0
    for i in range(n): # 정점 수만큼 반복
        for j in range(m):
            node = edges[j][0] # 현재 노드
            next_node = edges[j][1] # 인접 노드
            cost = edges[j][2] # 가중치
            if dist[node] != INF and dist[next_node] > dist[node] + cost:
                dist[next_node] = dist[node] + cost
                if i == n-1: # n-1번 이후 반복에도 값이 갱신되면 음수 순환 존재
                    return True
    return False

negative_cycle = bf(1)

if bf(1):
    print('-1')
else:
    for i in range(2, n+1):
        if dist[i] == INF:
            print('-1')
        else:
            print(dist[i])