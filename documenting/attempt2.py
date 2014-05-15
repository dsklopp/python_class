# AUTHOR:      Dan Klopp (dsklopp@gmail.com)
# DESCRIPTION: Demonstrate ineffective documentation
#              Think about "how" your code will be used
#              and write the code so that it is obvious
#              ie, this is better

import os

def generate_dict_of_conf_file(afile):
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

def print_dictionary(results):
  for key in results:
    print(key + " set to " + results[key])

def find_and_print_conf_file_settings(cwd=os.getcwd(),recursive=False):
  for afile in os.listdir(cwd):
    afile_abs=cwd+'/'+afile
    if os.path.isfile(afile_abs):
      if afile == 'attempt1.py' or afile == 'attempt1.pyc':
        continue
      print("Key-Value of file: " + afile_abs)
      print_dictionary(generate_dict_of_conf_file(afile_abs))
      print("")
    elif recursive and os.path.isdir(afile_abs):
      find_and_print_conf_file_settings(cwd=afile_abs, recursive=recursive)


find_and_print_conf_file_settings(recursive=True)
