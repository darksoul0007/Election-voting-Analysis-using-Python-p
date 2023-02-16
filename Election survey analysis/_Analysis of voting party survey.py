#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


survey = pd.read_csv(r"D:\downloads\Sayan project\python projects for data analytics\Survey Dataset - Technical Interview.csv")


# In[4]:


survey


# # Q1) How many samples were collected in each day? 

# In[5]:


survey.head(2)


# In[7]:


survey['collection_date'].unique()                              # to show all unique values of column


# In[8]:


survey['collection_date'].nunique()                             # total unique values in column


# In[10]:


survey['collection_date'].value_counts(ascending=True)


# # Q2) what proportion were respondents were age less than 44?

# In[11]:


survey.head(2)


# In[13]:


survey.age.dtype


# In[14]:


survey.age.unique()


# In[15]:


survey.age.value_counts()


# In[22]:


survey['age'].replace({'24ko':24},inplace = True)


# In[23]:


survey.age.unique()


# In[24]:


survey.age.value_counts()


# In[32]:


survey['age'] = survey.age.astype(int)                                          # to change the data tpye of column


# In[33]:


survey.age.dtype


# In[35]:


survey[survey['age']<44]


# In[36]:


6345/6867*100


# # Q3) Create a new column in the data frame "age_group". This column should contain the age group the respondent belong to , The age groups are 18-25,25-40,40-55 and 55+. 

# In[37]:


survey.head(2)


# In[38]:


data = survey.copy()                        # to make a copy of data frame


# In[39]:


data.head()


# In[ ]:


# df_name.insert('new column position', ' new column name ','new column values')    # to insert the new column required
# data. insert(10, ' age_group', survey.age)


# In[40]:


data.insert(10, 'age_group', survey.age)


# In[43]:


data1 =data[(data.age_group>= 18) & (data.age_group <25)]


# In[45]:


data1.age_group.unique()


# In[ ]:


# Assining values to a column


# In[46]:


data1['age_group'] = '18-25'                  # In this u can also find direct way


# In[47]:


data1.head(2)


# In[48]:


data[(data.age_group >=25) & (data.age_group < 40)]


# In[49]:


data2=data[(data.age_group >=25) & (data.age_group < 40)]


# In[50]:


data2.head(2)


# In[51]:


data2.age_group.unique()


# In[52]:


data2['age_group'] = '25-40'


# In[53]:


data2.head(2)


# In[54]:


data3=data[(data.age_group >= 40) & (data.age_group < 55)]


# In[55]:


data3.age_group.unique()


# In[56]:


data3['age_group']= '40-55'


# In[57]:


data4=data[data.age_group>=55]


# In[58]:


data4.head(2)


# In[59]:


data4['age_group']= '55+'


# In[60]:


data4.head(2)


# In[62]:


data = pd.concat([data1,data2,data3,data4])


# In[63]:


data


# In[64]:


data.age_group.unique()


# # Q4) How many samples were collected for each age -group? Which age group had the most samples?

# In[65]:


data.head(3)


# In[67]:


data['age_group'].value_counts()


# # Q5) What proportion of the resondents had opted for the RJD party in both the Vote_Now and  the Past_Vote questions?

# In[68]:


survey.head(2)


# In[69]:


survey.Vote_Now.unique()


# In[72]:


survey[(survey['Vote_Now']=='RJD') & (survey['Past_Vote']=='RJD')]


# In[73]:


811/6867*100


# # Q6) For each day of sample collection , determine the proportion of respondents who were fully satisfied with the performance of the CM. So if there were a total of 1000 samples on day 1 and 300 out of those said they were fully satisfied , then answer would be 0.3.

# In[74]:


survey.head(2)


# In[75]:


survey.CM_satisfaction.unique()


# In[78]:


CM=survey[survey.CM_satisfaction == 'Fully Satisfied']


# In[79]:


CM.head(2)


# In[80]:


CM.collection_date.value_counts()                # when fully satisfied collection is done


# In[81]:


a= CM.collection_date.value_counts()


# In[82]:


survey.collection_date.value_counts()              # orginal data sets of collection is done. 


# In[83]:


b=survey.collection_date.value_counts()


# In[90]:


c=a/b*100
print(c)


# # Q7) Create a day wise proportion of respondents that opted for fully dissatisfied with their MLA. Create a line plot of the result with the date on x - axis and proportion on y- axis.  

# In[91]:


data.head(2)


# In[92]:


data['MLA_satisfaction'].unique()


# In[94]:


MLA=data[data['MLA_satisfaction']=='Fully Dissatisfied']


# In[95]:


MLA.head(3)


# In[100]:


d=MLA.collection_date.value_counts()
print(d)


# In[102]:


e=survey.collection_date.value_counts()
print(e)


# In[103]:


f=d/e*100


# In[104]:


f


# 

# In[105]:


type(f)


# In[108]:


g=pd.DataFrame(f)
g


# In[109]:


type(g)


# In[111]:


g.collection_date.plot(kind='line',figsize=(16,4))


# # Q8) Create a pivot table with index as Past Vote , Column as vote_now and the cell values as the count of samples. 

# In[114]:


survey.pivot_table(index = 'Past_Vote', columns = 'Vote_Now',aggfunc = 'count')


# # Q9)Create a pivot table with index as Past Vote , Column as vote_now and the cell values as the sum of ''weights''. 

# In[118]:


survey.pivot_table(index = 'Past_Vote', columns = 'Vote_Now', values= 'weight', aggfunc='sum')


# # Q10) Create a dataframe by performing a group by over age_group and calculate the count of the total samples under each age_group. 

# In[119]:


data.head(3)


# In[121]:


df1 = data.groupby('age_group').count()


# In[122]:


type(df1)


# # Q11) Create a dataframe by performing a group by over age_group and calculate the count of the total samples for each age_group that opted for the JD(U) party in Vote_Now. 

# In[123]:


data.head(2)


# In[125]:


data.Vote_Now.unique()


# In[131]:


data_jdu=data[data['Vote_Now'] == 'JD(U)']


# In[132]:


type(data_jdu)


# In[133]:


data_jdu.groupby('age_group').count()


# In[134]:


df2=data_jdu.groupby('age_group').count()


# # Q12) Join/merge thetwo dataframes from questions 11 and 10 with common coloumn as a age_group.

# In[ ]:


# pd.merge(df1,df2, on='age_group')               - To  merge two dataframes


# In[135]:


pd.merge(df1,df2, on = 'age_group')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




