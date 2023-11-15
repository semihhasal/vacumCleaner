import random
import os

RoomA = "D"
RoomB = "D"
RoomC = "D"

fileB = open('./b.txt', 'w')


pA = 0.3
pB = 0.3
pC = 0.3

Probility = random.random()

count = 0;
print(Probility)
Probility=random.random()
print(Probility)


fileB.write(f"Step : {1} \n\n")
fileB.write('B,' + RoomA + "," + RoomB + "," + RoomC + '\n\n')

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
            fileB.write("suck\n\n")
            point += 1
            RoomB = "C"
            count += 1
            fileB.write(str(point) + "\n\n")
            fileB.write(f"Step : {count+1} \n\n")
            Probility = random.random()
            fileB.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
            while(pB>Probility):
                RoomB = "D"  ## room dirty again
                fileB.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
                fileB.write("suck\n\n")
                point += 1
                RoomB = "C" ##clean again
                count += 1
                fileB.write(str(point) + "\n\n")
                fileB.write(f"Step : {count+1} \n\n")
                Probility = random.random()
        if(pA>Probility and RoomA=="C"):
                RoomA="D"
        if(pC>Probility and RoomC=="C"):
                RoomC="D"


    if (robotStanding == "A"):
        while (RoomA == "D"):
            dirtyA += 1 ##count for ML
            fileB.write("suck\n\n")
            point += 1
            RoomA = "C"
            count += 1
            fileB.write(str(point) + "\n\n")
            fileB.write(f"Step : {count+1} \n\n")
            Probility = random.random()
            fileB.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
            while (pA > Probility):
                RoomA = "D"  ## room dirty again
                countA +=1  ## room need clean again
                dirtyA +=1  ## room is dirty
                fileB.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
                fileB.write("suck\n\n")
                point += 1
                RoomA = "C"  ##clean again
                count += 1
                fileB.write(str(point) + "\n\n")
                fileB.write(f"Step : {count+1} \n\n")
                Probility = random.random()
        if (pB > Probility and RoomB == "C"):
                RoomB = "D"
        if (pC > Probility and RoomC == "C"):
                RoomC = "D"

    if (robotStanding == "C"):
        while (RoomC == "D"):
            dirtyC += 1  ##count for ML
            fileB.write("suck\n\n")
            point += 1
            RoomC = "C"
            count += 1
            fileB.write(str(point)+"\n\n")
            fileB.write(f"Step : {count+1} \n\n")
            Probility = random.random()
            fileB.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
            while (pC > Probility):
                RoomC = "D"  ## room dirty again
                countC += 1  ## room need clean again
                dirtyC += 1  ## room is dirty
                fileB.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
                fileB.write("suck\n\n")
                point += 1
                RoomC = "C"  ##clean again
                count += 1
                fileB.write(str(point)+"\n\n")
                fileB.write(f"Step : {count+1} \n\n")
                Probility = random.random()
        if (pA > Probility and RoomA == "C"):
                RoomA = "D"
        if (pB > Probility and RoomB == "C"):
                RoomB = "D"


    return robotStanding, RoomA, RoomB, RoomC, point, count,countA,countC,dirtyA,dirtyC


