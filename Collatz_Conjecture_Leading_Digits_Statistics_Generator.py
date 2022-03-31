#

# decleration of initial variables

flightNumber = 1
totalAltitudes = 0
firstDigitCountArray = [0,0,0,0,0,0,0,0,0]

# inputing the range of values for which the occurence of leading digits is calculated

range = int(input("Enter the total of flightnumbers > ")) # for large values the program takes a while to output results

# while loop to iterate the trajectory of each flight number

while flightNumber < (range+1):
  
  altitude = flightNumber
  flag = True

  # while loop to iterate through the individual altitudes of a flight number
  
  while flag:

    # incrementing the total altitudes so a percentage can be calculated of the occurence of leading digits
    totalAltitudes = totalAltitudes + 1
    count = 1

    # while loop to increment the total number of the leading digit in the firstDigitCountArray
    
    while count < 10:
      
      if str(altitude)[0] == str(count):
        
        firstDigitCountArray[count-1] = firstDigitCountArray[count-1] + 1
      count = count + 1

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

  # incrementing the next flight number so that other trajectories can be calculated
  flightNumber = flightNumber + 1

# outputing the total occurence of leading digits

firstDigit = 1
print("\n")
while firstDigit < 10:
  print("The total occurence of",firstDigit,"is",firstDigitCountArray[firstDigit-1])
  firstDigit = firstDigit + 1

# outputing the percentage occurence of the leading digits

print("\n")
firstDigit = 1
for i in firstDigitCountArray:
  percentage = (i/totalAltitudes)*100
  print("The percentage of numbers beginning with",firstDigit, "is",percentage)
  firstDigit = firstDigit + 1

