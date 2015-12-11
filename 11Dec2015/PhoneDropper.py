import numpy as np
import matplotlib.pyplot as plt
nFloors = 1000

def drop(floor, breakFloor):
  if floor >= breakFloor:
    return True
  else:
    return False

def trials(intervals, breakFloor):
  n = intervals
  trials = int(np.floor(nFloors/n))
  steps = 0
  threshold = 0
  for i in range(1,trials+1):
    steps += 1
    floor = i*n
    isBroken = drop(floor, breakFloor)
    if isBroken:
      floorDecided = False
      for j in range((i-1)*n+1, (i*n)):
        steps += 1
        floor = j
        isBroken = drop(floor, breakFloor)
        if isBroken:
          threshold = j
          floorDecided = True
          break
        else:
          pass
      if not floorDecided:
        threshold = i*n
        break
      break
  if threshold==0:
    leftover = np.mod(nFloors, n)
    for i in range(nFloors - leftover + 1, nFloors+1):
      steps += 1
      floor = i
      isBroken = drop(floor, breakFloor)
      if isBroken:
        threshold = i
        break
  return steps, threshold

def findMax(interval):
  steps = []
  for i in range(1, nFloors):
    step, thresh = trials(interval, i)
    steps.append(step)
  return max(steps)

maxSteps = []
for l in range(1, nFloors):
  step = findMax(l)
  maxSteps.append(step)

plt.scatter(range(1,nFloors), maxSteps)
plt.show()