def movement(robotStanding, RoomA, RoomB, RoomC, point,count, comingFrom,countA,countC,dirtyA,dirtyC):


    if (robotStanding == "B" and count<=150):
        if (comingFrom == ""):
            fileB.write("right\n\n")
            point -= 0.5
            robotStanding = "C"
            countC+=1
            count+=1
            fileB.write(str(point)+"\n\n")
            fileB.write(f"Step : {count+1} \n\n")
            comingFrom = "B"
            if (pA > Probility and RoomA == "C"):
                RoomA = "D"
            if (pB > Probility and RoomB == "C"):
                RoomB = "D"
            if (pC > Probility and RoomC == "C"):
                RoomC = "D"
            fileB.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
        if(comingFrom == "A"):
            fileB.write("right\n\n")
            point -= 0.5
            robotStanding = "C"
            countC += 1
            count+=1
            fileB.write(str(point) + "\n\n")
            fileB.write(f"Step : {count+1} \n\n")
            comingFrom = "B"
            if (pA > Probility and RoomA == "C"):
                RoomA = "D"
            if (pB > Probility and RoomB == "C"):
                RoomB = "D"
            if (pC > Probility and RoomC == "C"):
                RoomC = "D"
            fileB.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
        if (comingFrom == "C"):
            fileB.write("left\n\n")
            point -= 0.5
            robotStanding = "A"
            countA += 1
            count += 1
            fileB.write(str(point)+"\n\n")
            fileB.write(f"Step : {count+1} \n\n")
            comingFrom = "B"
            if (pA > Probility and RoomA == "C"):
                RoomA = "D"
            if (pB > Probility and RoomB == "C"):
                RoomB = "D"
            if (pC > Probility and RoomC == "C"):
                RoomC = "D"
            fileB.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
        return robotStanding, RoomA, RoomB, RoomC, point,count, comingFrom,countA,countC,dirtyA,dirtyC

    elif(robotStanding == "B" and count>150):
         if(countA-dirtyA > countC-dirtyC):
             fileB.write("right\n\n")
             point -= 0.5
             robotStanding = "C"
             countC += 1
             count += 1
             fileB.write(str(point) + "\n\n")
             fileB.write(f"Step : {count+1} \n\n")
             comingFrom = "B"
             if (pA > Probility and RoomA == "C"):
                 RoomA = "D"
             if (pB > Probility and RoomB == "C"):
                 RoomB = "D"
             if (pC > Probility and RoomC == "C"):
                RoomC = "D"
             fileB.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
         else:
             fileB.write("left\n\n")
             point -= 0.5
             robotStanding = "A"
             countA += 1
             count += 1
             fileB.write(str(point) + "\n\n")
             fileB.write(f"Step : {count+1} \n\n")
             comingFrom = "B"
             if (pA > Probility and RoomA == "C"):
                 RoomA = "D"
             if (pB > Probility and RoomB == "C"):
                 RoomB = "D"
             if (pC > Probility and RoomC == "C"):
                 RoomC = "D"
             fileB.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')

         return robotStanding, RoomA, RoomB, RoomC, point,count, comingFrom, countA, countC, dirtyA, dirtyC


    if (robotStanding == "A"):
        if (comingFrom == "B"):
            fileB.write("right\n\n")
            point -= 0.5
            robotStanding = "B"
            count += 1
            fileB.write(str(point) + "\n\n")
            fileB.write(f"Step : {count + 1} \n\n")
            comingFrom = "A"
            fileB.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
        return robotStanding, RoomA, RoomB, RoomC, point,count, comingFrom,countA,countC,dirtyA,dirtyC
    if (robotStanding == "C"):
        if (comingFrom == "B"):
            fileB.write("left\n\n")
            point -= 0.5
            robotStanding = "B"
            count += 1
            fileB.write(str(point) + "\n\n")
            fileB.write(f"Step : {count+1} \n\n")
            comingFrom = "C"
            fileB.write(robotStanding + "," + RoomA + "," + RoomB + "," + RoomC + '\n\n')
        return robotStanding, RoomA, RoomB, RoomC, point,count, comingFrom,countA,countC,dirtyA,dirtyC



while (count < 999):
    robotStanding, RoomA, RoomB, RoomC, point, count, countA, countC, dirtyA, dirtyC = cleaning(robotStanding, RoomA, RoomB, RoomC, point, count,countA,countC,dirtyA,dirtyC)
    robotStanding, RoomA, RoomB, RoomC, point, count, comingFrom,countA,countC,dirtyA,dirtyC = movement(robotStanding, RoomA, RoomB, RoomC, point,count,comingFrom,countA,countC,dirtyA,dirtyC)



fileB.write(str(point))
