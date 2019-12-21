"""By Gideon Agyemang Prempeh
An Intcode program is a list of integers separated by commas (like 1,0,0,3,99).
To run one, start by looking at the first integer (called position 0).
Here, you will find an opcode - either 1, 2, or 99. The opcode indicates what
to do; for example, 99 means that the program is finished and should immediately
halt. Encountering an unknown opcode means something went wrong.
Opcode 1 adds together numbers read from two positions and stores the result
in a third position. The three integers immediately after the opcode tell you
these three positions - the first two indicate the positions from which you
should read the input values, and the third indicates the position at which the
output should be stored.

For the purposes of illustration, here is the same program split into multiple
lines:

1,9,10,3,
2,3,11,0,
99,
30,40,50

The first four integers, 1,9,10,3, are at positions 0, 1, 2, and 3. Together,
they represent the first opcode (1, addition), the positions of the two
inputs (9 and 10), and the position of the output (3).
To handle this opcode, you first need to get the values at the input positions:
position 9 contains 30, and position 10 contains 40. Add these numbers together
to get 70. Then, store this value at the output position; here, the output
position (3) is at position 3, so it overwrites itself. Afterward, the program
looks like this:

1,9,10,70,
2,3,11,0,
99,
30,40,50

Step forward 4 positions to reach the next opcode, 2. This opcode works just
like the previous, but it multiplies instead of adding. The inputs are at
positions 3 and 11; these positions contain 70 and 50 respectively.
Multiplying these produces 3500; this is stored at position 0:

3500,9,10,70,
2,3,11,0,
99,
30,40,50

Stepping forward 4 more positions arrives at opcode 99, halting the program.

Here are the initial and final states of a few more small programs:
1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99.

Replace position 1 with the value 12 and replace position 2 with the value 2.
What value is left at position 0 after the program halts?

Your puzzle answer was 3306701.

"""
Program = [int(line) for line in open("output_opcode.txt").read().split(",")]
Program[1] = 12
Program[2] =2
position = 0

while Program[position] != 99:
    opcode = Program[position]
    Day1,Day2,Day3 = Program[position+1],Program[position+2],Program[position+3]
    if opcode == 1:
        Program[Day3] = Program[Day1]+Program[Day2]
    elif opcode == 2:
        Program[Day3] = Program[Day1]*Program[Day2]
    else:
        break
    position += 4
answer = Program[0]
print("The left at position 0 after the program halts is",+answer )

