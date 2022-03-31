# The Python program 'Collatz_Conjecture_Batch_Altitude_Generator.py' generates the altitudes of the trajectories of several flight numbers.
# This program also comes with an additional file called 'trajectoryData.csv' to which the program writes data to.

# This software can be run for free on Replit.com

# importing library to write to CSV file
import csv

# open the file in the write mode
csvFile = open('trajectoryData.csv', 'w')
writer = csv.writer(csvFile)

# decleration of initial values

flightNumber = 1

# inputing the range of values for which trajectories are calculated
range = int(input("Enter the total of flightnumbers > "))

# while loop to iterate the trajectory of each flight number

while flightNumber < (range+1):

  # altitudes array to store all of the altitudes for a flightnumber
  altitudes = []
  altitude = flightNumber
  flag = True

    # while loop to iterate through the individual altitudes of a flight number
  
  while flag:

    altitudes.append(int(altitude))

    # conditional statement to check if the altitude is 1, in which case the trajectory is finished
    
    if altitude == 1:
      
      flag = False
      
    else:

      # conditional statement for the 3x+1 algorithm

      if altitude % 2 == 0:
      # checks if altitude is even and halves it as per rules of the conjecture
        
        altitude = altitude/2
        
      else:
        # if the altitude is not even, then it is odd and the altitude is multiplied by 3 and 1 is added to it
        
        altitude = (altitude*3)+1

  # writes data to CSV file
  
  writer.writerow(altitudes)
  flightNumber = flightNumber + 1

# closes CSV file
csvFile.close()
