#Made By HarveyGW
import time
from time import sleep
def InsertionSort(Arrlist):
  for index in range(1, len(Arrlist)):
    value = Arrlist[index]
    i = index - 1
    while i >= 0:
      if value < Arrlist[i]:
        Arrlist[i + 1] = Arrlist[i] #Shift number in slot i right to slot i+1
        Arrlist [i] = value #Shift value left into slot i
        i -= 1
        print(Arrlist)
        time.sleep(0.1)
      else:
        break

Arrlist = input("Enter the numbers: ").split()
InsertionSort(Arrlist)

 
