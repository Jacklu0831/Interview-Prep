def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    # first find the max and min indiices 
    min_idx = 0
    minimum = input_list[0]
    for i, num in enumerate(input_list):
        if num < minimum:
            num = minimum
            min_idx = i
            break
    max_idx = min_idx - 1 if min_idx > 0 else len(input_list) - 1

    # then find which region it is (beginning of arr of max, or right of end of array)
    if number == input_list[0]:
        return 0
    elif number > input_list[0]:
        left = 0
        right = max_idx
    else:
        right = len(input_list) - 1
        left = min_idx

    # binary search in the area
    while left <= right:
        middle = (left + right)//2
        if input_list[middle] == number:
            return middle
        elif input_list[middle] < number:
            left = middle + 1
        else:
            right = middle - 1

    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])