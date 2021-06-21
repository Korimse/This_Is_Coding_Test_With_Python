n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
first = arr[0]
second = arr[1]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1
print(result)