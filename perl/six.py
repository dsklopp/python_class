# AUTHOR: Daniel Klopp
# DESCRIPTION: Reimplementation of six.pl in Python and without obfuscation


def bottles_of_beer_on_the_wall(count):
   for bottle in reversed(range(1,count)):
      if bottle > 1: 
         print(str(bottle) + " bottles of beer on the wall, " + str(bottle) + " bottles of beer!")
      else:
         print(str(bottle) + " bottle of beer on the wall, " + str(bottle) + " bottle of beer!")
      print("Take one down, pass it around")

      newbottle=bottle-1
      if newbottle > 1:
         print(str(newbottle) + " bottles of beer on the wall!")
      elif newbottle == 1:
         print(str(newbottle) + " bottle of beer on the wall!")
      else:
         print("No bottles of beer on the wall!")
      print("")

bottles_of_beer_on_the_wall(100)
