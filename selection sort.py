def selection(arr):
    for i in range(len(arr)):
        min_ind = i
        for j in range(i+1, len(arr)):
           if arr[min_ind] > arr[j]:
               min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]
    return arr
arr = [2,17,5,13,19,23,21,4,7]
print(selection(arr))
