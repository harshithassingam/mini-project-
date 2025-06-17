#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Importing necessary libraries


# In[2]:


claims= pd.read_csv("C:/Users/Singam Srinivasa Rao/Downloads/insurancedataclaims.csv")
claims

# Assigning the CSV dataset to a variable 


# In[6]:


print(claims.columns)

# Viewing the names of the columns


# In[17]:


claims['submision_date'] = pd.to_datetime(claims['submision_date'])
claims

# Converting the submission_date into a datetime datatype and putting it under submission_date column in the claims table.


# In[18]:


claims['decision_date'] = pd.to_datetime(claims['decision_date'])
claims

# Converting the decision_date into a datetime datatype and putting it under decision_date column in the claims table.


# In[107]:


claims.describe()


# In[79]:


claims['processing_dates'] = (claims['decision_date'] - claims['submision_date'])
claims['processing_dates']

# Calculating the duration between the claim submission date and decision date and assigning it to the processing_dates column


# In[121]:


# total_claims gives the total number of all kinds of claims. Using Groupby, we group the individual values and give the individual value count using value_counts

total_claims = claims['claim_status'].value_counts()

# approved_claim_status gives the total number of approved claims. Approved claims are stored as 0 and we are filtering only the approved claims and adding them using sum() function

approved_claim_status = (claims['claim_status'] == 0).sum()

# rejected_claim_status gives the total number of rejected claims. Rejected claims are being filtered and added using the sum() function. 

rejected_claim_status = (claims['claim_status'] == 1).sum()

# fraudulent_claims gives the total number of fraudulent claim.

fraudulent_claims = (claims['fraud_flag'] == 'Fraud').sum()

# avg_processing_time is the average amount of time it takes to process the claims. mean() function gives us the average of the processing time.

avg_processing_time = claims['processing_dates'].mean()


print("Total claims: " , total_claims)
print("Approved_ claim_status: " , approved_claim_status)
print("Rejected CLaim Status : " , rejected_claim_status)
print("Fraudulent claims: " , fraudulent_claims)
print("Average Processing Time: " , avg_processing_time)


# In[22]:


plt.figure(figsize=(10,5))  # gives the size of the pie chart 
plt.title("approved vs rejected")  # gives the title for the pie chart

plt.pie(claims["claim_status"].value_counts(), labels=["approved","rejected"]) 

# plt.pie() is a matplotlib function, used to create a pie chart. Using value_counts, we are counting each unique value in that column and we give the lables as approved or rejected using labels.


# In[112]:


# Using value_counts, we are counting the number of times each unique value appears. reset_index() converts it into a DataFrame and moves the index (status value) into a column. 

    
claim_counts = claims['claim_status'].value_counts().reset_index()

#Renaming thc column 

claim_counts.columns = ['claim_status', 'count']


plt.figure(figsize=(10,9)) # givesthe size of the bar graph

# we are creating a barplot using a seaborn function called as bar plot and we are giving the values for x axis and y axis
sns.barplot(data=claim_counts, x='claim_status', y='count', palette=['skyblue', 'orange'])

plt.title("Number of Claims by Status")
plt.xlabel("Claim Status")
plt.ylabel("Count")
plt.show()


# In[ ]:




