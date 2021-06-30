n, c = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

left = arr[1] - arr[0]
right = arr[n-1] - arr[0]
result = 0

while left <= right:
    mid = (left+right)//2
    value = arr[0]
    count = 1

    for i in range(1, n):
        if arr[i] >= value + mid:
            value = arr[i]
            count += 1
    if count >= c:
        left = mid + 1
        result = mid
    else:
        right = mid-1
print(result)