
import os
import sys
import re
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from login import get_input

input = get_input(3)
values = input.split("mul(")
values2 = []
for n in values:
    if ")" in n:
        n = n.split(")")[0]
        values2.append(n)

result = 0
for n2 in values2:
    if len(n2.split(",")) == 2:
        number1, number2 = n2.split(",")[0], n2.split(",")[1]
        if number1.isdigit() and number2.isdigit():
            result += int(number1) * int(number2)
print("(PART 1) The result is:", result)

#split based on "don't" and "do"
values = re.split(r"(don't|do)", input)
values.insert(0, "do")

#create a new string with only "do" values
string = ""
for i, n in enumerate(values):
    if n == "do":
        string += values[i+1]

#apply same logic as part 1
values = string.split("mul(")
values2 = []
for n in values:
    if ")" in n:
        n = n.split(")")[0]
        values2.append(n)

result = 0
for n2 in values2:
    if len(n2.split(",")) == 2:
        number1, number2 = n2.split(",")[0], n2.split(",")[1]
        if number1.isdigit() and number2.isdigit():
            result += int(number1) * int(number2)
print("(PART 2) The result is:", result)