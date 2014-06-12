import os

afile="file.1"
files=os.listdir(".")
for afile in files:
   if afile.startswith("file."):
      # wrong way
      print(afile[0:5] + " - " + afile[-1:])

