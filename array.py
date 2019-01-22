#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
np.zeros([2,2])


# In[17]:


import numpy as np
np.ones([2,2],float)


# In[3]:


np.array([[ 1, 2, 3], [ 4, 5, 6], [ 0, 8, 9], [ 0, 0, 12]])


# In[9]:


x=np.array([[1,2,3], [4,5,6]], np.int32)
print('x is {}'.format(x))
y=np.empty_like(x)
print('y is {}'.format(y))


# In[18]:


np.identity(3)


# In[21]:


np.ones([3,2], float)


# In[3]:


import numpy as np
x = np.arange(4, dtype =np.int64)
print(x)
y=np.ones_like(x)
print('y is {}'.format(y))


# In[32]:


np.zeros((3,2),float)


# In[2]:


import numpy as np
x=np.full((2,5),6)
print(x)


# In[5]:



x = np.arange(4, dtype =np.int64)
print(x)
y=np.zeros_like(x)
print('y is {}'.format(y))


# In[9]:


x = np.arange(4, dtype =np.int64)
print('x is {}'.format(x))
y=np.full_like(x,6)
print(y)


# In[20]:


np.array([1,2,3])


# In[22]:


x=[1,2]
np.asarray(x)


# In[24]:


x= np.array([[1, 2], [3, 4]])
y=np.asmatrix(x)
y


# In[25]:


x=[1,2]
np.asfarray(x)


# In[27]:


x = np.array([30])
np.asscalar(x)


# In[3]:


import numpy as np
x = np.array([1, 2, 3])
y = x.copy()
print(id(x), x)
print(id(y), y)


# In[29]:


np.arange(2,101,2)


# In[30]:


np.linspace(3,10,50)


# In[31]:


np.logspace(3.,10.,50.)


# In[37]:



x = np.array([[ 0, 1, 2, 3], [ 4, 5, 6, 7], [ 8, 9, 10, 11]])
print(x)
x.diagonal()


# In[39]:


np.diagflat([1,2,3,4])


# In[6]:


np.tri(3,5,-1)


# In[5]:


np.tril(np.arange(1,13).reshape(4,3), -1)


# In[4]:



np.triu(np.arange(1,13).reshape(4,3), -1)


# In[ ]:




