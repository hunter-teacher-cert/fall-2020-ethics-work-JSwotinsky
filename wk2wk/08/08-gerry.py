#Sangmin Pak and Jonathan Swotinsky
#Ethics and Computer Science

#State Name: Pythonia

import random

#Print the current state of the "state":
def printState():
  print("STATE:\n")
  for i in range(6):
    for k in range(3):
      print(state[i][k], end="")
    print("")
  print("\n")

#Print the current state of the "districts":
def printDistricts():
  print("DISTRICTS:\n")
  for i in range(6):
    print("District ", i, ": ", sep = "", end="")
    print(districts[i])
  print("\n")

#Print the "winnders" in each "district":
def printWinners():
  print("WINNERS:\n")
  
  #for each of the six districts, declare a winner:
  for i in range(6):
    #If the sum of the votes in district i is greater than or equal to 2 (e.g. if 1 wins district i), declare 1 as the winner of district i:
    if(state[districts[i][0][0]][districts[i][0][1]]+state[districts[i][1][0]][districts[i][1][1]]+state[districts[i][2][0]][districts[i][2][1]]>=2):
      print("District", i, "Winner: 1")
    #If the sum of the votes in district i is less than 2 (e.g. if 0 wins district i), declare 0 as the winner of district i:
    else:
      print("District", i, "Winner: 0")

#Generate a "state" composed of 6 rows and 3 columns, and set the "voting preference" of each cell to 0:
state = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

#Randomly assign a "voting preference" of 0 or 1 to each cell in the state:
for i in range(6):
  for k in range(3):
    state[i][k]=random.randint(0,1)

#Generate a list of "districts" each of which is represented by a row in the "state":
districts = []
districts.append([[0,0],[0,1],[0,2]]) 
districts.append([[1,0],[1,1],[1,2]]) 
districts.append([[2,0],[2,1],[2,2]]) 
districts.append([[3,0],[3,1],[3,2]]) 
districts.append([[4,0],[4,1],[4,2]]) 
districts.append([[5,0],[5,1],[5,2]]) 

printState()
printDistricts()
printWinners()
