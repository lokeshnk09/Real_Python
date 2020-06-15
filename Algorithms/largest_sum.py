def largest(arr):
    if len(arr) == 0:
        return print('Too small')

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)

    return max_sum

print(largest([2,4,1,5,-1,5,-9,12,18]))
