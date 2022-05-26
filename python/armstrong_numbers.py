# How can you make this more scalable and reusable later?
import functools as ft

def find_armstrong_numbers(numbers):
    armstrong_num = []

    # Checks if number in list is an armstrong number. If so, appends to armstrong_num list
    for num in numbers:
        if(test_for_armstrong(num) == True):
            armstrong_num.append(num)

    return armstrong_num

def test_for_armstrong(numbers):
    num_ls = [int(num) for num in str(numbers)] # separate each digit into a list
    num_raised = [num**len(num_ls) for num in num_ls]    # raise each num to the power of the amount of digits in the original number
    sum = (ft.reduce(lambda agg, num : agg + num, num_raised))   # use reduce() to aggregate all nums in the armstrong_num list
    if(sum == numbers):
        return True
    else:
        return False

# print(find_armstrong_numbers(list(range(0,20000))))
