n = int(input())

arr = list(map(int, input().split()))

arr.sort()

answer = 0

count = 0
for i in range(len(arr)):
    count += 1
    if count >= arr[i]:
        answer += 1
        count = 0

print(answer)