
#Created with the assistance of Madhusudhan Sridhar
#https://github.com/noobCubed

import os
import re

#insert the required directory here
os.chdir('F:\TestDrive')


lis = os.listdir()


for fileName in lis:
    count = 0
    for j in fileName:
        if j.isalpha() == False:
            count += 1
        else:
            break
    newFileName="".join(fileName[count:])

    newFileName=newFileName.replace('-',' ')
    newFileName=newFileName.replace(newFileName[0],newFileName[0].upper(),1)

    os.rename(fileName,newFileName)

