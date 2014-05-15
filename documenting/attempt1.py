# AUTHOR:      Dan Klopp (dsklopp@gmail.com)
# DESCRIPTION: Demonstrate ineffective documentation
#              Think about "how" your code will be used
#              and write the code so that it is obvious
#              ie, don't do what you see here

import os

def funcA(afile):
  """
  Read a *.conf file, store all key-value pairs of the form
  key=value
  in a dictionary and return that as the result.
  """
  f=open(afile,'r')
  results={}
  for line in ( line.strip() for line in f ):
    if len(line) == 0:
      continue
    elif line[0]=='#':
      continue
    entry=line.split('=')
    if len(entry) != 2:
      continue
    results[entry[0]]=entry[1]
  f.close()
  return results

def funcC(results):
  """
  Given a dictionary, print out each key-value pair found
  """
  for key in results:
    print(key + " set to " + results[key])

def funcB(cwd=os.getcwd(),recursive=False):
  """
  Search a directory structure for *.conf files and print out
  all key-value pairs, of the format:
  key=value
  found in that file.
  recursive=True will descend into the directory structure.  By
  default it searches from PWD.
  """
  for afile in os.listdir(cwd):
    afile_abs=cwd+'/'+afile
    if os.path.isfile(afile_abs):
      if afile == 'attempt1.py' or afile == 'attempt1.pyc':
        continue
      print("Key-Value of file: " + afile_abs)
      funcC(funcA(afile_abs))
      print("")
    elif recursive and os.path.isdir(afile_abs):
      funcB(cwd=afile_abs, recursive=recursive)


funcB(recursive=True)
