
def minimumTime(ability, processes):
    # make a modest guess of what the days may be, and use it as a starting point
    efficiency = [1.0 / x for x in ability]
    lower_bound = int(processes / sum(efficiency)) - 1
    upper_bound = lower_bound + max(ability) + 1

    while lower_bound < upper_bound - 1:
        days = (lower_bound + upper_bound) // 2
        produce = sum([days // x for x in ability])
        if produce >= processes:
            upper_bound = days
        elif produce < processes:
            lower_bound = days

    return upper_bound


if __name__ == "__main__":
    print(minimumTime([2, 4, 2, 3, 1], 15))