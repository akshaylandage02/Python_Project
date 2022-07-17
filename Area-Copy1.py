#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
def circle_area():
    r=int(input("Enter radius"))
    print(r*r*3.14)
def rectangl_area():
    l=int(input("Enter Length"))
    b=int(input("Enter Breadth"))
    print(l*b)
def square_area():
    s=int(input("Enter Side of square"))
    print(s*s)
    
print("*******************Menu****************")
print("1.circle \n"
      "2.Rectangle\n"
      "3.Square\n")
choice=int(input("Enter your Choice"))
if choice == 1:
       circle_area()
elif choice == 2:
       rectangl_area()
elif choice == 3:
        square_area()



# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




