import os
files=os.listdir(".")
for afile in files:
   if afile.startswith("file."):
      file_no=afile[5:]
      if file_no[:2] == '00':
         digit=file_no[-1:] # 001
      elif file_no[:1]== '0':
         digit=file_no[-2:] # 010
      else:
         digit=file_no # 100
      newfile=afile[:5]+digit
      os.rename(afile,newfile) 

