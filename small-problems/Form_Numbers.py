"""
Rearrange Array Elements so as to form two number such that their sum is maximum. 
Return these two numbers. 
You can assume that all array elements are in the range [0, 9]. 

for e.g. [1, 2, 3, 4, 5]
The expected answer would be [531, 42]. 
Another expected answer can be [542, 31]. 
In scenarios such as these when there are more than one possible answers, return any one.
"""

def quick_sort(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    quick_sort_recursive(input_list, 0, len(input_list)-1)

    
def quick_sort_recursive(input_list, left, right):
	if left >= right:
		return
	i = left
	p = right
	while i < p:
		if input_list[i] < input_list[p]:
			i += 1
		else:
			temp = input_list[p-1]
			pivot = input_list[p]
			front = input_list[i]

			input_list[p] = front
			input_list[i] = temp
			input_list[p-1] = pivot # this line has to be the last when i = p-1
			p -= 1

	quick_sort_recursive(input_list, left, p-1)
	quick_sort_recursive(input_list, p+1, right)


def list_to_num(num):
	num = [str(n) for n in num]
	num = int("".join(num))
	return num


def rearrange_digits(input_list):
	quick_sort(input_list)

	num1 = []
	num2 = []

	for i, n in enumerate(input_list):
		if i % 2 == 0:
			num1.append(n)
		else:
			num2.append(n)

	num1.reverse()
	num1 = list_to_num(num1)
	num2.reverse()
	num2 = list_to_num(num2)

	return [num1, num2]




def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

