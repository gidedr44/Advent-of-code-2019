"""By Gideon Agyemang Prempeh

An Elf just remembered one more important detail: the two adjacent matching
digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the
following are now true:

112233 meets these criteria because the digits never decrease and all repeated
digits are exactly two digits long.
123444 no longer meets the criteria (the repeated 44 is part of a larger
group of 444).
111122 meets the criteria (even though 1 is repeated more than twice,
it still contains a double 22).
How many different passwords within the range given in your puzzle
input meet all of the criteria?

Your puzzle input is still 246540-787419.

"""


def check_digits(num):
    count = 0
    for num1, num2 in zip(num, num[1:]):
        if num1 == num2:
            count += 1
        else:
            if count == 1:
                return True
            count = 0
    return count == 1

passcode = 0

for num in range(246540, 787419):
    num = str(num)
    if "".join(sorted(num)) == num:
        if check_digits(num):
            passcode += 1

words = "The passwords within the range given in the puzzle input that meet all of the criteria are"
print(words ,passcode)
