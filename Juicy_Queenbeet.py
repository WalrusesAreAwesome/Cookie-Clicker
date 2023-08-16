# reproduce between [80, 100)
import random
plot = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
JB = [-1,-1,-1,-1]
lumps = 0

def tick(): 
  global plot
  global JB
  global lumps
  for ring in range(4):
    fertile = True
    for beet in range(8):
      if (JB[ring] == -1):
        rand = random.random()
        if (rand<0.8):
          plot[ring][beet] += 1
        else:
          plot[ring][beet] += 2
      if plot[ring][beet]>=100:
        for beetDeath in range(8):
          plot[ring][beetDeath] = 0
        break
      elif (plot[ring][beet] >= 80):
        fertile = False

    if (fertile):
      for beetDeath in range(8):
        plot[ring][beetDeath] = 0
      rand = random.random()
      if (rand<(0.001*3) and JB[ring] == -1):
        JB[ring] = 0

    if (JB[ring] != -1):
      rand = random.random()
      if (rand<0.08):
        JB[ring] += 1
      if JB[ring] >= 85:
        lumps+=1
        JB[ring] = -1

time = 10**9
for t in range(time):
  if t%(time/1000) == 0:
    print(str(t/(time/100))+"%")
  tick()
print(str(lumps) + " lumps out of " + str(time) + " ticks")
print(str(lumps/(time*300)) + " lumps per second")
print(str(lumps/(time*5)) + " lumps per minute")
print(str(lumps/(time/12)) + " lumps per hour")
print(str(lumps/(time/288)) + " lumps per day")
print(str(lumps/(time/105120)) + " lumps per year")
