n = int(input())

arr = list(map(int, input().split()))
arr.sort()

m = int(input())

problem = list(map(int, input().split()))

def binary(left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False

for p in problem:
    result = binary(0, n-1, p)
    if result == False:
        print('no', end = ' ')
    else:
        print('yes', end=' ')