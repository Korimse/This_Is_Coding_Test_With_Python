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
parent = [0]*(n+1)
for i in range(1, n+1):
    parent[i] = i

result = 0

ga = []

for i in range(m):
    a, b, c = map(int, input().split())
    ga.append((a, b, c))

ga.sort(key=lambda x:x[2])
total = 0

for g in ga:
    a, b, c = g
    total += c
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        result += c
print(total - result)