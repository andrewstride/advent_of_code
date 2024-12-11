def find_operators(input, pt2=False):
    """Finds which equations can be solved using plus and multiply operators

    Args:
        input (str): formatted 'answer: numbers to operate'

    Returns:
        number of successful equations (int)
    """
    equations = input.split("\n")
    valid = 0
    for equation in equations:
        answer, nums = int(equation.split(":")[0]), [
            int(num) for num in equation.split(":")[1].strip().split(" ")
        ]
        if is_valid(answer, nums, pt2):
            print(f"{answer=}")
            valid += answer

    return valid


def is_valid(answer, nums, pt2):
    if len(nums) == 1:
        return nums[0] == answer
    elif is_valid(answer, [nums[0] + nums[1]] + nums[2:], pt2):
        return True
    elif is_valid(answer, [nums[0] * nums[1]] + nums[2:], pt2):
        return True
    elif pt2 and is_valid(answer, [int(str(nums[0]) + str(nums[1]))] + nums[2:], pt2):
        return True
    else:
        return False
