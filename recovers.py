import os
import re
import sys
import shutil

total = 0
count = 0
src_dict = ("/home/ashok/Downloads/refined")
pattern = re.compile('soknadsweb',re.I) #keyword
dest_dict = ("/home/ashok/Downloads/refin1/")

for m_files in os.listdir(src_dict):
    files = os.path.join(src_dict,m_files))
    strng = open(files,encoding='latin1')
    total = total + 1
    for lines in strng.readlines():
	if re.search(pattern,lines):
            count += 1
	    dest = os.path.join(dest_dict,m_files)
            shutil.move(files,dest_dict)  #move files
            print(re.split(r'=', lines))
            print(files)
            break


print("Total match = ", count)


print("Total files= ",total)
