"""By Gideon Agyemang Prempeh
To complete the gravity assist, you need to determine what pair of inputs
produces the output 19690720."

The inputs should still be provided to the program by replacing the values at
addresses 1 and 2, just like before. In this program, the value placed in
address 1 is called the noun, and the value placed in address 2 is called the
verb. Each of the two input values will be between 0 and 99, inclusive.

Once the program has halted, its output is available at address 0, also
just like before. Each time you try a pair of inputs, make sure you first
reset the computer's memory to the values in the program (your puzzle input)
- in other words, don't reuse memory from a previous attempt.

Find the input noun and verb that cause the program to produce the output
19690720. What is 100 * noun + verb? (For example, if noun=12 and verb=2,
the answer would be 1202.)

Your puzzle answer was 7621.

"""
Code = [int(line) for line in open("opcode_num.txt").read().split(",")]
for noun in range(100):
    for verb in range(100):
        Program = [line for line in Code]
        Program[1] = noun
        Program[2] = verb
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
        plot = Program[0]

        num = 19690720
        answer = 100 * noun + verb
        if plot == num:
            print(answer)

