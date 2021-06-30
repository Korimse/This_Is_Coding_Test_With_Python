n = int(input())

arr = list(map(int, input().split()))

left = 0
right = n-1

def binary_search(arr, left, right):
    while left <= right:
        mid = (left+right)//2
        
        if arr[mid] == mid:
            return mid
        
        elif arr[mid] > mid:
            right = mid - 1
        else:
            left = mid + 1

    return None

index = binary_search(arr, left, right)
if index == None:
    print(-1)
else:
    print(index)