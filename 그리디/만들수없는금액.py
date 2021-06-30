n = int(input())

arr = list(map(int, input().split()))

arr.sort()

minv = 1

for a in arr:
    if minv < a:
        break
    minv += a
print(minv)