
# coding: utf-8

# In[77]:


#Estimating ARIMA


# In[91]:


#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf 
from statsmodels.tsa.seasonal import seasonal_decompose                       
from sklearn.metrics import mean_squared_error
from math import sqrt
import warnings
warnings.filterwarnings("ignore")  


# In[80]:


#importing data
data = pd.read_csv(r"C:\Users\PC\Desktop\inflation_data.csv")
data["month"] = pd.to_datetime(data["month"])
data = data.set_index(["month"], drop = True)
data.head()


# In[81]:


#creating train and test data
split_date = pd.Timestamp('2012-09-30')
train = data.loc[:split_date]
test = data.loc[split_date:]
test.head()


# In[82]:


#seasonal decompositon
seas = seasonal_decompose(data["inflation"], model = "add")
seas.plot()


# In[83]:


#Estimating Arima model with optimal parameters of (4, 0, 1)
arima = SARIMAX(train["inflation"], order = (4, 0, 1), seasonal_order = (1,0,1,12))
arima_result = arima.fit()
arima_result.summary()


# In[104]:


arima_prediction = arima_result.predict(start = len(train)-1, end = len(data)-1, type = "levels").rename("ARIMA Forecast")
arima_prediction2 = arima_result.predict(start = 0, end = len(train)-1, type = "levels").rename("ARIMA Forecast")


# In[105]:


arima_prediction2[-10:]


# In[95]:


test["inflation"].plot(figsize = (16,5), legend = True)
arima_prediction.plot(legend = True);


# In[90]:


test["ARIMA_Forecast"] = arima_prediction
test.tail()


# In[108]:


rmse = sqrt(mean_squared_error(test.inflation, test.ARIMA_Forecast))
print(rmse)


# In[110]:


rmse2 = sqrt(mean_squared_error(train.inflation, arima_prediction2))
print(rmse2)

