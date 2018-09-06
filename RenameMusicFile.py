
#Created with the assistance of Madhusudhan Sridhar
#https://github.com/noobCubed

import os
import re
import argparse

parser = argparse.ArgumentParser(description='Rename Music File')
parser.add_argument('-directory', help=('Given the directory where the music files are present, the program will rename all of them accordingly'))

args = parser.parse_args()

#insert the required directory here
os.chdir(args.directory)

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

