#-----------------------------------------------------------------------------
# Name:        Resistor Calculator (main.py)
# Purpose:     Calculates the resistance of multiple 4-band resistors
#
# Author:      Sophie Wong
# Created:     27-Mar-2023
# Updated:     5-Apr-2023
#-----------------------------------------------------------------------------

# function that calculates the resistance of 4-band resistors
def resistorCalc(firstBand,secondBand,thirdBand,lastBand):
  # resistor values dictionary
  resistorValues = {'black':0,'brown':1,'red':2,'orange':3,'yellow':4,'green':5,'blue':6,'violet':7,'grey':8,'white':9,'gold':0.1,'silver':0.01}

  # adding the first two bands' digits together (first band is tens digit, second band is ones digit)
  firstTwoBands = resistorValues[firstBand]*10 + resistorValues[secondBand]
   
  # determining the third band (multiplier) to multiply the current resistance value
  if thirdBand == 'black':
    resistorValues['black'] = 0
    thirdBand == resistorValues['black']
  elif thirdBand == 'brown':
    resistorValues['brown'] += 9
    thirdBand == resistorValues['brown']
  elif thirdBand == 'red':
    resistorValues['red'] += 98
    thirdBand == resistorValues['red']
  elif thirdBand == 'orange':
    resistorValues['orange'] += 997
    thirdBand == resistorValues['orange']
  elif thirdBand == 'yellow':
    resistorValues['yellow'] += 9996
    thirdBand == resistorValues['yellow']
  elif thirdBand == 'green':
    resistorValues['green'] += 99995
    thirdBand == resistorValues['green']
  elif thirdBand == 'blue':
    resistorValues['blue'] += 999994
    thirdBand == resistorValues['blue']
  elif thirdBand == 'violet':
    resistorValues['violet'] += 9999993
    thirdBand == resistorValues['violet']
  elif thirdBand == 'grey':
    resistorValues['grey'] += 99999992
    thirdBand == resistorValues['grey']
  elif thirdBand == 'white':
    resistorValues['white'] += 999999991
    thirdBand == resistorValues['white']
  
  multipliedValue = firstTwoBands*resistorValues[thirdBand]
  
  # determining the colour of the last band to determine the tolerance of the resistor
  if lastBand == 'brown':
    resistorValues['brown'] = 0.01
    lastBand == resistorValues['brown']
  elif lastBand == 'red':
    resistorValues['red'] = 0.02
    lastBand == resistorValues['red']
  elif lastBand == 'gold':
    resistorValues['gold'] = 0.05
    lastBand == resistorValues['gold']
  elif lastBand == 'silver':
    resistorValues['silver'] = 0.1
    lastBand == resistorValues['silver']
    
  # creating range for tolerance
  resistanceRange = int(multipliedValue*resistorValues[lastBand])
  resistanceRangeUp = int(multipliedValue + resistanceRange)
  resistanceRangeDown = int(multipliedValue - resistanceRange)

  # creating list of tolerances to print
  toleranceRange = []
  for tolerance in range(resistanceRangeDown,resistanceRangeUp+1):
    toleranceRange.append(tolerance)
    if tolerance < 0:
      toleranceRange.remove(tolerance)
  for tolerance in range(0,len(toleranceRange)):
    if len(toleranceRange) > 30:
      del toleranceRange [-1]
  toleranceRange = ", ".join(map(str,toleranceRange))  
  return "Resistor #" + str(resistor + 1) + "'s resistance can be any of the following values - " + str(toleranceRange) + " Ohms, just to name some whole values."
  
 

# outside of function
# user inputs number of resistors they want to calculate the resistance of
numOfResistors = int(input("How many resistors do you want to calculate the resistance of?: "))

# list of colours for user to refer to
print("The possible colours you can input are: black, brown, red, orange, yellow, green, blue, violet, grey, white, gold, silver.")

# user inputs colours of bands for each resistor
print()
for resistor in range(numOfResistors):
  print("Resistor #" + str(resistor+1) + ":")
  
  # first band
  firstBand = str(input("What is the colour of the first band?: "))
  firstBand = firstBand.casefold()
  while firstBand not in ['black','brown','red','orange','yellow','green','blue','violet','grey','white']:
    firstBand = str(input("That is not possible, what is the colour of the first band?: "))
    firstBand = firstBand.casefold()
  
    # second band
  secondBand = str(input("What is the colour of the second band?: "))
  secondBand = secondBand.casefold()
  while secondBand not in ['black','brown','red','orange','yellow','green','blue','violet','grey','white']:
    secondBand = str(input("That is not possible, what is the colour of the second band?: "))
    secondBand = secondBand.casefold()
  
    # third band
  thirdBand = str(input("What is the colour of the third band?: "))
  thirdBand = thirdBand.casefold()
  while thirdBand not in ['black','brown','red','orange','yellow','green','blue','violet','grey','white','gold','silver']:
    thirdBand = str(input("That is not possible, what is the colour of the third band?: "))
    thirdBand = thirdBand.casefold()
  
  # last band
  lastBand = str(input("What is the colour of the last band?: "))
  lastBand = lastBand.casefold()
  while lastBand not in ['brown','red','gold','silver']:
    lastBand = str(input("That is not possible, what is the colour of the last band?: "))
    lastBand = lastBand.casefold()
  
  print()
  # calling the function to calculate resistance with the values that have been given
  print(resistorCalc(firstBand,secondBand,thirdBand,lastBand))
  print()

 # calculating resistance if the colour of the first band was another colour
  if firstBand != 'blue':
    firstBand = 'blue'
    print("If the first band was blue, " + resistorCalc(firstBand,secondBand,thirdBand,lastBand))
  else:
    firstBand = 'orange'
    print("If the first band was orange, " + resistorCalc(firstBand,secondBand,thirdBand,lastBand))
  print()
  print()