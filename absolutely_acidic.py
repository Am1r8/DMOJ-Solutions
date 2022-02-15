N = int(input())
sensors = [] #value of sensor
readings = [] #frequency
highs = []
highs2 = []

for i in range(N):
  r = input()
  if r not in sensors:
    sensors.append(r)
    readings.append(1)
  elif r in sensors:
    readings[sensors.index(r)] += 1
    
for i in range(len(sensors)):
  if readings[i] == max(readings):
    highs.append(int(sensors[i]))

if len(highs) > 1:
  highs.sort()
  print (highs[len(highs)-1]-highs[0])
else:
  sensors.remove(sensors[readings.index(max(readings))])
  readings.remove(max(readings))
  for i in range(len(sensors)):
    if readings[i] == max(readings):
      highs2.append(int(sensors[i]))
  highs2.sort()
  if abs(highs2[0]-highs[0]) > abs(highs2[len(highs2)-1]-highs[0]):
    print (abs(highs2[0]-highs[0]))
  else:
    print (abs(highs2[len(highs2)-1]-highs[0]))