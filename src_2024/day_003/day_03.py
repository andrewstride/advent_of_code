import re


def regex_mul(input):
    """Decipher jumbled input string to multiply numbers

    Args:
        input (str): Puzzle input string

    Returns:
        multiplication result (int)
    """
    regex = r"mul\(\d+,\d+\)"
    mul_list = re.findall(regex, input)
    list_to_sum = []
    for item in mul_list:
        nums = re.findall("\d+", item)
        nums = [int(num) for num in nums]
        list_to_sum.append(nums[0] * nums[1])
    return sum(list_to_sum)


def regex_mul_pt2(input):
    """Decipher jumbled input string to multiply numbers, conditionally based on either being at the start, being after a "do()", and not after a "don't()".

    Args:
        input (str): Puzzle input string

    Returns:
        multiplication result (int)"""
    regex = r"""mul\(\d+,\d+\)|don't\(\)|do\(\)"""
    mul_list = re.findall(regex, input)
    list_to_sum = []
    do = True
    for item in mul_list:
        if item == """don't()""":
            do = False
        elif item == """do()""":
            do = True
        elif do:
            nums = re.findall("\d+", item)
            nums = [int(num) for num in nums]
            list_to_sum.append(nums[0] * nums[1])
    return sum(list_to_sum)
