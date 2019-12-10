"""By Gideon Agyemang Prempeh
Fuel required to launch a given module is based on its mass.
Specifically, to find the fuel required for a module, take its mass,
divide by three, round down, and subtract 2.

For example:

For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
For a mass of 14, dividing by 3 and rounding down still yields 4,
so the fuel required is also 2.
For a mass of 1969, the fuel required is 654.
For a mass of 100756, the fuel required is 33583.
The Fuel Counter-Upper needs to know the total fuel requirement.
To find it, individually calculate the fuel needed for the mass
of each module (your puzzle input), then add together all the fuel values.

What is the sum of the fuel requirements for all of the modules on your
spacecraft?
Your puzzle answer was 3380880
"""
import sys

nums_list=[]
f = open("sample_file.txt", "r")
for line in f.readlines():
    line = line.strip()
    line_flt = float(line)
    num = int(line_flt / 3 - 2)
    nums_list.append(num)
sum_of_mass = sum(nums_list)
print("The fuel needed for all the mass is", +sum_of_mass)