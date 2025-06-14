def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# تست
numbers = [2, 3, 4, 5, 8]
target = 4

result = binary_search(numbers, target)
if result != -1:
    print(f"Number {target} found at index {result}")
else:
    print(f"Number {target} not found")
