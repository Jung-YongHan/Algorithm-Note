def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# v 노드의 개수, e 간선의 개수
v, e = map(int, input().split())

parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

# 거리 비용을 튜플의 첫 번째 원소로 받아 오름차순 정렬
edges = []
for i in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()

result = 0
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않은 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)