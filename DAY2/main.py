
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from login import get_input

input = get_input(2).splitlines()
lists = [[int(input_value) for input_value in input_line.split(" ")] for input_line in input]

def only_increasing(values: list, removed=False):
    for i in range(len(values)-1):
        dif = values[i+1] - values[i]
        if (dif < 1) or (dif > 3):
            if removed:
                return False
            else:
                new_values = values[:i + 1] + values[i + 2:]
                if only_increasing(new_values, removed=True):
                    return True
                new_values = values[:i] + values[i + 1:]
                if only_increasing(new_values, removed=True):
                    return True
                return False
    return True

def only_decreasing(values: list, removed=False):
    for i in range(len(values)-1):
        dif = values[i] - values[i+1]
        if (dif < 1) or (dif > 3):
            if removed:
                return False
            else:
                new_values = values[:i + 1] + values[i + 2:]
                if only_decreasing(new_values, removed=True):
                    return True
                new_values = values[:i] + values[i + 1:]
                if only_decreasing(new_values, removed=True):
                    return True
                return False
    return True
        
def is_safe(values: list, part2: bool):
    if part2:
        result = only_increasing(values, False) or only_decreasing(values, False)
    else:
        result = only_increasing(values, True) or only_decreasing(values, True)
    return result

# PART 1
c1 = 0
for values in lists:
    if is_safe(values, False):
        c1 += 1
print("(PART 1) The result is:", c1)

# PART 2
c2 = 0
for values in lists:
    if is_safe(values, True):
        c2 += 1
print("(PART 2) The result is:", c2)