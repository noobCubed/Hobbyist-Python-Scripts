
# coding: utf-8

# In[121]:


import os
import re


# In[122]:


#insert the required directory here
os.chdir('F:\TestDrive')


# In[137]:


lis = os.listdir()


# In[138]:


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

