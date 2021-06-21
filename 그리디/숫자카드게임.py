n, m = map(int, input().split())
result = 0
for i in range(n):
    arr = list(map(int, input().split()))
    arr.sort()
    result = max(result, arr[0])
print(result)