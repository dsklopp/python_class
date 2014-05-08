# AUTHOR: Daniel Klopp
# DESCRIPTION: Reimplementation of six.pl in Python and without obfuscation


def bottles_of_beer_on_the_wall(count):
   for bottle in reversed(range(1,count)):
      if bottle > 2: 
         print(str(bottle) + " bottles of beer on the wall, " + str(bottle) + " bottles of beer!")
         print("Take one down, pass it around")
         print(str(bottle-1) + " bottles of beer on the wall!")
      elif bottle == 2:
         print(str(bottle) + " bottles of beer on the wall, " + str(bottle) + " bottles of beer!")
         print("Take one down, pass it around")
         print(str(bottle-1) + " bottle of beer on the wall!")
      else:
         print(str(bottle) + " bottle of beer on the wall, " + str(bottle) + " bottle of beer!")
         print("Take one down, pass it around")
         print("No bottles of beer on the wall!")
      print("")

bottles_of_beer_on_the_wall(100)
