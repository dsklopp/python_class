import os
files=os.listdir(".")
for afile in files:
   if afile.startswith("file."):
      # right way
      print(afile[0:5] + " - " + afile[5:])

