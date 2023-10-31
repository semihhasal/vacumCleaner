import random

RoomA = "D"
RoomB = "D"
RoomC = "D"

fileA = open('C:/Users/Semih/PycharmProjects/vacumCleaner/a.txt', 'w')
fileB = open('C:/Users/Semih/PycharmProjects/vacumCleaner/b.txt', 'w')

pA = 0.3
pB = 0.3
pC = 0.3

Probility = random.random()

count = 0;
print(Probility)

fileA.write('B,' + RoomA + "," + RoomB + "," + RoomC + '\n\n')

point = 0
robotStanding = "B"
comingFrom =  ""


def cleaning(robotStanding, RoomA, RoomB, RoomC, point, count):
    if (robotStanding == "B"):
        if (RoomB == "D"):
            fileA.write("suck\n\n")
            point += 1
            RoomB = "C"
            fileA.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
            count += 1
    if (robotStanding == "A"):
        if (RoomA == "D"):
            fileA.write("suck\n\n")
            point += 1
            RoomA = "C"
            fileA.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
            count += 1
    if (robotStanding == "C"):
        if (RoomC == "D"):
            fileA.write("suck\n\n")
            point += 1
            RoomC = "C"
            fileA.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
            count += 1
    return robotStanding, RoomA, RoomB, RoomC, point, count


def movement(robotStanding, RoomA, RoomB, RoomC, count, comingFrom):

    if (robotStanding == "B"):
        if (comingFrom == ""):
            fileA.write("right\n\n")
            robotStanding = "C"
            count+=1
            comingFrom = "B"
            fileA.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
        if(comingFrom == "A"):
            fileA.write("right\n\n")
            robotStanding = "C"
            count+=1
            comingFrom = "B"
            fileA.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
        if (comingFrom == "C"):
            fileA.write("left\n\n")
            robotStanding = "A"
            count += 1
            comingFrom = "B"
            fileA.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
        return robotStanding, RoomA, RoomB, RoomC, count, comingFrom
    if (robotStanding == "A"):
        if (comingFrom == "B"):
            fileA.write("right\n\n")
            robotStanding = "B"
            count += 1
            comingFrom = "A"
            fileA.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
        return robotStanding, RoomA, RoomB, RoomC, count, comingFrom
    if (robotStanding == "C"):
        if (comingFrom == "B"):
            fileA.write("left\n\n")
            robotStanding = "B"
            count += 1
            comingFrom = "C"
            fileA.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
        return robotStanding, RoomA, RoomB, RoomC, count, comingFrom



while (count < 1000):
    robotStanding, RoomA, RoomB, RoomC, point, count = cleaning(robotStanding, RoomA, RoomB, RoomC, point, count)
    robotStanding, RoomA, RoomB, RoomC, count,comingFrom = movement(robotStanding, RoomA, RoomB, RoomC, count,comingFrom)
    count += 1


fileA.write(str(point))
