def merge_sorted_array(array1, array2):
    merged_array = []
    if len(array1) == 0:
        return array2
    elif len(array2) == 0:
        return array1
    i = j = 0
    while (i < len(array1)) and (j < len(array2)):
        if array1[i] < array2[j]:
            merged_array.append(array1[i])
            i += 1
        else:
            merged_array.append(array2[j])
            j += 1
    merged_array = merged_array + array1[i:] + array2[j:]
    return merged_array


array1 = [0, 3, 4, 5]
array2 = [1, 2, 4, 4, 30, 37]
print(merge_sorted_array(array1, array2))
