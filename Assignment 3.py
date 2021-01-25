#!/usr/bin/env python
# coding: utf-8

# # Question 1

# In[1]:


# Write a python program to merge two files into a third file 


# In[ ]:


import shutil 

from pathlib import Path 

   

firstfile = Path(r'C:\Users\Sohom\Desktop\GFG.txt') 

secondfile = Path(r'C:\Users\Sohom\Desktop\CSE.txt') 

  

newfile = input("Enter the name of the new file: ") 

print() 

print("The merged content of the 2 files will be in", newfile) 

  

with open(newfile, "wb") as wfd: 

  

    for f in [firstfile, secondfile]: 

        with open(f, "rb") as fd: 

            shutil.copyfileobj(fd, wfd, 1024 * 1024 * 10) 

  

print("\nThe content is merged successfully.!") 

print("Do you want to view it ? (y / n): ") 

  

check = input() 

if check == 'n': 

    exit() 

else: 

    print() 

    c = open(newfile, "r") 

    print(c.read()) 

    c.close()


# # Question 2

#  Take two lists as input list1 = [1,2,3,4,5] and list2 = ["a","b","c","d","e"] From that make a dictionary
#  output {1:"a",2:"b",3:"c",4:"d",5:"e"}

# In[3]:


a=[1,2,3,4,5]
b=["a","b","c","d","e"]
c={}
for i in range (len(a)):
    c[a[i]]=b[i]
print(c)


# In[ ]:




