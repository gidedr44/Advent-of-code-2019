"""By Gideon Agyemang Prempeh

In the above example, the intersection closest to the central port is reached after 8+5+5+2 = 20 steps by the first wire and 7+6+4+3 = 20 steps by the second wire for a total of 20+20 = 40 steps.

However, the top-right intersection is better: the first wire takes only 8+5+2 = 15 and the second wire takes only 7+6+2 = 15, a total of 15+15 = 30 steps.

Here are the best steps for the extra examples from above:

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = 610 steps
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = 410 steps

What is the fewest combined steps the wires must take to reach an intersection?

"""
sec1,sec2 = open("distance.txt").read().split("\n")
sec1,sec2 = [line.split(",") for line in [sec1,sec2]]

def movement_num(run):
    x = y = steps = 0
    daythree = {}

    for num in run:
        direction = num[0]
        space = int(num[1:])
        direction_x = direction_y = 0
        if direction == "U":
            direction_y = 1
        elif direction == "D":
            direction_y = -1
        elif direction == "R":
            direction_x = 1
        elif direction == "L":
            direction_x = -1
        else:
            break
        
        for _ in range(space):
            x += direction_x
            y += direction_y
            steps += 1
            pay = (x,y)

            if pay not in daythree:
                daythree[pay] = steps
    return daythree

path_A = movement_num(sec1)
path_B = movement_num(sec2)
path_AB = set(path_A)&set(path_B)


def inter_sec():
    return min([path_A[pay] + path_B[pay] for pay in path_AB])

lay = inter_sec()
words = "The fewest combined steps it takes to reach an intersection is"
print(words,lay )
