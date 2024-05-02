#!/usr/bin/env python
# coding: utf-8

# In[6]:


l=[1,1,2,2,4,5,6,7,7,9]
c=0
for i in range(0,len(l)):
    for j in range (i+1,len(l)):
        if l[i]==l[j]:
            c=c+1
print(c)
          


# In[ ]:




