import os
files=os.listdir(".")
for afile in files:
   if afile.startswith("file."):
      file_no=afile[5:]
      if len(file_no) == 1:
         digit="00"+ file_no # 001
      elif len(file_no)== 2:
         digit="0" + file_no # 010
      elif len(file_no) == 3:
         digit=file_no # 100
      newfile=afile[:5]+digit
      os.rename(afile,newfile) 

