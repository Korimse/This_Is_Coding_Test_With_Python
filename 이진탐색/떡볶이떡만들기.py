n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

left = 0
right = arr[n-1]
answer = 0

while left <= right:
    mid = (left + right) // 2
    ran = 0
    for i in range(len(arr)):
        if arr[i] - mid > 0:
           ran += arr[i] - mid
    
    if ran == m:
        answer = mid
        break
    elif ran > m:
        left = mid + 1
        answer = mid
    else:
        right = mid - 1
print(answer)