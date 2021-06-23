def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n+1)

edges = []
result = 0

for i in range(1, n+1):
    parent[i] = i

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

edges.sort(key=lambda x : x[2])
last = 0

for edge in edges:
    a, b, c = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        result += c
        last = c

print(result - last)