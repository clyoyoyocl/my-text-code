# _*_ conding: utf8 _*_


import random

total = 1000000
doors = [1, 2, 3]
wins = 0

for x in range(total):
    binggo = random.choice(doors)
    hoost = random.choice(doors)
    if hoost == binggo:
        wins += 1
print "wins gailv for stay: %.5f%%" % (wins/float(total)*100)

wins_2 = 0

for x in range(total):
    binggo = random.choice(doors)
    hoost = random.choice(doors)
    doors_2 = doors[:]
    doors_2.remove(hoost)
    swicth = random.choice(doors_2) 
    if swicth == binggo:
        wins_2 += 1
print "wins gailv for swicth: %.5f%%" % (wins_2/float(total)*100)

stay_gailv = wins/float(total)
swicth_gailv = wins_2/float(total)

if stay_gailv > swicth_gailv:
    print "stay > swicth"
else:
    print "swicth > stay"
