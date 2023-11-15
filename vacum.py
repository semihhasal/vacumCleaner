import random
import os

RoomA = "D"
RoomB = "D"
RoomC = "D"

fileA = open('./a.txt', 'w')


pA = 0.3
pB = 0.3
pC = 0.3

Probility = random.random()

count = 0;
print(Probility)
Probility=random.random()
print(Probility)


fileA.write(f"Step : {1} \n\n")


point = 0
countA=0
countC=0
dirtyA=0
dirtyC=0


robotStanding = "B"
comingFrom =  ""


def cleaning(robotStanding, RoomA, RoomB, RoomC, point, count,countA,countC,dirtyA,dirtyC):
    Probility=random.random()

    if (robotStanding == "B"):
        while(RoomB == "D"):
            fileA.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
            fileA.write("suck\n\n")
            RoomB = "C"
            RoomA, RoomB, RoomC, point = pointing(RoomA, RoomB, RoomC, point)
            count += 1
            fileA.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
            fileA.write(str(point) + "\n\n")
            fileA.write(f"Step : {count+1} \n\n")
            Probility = random.random()
            while(pB>Probility):
                RoomB = "D"  ## room dirty again
                fileA.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
                fileA.write("suck\n\n")
                RoomB = "C" ##clean again
                RoomA, RoomB, RoomC, point = pointing(RoomA, RoomB, RoomC, point)
                count += 1
                fileA.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
                fileA.write(str(point) + "\n\n")
                fileA.write(f"Step : {count+1} \n\n")
                Probility = random.random()
        if(pA>Probility and RoomA=="C"):
                RoomA="D"
        if(pC>Probility and RoomC=="C"):
                RoomC="D"


    if (robotStanding == "A"):
        while (RoomA == "D"):
            fileA.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
            dirtyA += 1 ##count for ML
            fileA.write("suck\n\n")
            RoomA = "C"
            RoomA, RoomB, RoomC, point = pointing(RoomA, RoomB, RoomC, point)
            count += 1
            fileA.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
            fileA.write(str(point) + "\n\n")
            fileA.write(f"Step : {count+1} \n\n")
            Probility = random.random()
            while (pA > Probility):
                RoomA = "D"  ## room dirty again
                countA +=1  ## room need clean again
                dirtyA +=1  ## room is dirty
                fileA.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
                fileA.write("suck\n\n")
                RoomA = "C"  ##clean again
                RoomA, RoomB, RoomC, point = pointing(RoomA, RoomB, RoomC, point)
                count += 1
                fileA.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
                fileA.write(str(point) + "\n\n")
                fileA.write(f"Step : {count+1} \n\n")
                Probility = random.random()
        if (pB > Probility and RoomB == "C"):
                RoomB = "D"
        if (pC > Probility and RoomC == "C"):
                RoomC = "D"

    if (robotStanding == "C"):
        while (RoomC == "D"):
            fileA.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
            dirtyC += 1  ##count for ML
            fileA.write("suck\n\n")
            RoomC = "C"
            RoomA, RoomB, RoomC, point = pointing(RoomA, RoomB, RoomC, point)
            count += 1
            fileA.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
            fileA.write(str(point)+"\n\n")
            fileA.write(f"Step : {count+1} \n\n")
            Probility = random.random()
            while (pC > Probility):
                RoomC = "D"  ## room dirty again
                countC += 1  ## room need clean again
                dirtyC += 1  ## room is dirty
                fileA.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
                fileA.write("suck\n\n")
                RoomC = "C"  ##clean again
                RoomA, RoomB, RoomC, point = pointing(RoomA, RoomB, RoomC, point)
                count += 1
                fileA.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
                fileA.write(str(point)+"\n\n")
                fileA.write(f"Step : {count+1} \n\n")
                Probility = random.random()
        if (pA > Probility and RoomA == "C"):
                RoomA = "D"
        if (pB > Probility and RoomB == "C"):
                RoomB = "D"


    return robotStanding, RoomA, RoomB, RoomC, point, count,countA,countC,dirtyA,dirtyC


