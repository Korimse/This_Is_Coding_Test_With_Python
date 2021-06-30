n, m = map(int, input().split())

data = list(map(int, input().split()))

arr = [0] * (m+1)

for d in data:
    arr[d] += 1

result = 0

for i in range(1, m+1):
    n -= arr[i]
    result += arr[i] * n

print(result)