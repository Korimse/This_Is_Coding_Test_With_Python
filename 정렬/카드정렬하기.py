import heapq

n = int(input())

arr = []
for i in range(n):
    heapq.heappush(arr, int(input()))

result = 0

while len(arr) > 1:
    one = heapq.heappop(arr)
    two = heapq.heappop(arr)
    sumv = one + two
    result += sumv
    heapq.heappush(arr, sumv)
print(result)