def movement(robotStanding, RoomA, RoomB, RoomC,point,count,comingFrom,countA,countC,dirtyA,dirtyC):
    Probility = random.random()

    if (robotStanding == "B" and count<=150):
        if (comingFrom == ""):
            fileA.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
            fileA.write("right\n\n")
            robotStanding = "C"
            countC+=1
            count+=1
            RoomA, RoomB, RoomC, point = pointing(RoomA, RoomB, RoomC, point)
            fileA.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
            fileA.write(str(point)+"\n\n")
            fileA.write(f"Step : {count+1} \n\n")
            comingFrom = "B"
            if (pA > Probility and RoomA == "C"):
                RoomA = "D"
            if (pB > Probility and RoomB == "C"):
                RoomB = "D"
            if (pC > Probility and RoomC == "C"):
                RoomC = "D"
        if(comingFrom == "A"):
            fileA.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
            fileA.write("right\n\n")
            robotStanding = "C"
            countC += 1
            count+=1
            RoomA, RoomB, RoomC, point = pointing(RoomA, RoomB, RoomC, point)
            fileA.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
            fileA.write(str(point) + "\n\n")
            fileA.write(f"Step : {count+1} \n\n")
            comingFrom = "B"
            if (pA > Probility and RoomA == "C"):
                RoomA = "D"
            if (pB > Probility and RoomB == "C"):
                RoomB = "D"
            if (pC > Probility and RoomC == "C"):
                RoomC = "D"
        if (comingFrom == "C"):
            fileA.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
            fileA.write("left\n\n")
            robotStanding = "A"
            countA += 1
            count += 1
            RoomA, RoomB, RoomC, point = pointing(RoomA, RoomB, RoomC, point)
            fileA.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
            fileA.write(str(point)+"\n\n")
            fileA.write(f"Step : {count+1} \n\n")
            comingFrom = "B"
            if (pA > Probility and RoomA == "C"):
                RoomA = "D"
            if (pB > Probility and RoomB == "C"):
                RoomB = "D"
            if (pC > Probility and RoomC == "C"):
                RoomC = "D"
        return robotStanding, RoomA, RoomB, RoomC, point, count, comingFrom, countA, countC, dirtyA, dirtyC

    elif(robotStanding == "B" and count>150):
         if(countA-dirtyA > countC-dirtyC):
             fileA.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
             fileA.write("right\n\n")
             robotStanding = "C"
             countC += 1
             count += 1
             RoomA, RoomB, RoomC, point = pointing(RoomA, RoomB, RoomC, point)
             fileA.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
             fileA.write(str(point) + "\n\n")
             fileA.write(f"Step : {count+1} \n\n")
             comingFrom = "B"
             if (pA > Probility and RoomA == "C"):
                 RoomA = "D"
             if (pB > Probility and RoomB == "C"):
                 RoomB = "D"
             if (pC > Probility and RoomC == "C"):
                RoomC = "D"

         else:
             fileA.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
             fileA.write("left\n\n")
             robotStanding = "A"
             countA += 1
             count += 1
             RoomA, RoomB, RoomC, point = pointing(RoomA, RoomB, RoomC, point)
             fileA.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
             fileA.write(str(point) + "\n\n")
             fileA.write(f"Step : {count+1} \n\n")
             comingFrom = "B"
             if (pA > Probility and RoomA == "C"):
                 RoomA = "D"
             if (pB > Probility and RoomB == "C"):
                 RoomB = "D"
             if (pC > Probility and RoomC == "C"):
                 RoomC = "D"


         return robotStanding, RoomA, RoomB, RoomC, point, count, comingFrom, countA, countC, dirtyA, dirtyC


    if (robotStanding == "A"):
        if (comingFrom == "B"):
            fileA.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
            fileA.write("right\n\n")
            robotStanding = "B"
            count += 1
            RoomA, RoomB, RoomC, point = pointing(RoomA, RoomB, RoomC, point)
            fileA.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
            fileA.write(str(point) + "\n\n")
            fileA.write(f"Step : {count + 1} \n\n")
            comingFrom = "A"

        return robotStanding, RoomA, RoomB, RoomC, point, count, comingFrom, countA, countC, dirtyA, dirtyC
    if (robotStanding == "C"):
        if (comingFrom == "B"):
            fileA.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
            fileA.write("left\n\n")
            robotStanding = "B"
            count += 1
            RoomA, RoomB, RoomC, point = pointing(RoomA, RoomB, RoomC, point)
            fileA.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
            fileA.write(str(point) + "\n\n")
            fileA.write(f"Step : {count+1} \n\n")
            comingFrom = "C"

        return robotStanding, RoomA, RoomB, RoomC, point,count, comingFrom,countA,countC,dirtyA,dirtyC



def pointing(RoomA,RoomB,RoomC,point):
    if (RoomA=="C"):
        point += 1
    if (RoomB == "C"):
        point += 1
    if (RoomC == "C"):
        point += 1

    return  RoomA,RoomB,RoomC,point


while (count < 999):
    robotStanding, RoomA, RoomB, RoomC, point, count, countA, countC, dirtyA, dirtyC = cleaning(robotStanding, RoomA, RoomB, RoomC, point, count,countA,countC,dirtyA,dirtyC)
    robotStanding, RoomA, RoomB, RoomC,point,count, comingFrom,countA,countC,dirtyA,dirtyC = movement(robotStanding, RoomA, RoomB, RoomC, point,count,comingFrom,countA,countC,dirtyA,dirtyC)



fileA.write(str(point))
