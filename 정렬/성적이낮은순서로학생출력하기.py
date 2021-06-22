n = int(input())

arr = []
for i in range(n):
    data = input().split()
    arr.append((data[0], data[1]))

arr.sort(key=lambda x: x[1])

for ar in arr:
    print(ar[0], end=' ')