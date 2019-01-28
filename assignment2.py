#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n=int(input('enter number  :'))
if n%2!=0:
    print('weird')
elif n % 2==0 and n>=2:
    print('not weird')
    if n>=6 and n<=20:
        print('weird')
if n>=20:
    print('weird')
    


# In[33]:


a=int(input('enter number x:'))
b=int(input('enter number y:'))
x=10
y=25
if x>3 and y>13 :
      print('both conditions are correct')
if x<=3 or y<=13:
      print('atleast one of the condition is false')
      
      


# In[37]:


list = ['23', 'name', 'age', 'veridic', 'python', 'data']

for i in list:
    print(i)


# In[4]:


n = int(input('Enter number of elements: '))
l = []
for i in range(n):
    item = input('Enter element: ')
    l.append(item)

print(l)
item_to_search = input('Enter element to delete: ')
l.remove(item_to_search)
print(l)
         
         


# In[5]:


for i in range(20):
    print('14 x ' + str(i+1) + ' = ' +str(14*(i+1)))


# In[10]:


list = [2, 4, 5, 6, 7, 8, 19, 34, 45, 56, 12, 65, 88, 92, 100]
a= []

for i in list:
    a.append(i ** 2)

print(a)


# In[11]:



tup = (1, 3, 5, 6, 94, 100, 7)

for i in tup:
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                break
        else:    
            print(i)


# In[18]:


a= input('Enter a input: ')
b = input('Enter b input: ')
if a == b:
    print("It's a tie!")
elif a == 'rock':
    if b == 'scissors':
        print("Rock wins!")
    else:
        print("Paper wins!")
elif a == 'scissors':
    if b == 'paper':
        print("Scissors win!")
    else:
        print("Rock wins!")
elif a == 'paper':
    if b == 'rock':
        print("Paper wins!")
    else:
        print("Scissors win!")
else:
    print("Invalid input! You have not entered rock, paper or scissors, try again.")


# In[ ]:




