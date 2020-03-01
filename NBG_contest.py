
# coding: utf-8

# In[1]:


#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os


# In[2]:


#importing data
data = pd.read_csv(r"C:\Users\PC\Desktop\inflation_data.csv")
data["month"] = pd.to_datetime(data["month"])
data = data.set_index(["month"], drop = True)
data.head()


# In[3]:


#creating train and test data
split_date = pd.Timestamp('2012-09-30')
train = data.loc[:split_date]
test = data.loc[split_date:]
train.tail()


# In[4]:


#ploting train and test sets
plt.figure(figsize = (10,6))
ax = train.plot()
test.plot(ax = ax)
plt.legend(['train', 'test']);


# In[6]:


from sklearn.metrics import mean_squared_error
from math import sqrt


# In[7]:


i = 3
rolling_mean = train.inflation.rolling(window=i).mean()
train['moving_average_prediction'] = rolling_mean
final = train.copy()
final_train = final[i:]
final_train.head()
rmse = sqrt(mean_squared_error(final_train.inflation, final_train.moving_average_prediction))
print(rmse)


# In[8]:


plt.figure(figsize=(16,8))
plt.plot(final_train['inflation'], label='Train')
plt.plot(final_train['moving_average_prediction'], label='Moving Average prediction')
plt.legend(loc='best')
plt.show()


# In[9]:


#predict for the test set
rolling_mean = data.inflation.rolling(window=3).mean()
test['moving_average_prediction'] = rolling_mean[split_date:]
test.head()


# In[10]:


#ploting results
plt.figure(figsize=(16,8))
plt.plot(final_train['inflation'], label='Train')
plt.plot(test['inflation'], label='Test')
plt.plot(test['moving_average_prediction'], label='Moving Average prediction')
plt.legend(loc='best')
plt.show()


# In[11]:


final_test = test[3:]
rmse = sqrt(mean_squared_error(final_test.inflation, final_test.moving_average_prediction))
print(rmse)

