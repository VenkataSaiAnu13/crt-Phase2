def insertion(arr):
    for i in range(1, len(arr)):
        j = 1
        while arr[j-1] > arr[j] and j >0:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j = -1
    return arr
arr = [5,2,4,3,1,7]
print(insertion(arr))