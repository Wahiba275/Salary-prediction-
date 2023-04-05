#!/usr/bin/env python
# coding: utf-8

# # Importing the libraries

# In[1]:


import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 


# # Reading the dataset

# In[2]:


data=pd.read_csv("Salary_Data.csv")


# In[3]:


data


# In[4]:


data.info()


# In[9]:


X = data.iloc[:,:-1].values
y=data.iloc[:,-1].values


# In[15]:


plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Salary in function of Years of Experience')
plt.scatter(X , y , color='red' , marker='*')


# In[11]:


print(X)


# In[12]:


print(y)


# # Splitting the dataset into the training set and the test set

# In[13]:


from sklearn.model_selection import train_test_split 
X_train , X_test , y_train , y_test = train_test_split(X , y , test_size=0.2 , random_state=0)


# # Training the simple linear regression model on the training set 

# In[16]:


from sklearn.linear_model import LinearRegression 
regressor = LinearRegression()
regressor.fit(X_train , y_train)


# # Predicting the test set results

# In[18]:


y_pred=regressor.predict(X_test)


# In[22]:


print(X_test)


# In[21]:


print(y_pred)


# In[23]:


print(y_test)


# # Visualising the training set results

# In[28]:


plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Salary vs Years of Experience (Training set)')
plt.scatter(X_train , y_train , color='red' , marker='*')
plt.plot(X_train , regressor.predict(X_train) , color='blue')
plt.show()


# # Visualising the Test set results

# In[30]:


plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Salary vs Years of Experience (Test set )')
plt.scatter(X_test , y_test, color='red' , marker='*')
plt.plot(X_test , y_pred , color='blue')
plt.show()


# In[ ]:




