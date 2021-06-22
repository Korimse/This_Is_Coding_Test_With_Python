n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)

for ar in arr:
    print(ar, end=' ')