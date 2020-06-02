def insertion_sort(array):
    # Loop from the second element of the array until
    # the last element
    for i in range(1, len(array)):
        # This is the element we want to position in its
        # correct place
        key_item = array[i]


        # Initialize the variable that will be used to
        # find the correct position of the element referenced
        # by `key_item`
        j = i - 1
        while j >= 0 and array[j] > key_item:
            array[j+1] = array[j]
            j-=1
        array[j+1] = key_item

    return array


s = insertion_sort([8, 2, 6, 4, 5])
print(s)