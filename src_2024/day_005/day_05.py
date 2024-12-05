def print_queue(print_rules, pt2=False) -> int:
    """Sorts print queue based on given rules

    Args:
        print_rules (str): rules and order sequence

    Returns:
        Sum of middle pages
    """
    rules, updates = print_rules.split("\n\n")
    rules = [[int(n) for n in rule.split("|")] for rule in rules.split("\n")]
    updates = [[int(n) for n in update.split(",")] for update in updates.split("\n")]
    valid_updates = []
    corrected_updates = []
    for update in updates:
        include = True
        for i in range(len(update)):
            before = [update[n] for n in range(i)]
            after = [update[n] for n in range(i + 1, len(update))]
            for n in after:
                for rule in rules:
                    if rule == [n, update[i]]:
                        include = False
            for n in before:
                for rule in rules:
                    if rule == [update[i], n]:
                        include = False
        if include:
            valid_updates.append(update)
        while not include:
            for i in range(len(update)):
                after = [update[n] for n in range(i + 1, len(update))]
                for n in after:
                    for rule in rules:
                        if rule == [n, update[i]]:
                            j = update.index(n)
                            update[i], update[j] = n, update[i]
                            continue
            corrected_updates.append(update)
            include = True
    middle_total = 0
    if pt2:
        for update in corrected_updates:
            middle = int((len(update) - 1) / 2)
            middle_total += update[middle]
        return middle_total
    for update in valid_updates:
        middle = int((len(update) - 1) / 2)
        middle_total += update[middle]
    return middle_total
