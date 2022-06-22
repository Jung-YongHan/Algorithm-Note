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

parent = [0] * (n+1)
for i in range(1, v+1):
    parent[i] = i

# 각 노드 간의 연결 정보 입력
for i in range(e):
    a, b = map(int. input().split())
    union_parent(parent, a, b)

# 각 노드의 부모 노드 출력
print(*parent[1:])