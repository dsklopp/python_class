import os
files=os.listdir(".")
for afile in files:
   if afile.startswith("file."):
      print(afile)
