
# def binary_search(array, value):
#     first_item = 0
#     last_item = len(array) - 1
#     found = False
#     while (first_item <= last_item and not found):
#         mid = (first_item + last_item) // 2
#         if array[mid] == value:
#             found = True
#         else:
#             if value < array[mid]:
#                 last_item = mid - 1
#             else:
#                 first_item = mid + 1
#     return found
#
#
# f = binary_search([1,2,4,7,6,9], 8)
#
# c = e, v in enumerate(
#


def contains(elements, value):
    left, right = 0, len(elements) - 1
    if left <= right:
        center = left + right // 2
        if elements[center] == value:
            return True
        if elements[center] > value:
            return contains(elements[center + 1], value)
        elif elements[center] < value:
            return contains(elements[:center], value)

    return False


s = contains()
