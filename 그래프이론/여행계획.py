n, m = map(int, input().split())

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

for i in range(n):
    graph = (list(map(int, input().split())))
    for j in range(n):
        if graph[j] == 1:
            union(parent, i+1, j+1)
            

trip = list(map(int, input().split()))

result = True
for i in range(m-1):
    if find_parent(parent, trip[i]) != find_parent(parent, trip[i+1]):
        result = False

print(parent)
if result:
    print("yes")
else:
    print("no")