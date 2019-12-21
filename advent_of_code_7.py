"""By Gideon Agyemang Prempeh

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?

Your puzzle input is 246540-787419.

"""


def times_repeated(num):
    for pay1, pay2 in zip(num, num[1:]):
        if pay1 == pay2:
            return True

passcode = 0

for num in range(246540, 787419):
    num = str(num)
    if "".join(sorted(num)) == num:
        if times_repeated(num):
            passcode += 1
words = "The passwords within the range given in the puzzle input that meet all of the criteria are"
print(words ,passcode)



