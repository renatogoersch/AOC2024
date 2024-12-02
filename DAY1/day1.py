
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from login import get_input

input = get_input(1)

l1 = []
l2 = []
for i, line in enumerate(input.splitlines()):
    v1, v2 = line.split("   ")[0], line.split("   ")[1]
    l2.append(int(v1))
    l1.append(int(v2))

l1.sort()
l2.sort()
result1 = 0
for i, value in enumerate(l1):
    result1 += abs(value - l2[i])

print("(PART 1) The result is:", result1)

result2 = 0
for value in l1:
    count = l2.count(value)
    result2 += count * value

print("(PART 2) The result is:", result2)