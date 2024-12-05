def wordsearch(input) -> int:
    """finds number of times 'XMAS' appears forwards, backwards, vertically up or down, or diagonally

    Args:
        input (str): wordsearch

    Returns:
        answer (int)
    """
    count = 0
    lines = [line.strip() for line in input.split("\n")]
    height = len(lines)
    width = len(lines[0])

    for y in range(height):
        for x in range(width):
            diag_se = ""
            diag_ne = ""
            hor = ""
            ver = ""
            if (y + 4) <= height and (x + 4) <= width:
                diag_se = "".join([lines[y + i][x + i] for i in range(4)])
            if (y - 3) >= 0 and (x + 4) <= width:
                diag_ne = "".join([lines[y - i][x + i] for i in range(4)])
            if (x + 4) <= width:
                hor = lines[y][x : x + 4]
            if (y + 4) <= height:
                ver = "".join([lines[y + i][x] for i in range(4)])
            count += [diag_ne, diag_se, hor, ver].count("XMAS")
            count += [diag_ne, diag_se, hor, ver].count("SAMX")
    return count


def x_mas(input) -> int:
    """finds number of times 'MAS' appears in X-shape

    Args:
        input (srt): wordsearch

    Returns:
        answer (int)"""
    count = 0
    lines = [line.strip() for line in input.split("\n")]
    height = len(lines)
    width = len(lines[0])

    for y in range(height):
        for x in range(width):
            diag_se = ""
            diag_ne = ""
            if (y + 3) <= height and (x + 3) <= width:
                diag_se = "".join([lines[y + i][x + i] for i in range(3)])
            if (y + 3) <= height and (x + 3) <= width:
                diag_ne = "".join([lines[y + (2 - i)][x + i] for i in range(3)])
            if diag_ne in ["MAS", "SAM"] and diag_se in ["MAS", "SAM"]:
                count += 1
    return count
