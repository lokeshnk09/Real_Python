def bubble_sort(array):
    n = len(array)


    for i in range(n):
        already_sorted = True
        for j in range(n-i -1):
            # print(array[j])
            if array[j] > array[j + 1]:
                array[j], array[j+1] = array[j+1], array[j]
                already_sorted = False
        if already_sorted:
            break

    return array


s = bubble_sort([8, 2, 6, 4, 5])
print(s)
