from bisect import bisect_left, bisect_right

def bisect(nums, left, right):
    left_b = bisect_left(nums, left)
    right_b = bisect_right(nums, right)
    return right_b - left_b

n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

print(bisect(arr, m, m))