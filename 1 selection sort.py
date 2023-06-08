def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Test the function
input_list = [5, 416, 54, 21, 6135, 15, 741]
sorted_list = selection_sort(input_list)
print(sorted_list)
