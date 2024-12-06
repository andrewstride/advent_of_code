def guard_route(map):
    """calculate route of guard using given map

    Args:
        input map (str): map

    Returns:
        total of coordinates covered by guard (int)
    """
    map = map.split("\n")
    height = len(map)
    width = len(map[0])
    route_count = 1
    guard = ["<", "^", ">", "v"]
    for y in range(height):
        for x in range(width):
            if map[y][x] in guard:
                guard_pos = [y, x]
                guard_dir = guard[guard.index(map[y][x])]
                travelled = [[y, x]]
    edges = []
    for x in range(width):
        edges.append([0, x])
        edges.append([height - 1, x])
    for y in range(height):
        edges.append([width - 1, y])
        edges.append([y, 0])
    while guard_pos not in edges:
        match guard_dir:
            case "<":
                next_pos = [guard_pos[0], guard_pos[1] - 1]
            case "^":
                next_pos = [guard_pos[0] - 1, guard_pos[1]]
            case ">":
                next_pos = [guard_pos[0], guard_pos[1] + 1]
            case "v":
                next_pos = [guard_pos[0] + 1, guard_pos[1]]
        next_char = map[next_pos[0]][next_pos[1]]
        match next_char:
            case "#":
                index = guard.index(guard_dir)
                index = (index + 1) % 4
                guard_dir = guard[index]
            case "." | "^":
                if next_pos not in travelled:
                    route_count += 1
                guard_pos = next_pos
                travelled.append(guard_pos)
        if guard_pos in edges:
            return route_count
