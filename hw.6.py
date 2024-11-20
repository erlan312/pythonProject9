def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr
def binary_search(target, arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            print("Элемент найден на позиции:", mid)
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    print("Элемент не найден")
    return -1

numbers = [5, 2, 9, 1, 7, 6]
print("Изначальный список:", numbers)

sorted_numbers = bubble_sort(numbers)
print("Отсортированный список:", sorted_numbers)

binary_search(7, sorted_numbers)