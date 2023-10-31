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

fileA.write('B,D,D,D')

fileA.close()

while (count < 1000):
    count = count + 1
