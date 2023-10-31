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

fileA.write('B,'+RoomA+","+RoomB+","+RoomC+'\n\n')

Rooms = [RoomA, RoomB, RoomC]
point=0
robotStanding = "B"

def cleaning(robotStanding,RoomA,RoomB,RoomC,point,count):

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

while (count < 1000):
   robotStanding, RoomA, RoomB, RoomC, point, count = cleaning(robotStanding, RoomA, RoomB, RoomC, point, count)
   count+=1