# decleration of initial variables

steps = 0
flag = True

# inputing the initial flight number

flightNumber = int(input("Enter the flight number > "))
altitude = flightNumber

# while loop to iterate through all of the altitudes in the trajectory

while flag:

  # conditional statement to check if the altitude is 1, in which case the trajectory is finished
  
  if altitude == 1:
    
    flag = False
    
  else:

    # conditional statement for the 3x+1 algorithm
    
    if altitude % 2 == 0:
    # checks if altitude is evenand halves it as per rules of the conjecture
      
      altitude = altitude/2
      
    else:
    # if the altitude is not even, then it is odd and the altitude is multiplied by 3 and 1 is added to it
      
      altitude = (altitude*3)+1

    # counting the total number of steps in the trajectory
    steps = steps+1

    # outputing data
    print("Step: ",steps," Altitude: ",int(altitude))
      
  