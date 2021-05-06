#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns


# In[8]:


ipl=pd.read_csv(r"C:\Users\user\Downloads\ipl data.csv")


# In[9]:


ipl.head()


# In[10]:


ipl.shape


# # Player of the Match

# In[11]:


ipl['player_of_match'].value_counts()


# In[12]:


ipl['player_of_match'].value_counts()[0:10]


# In[13]:


ipl['player_of_match'].value_counts()[0:5]


# In[14]:


plt.figure(figsize=(15,10))
plt.bar(list(ipl['player_of_match'].value_counts()[0:10].keys()),list(ipl['player_of_match'].value_counts()[0:10]),color=["r","g","gold","b","orange","purple","gold","gold","purple","silver"])
plt.show()


# # Results

# In[15]:


ipl['result'].value_counts()


# # Toss Winning Teams

# In[16]:


ipl['toss_winner'].value_counts()


# # Batting First

# In[17]:


batting_first=ipl[ipl['win_by_runs']!=0]


# In[18]:


batting_first.head()


# In[19]:


plt.figure(figsize=(10,10))
plt.hist(batting_first['win_by_runs'],bins=30)
plt.show()


# In[20]:


batting_first['winner'].value_counts()


# In[21]:


plt.figure(figsize=(13,10))
plt.bar(list(batting_first['winner'].value_counts()[0:5].keys()),list(batting_first['winner'].value_counts()[0:5]),color=["blue","yellow","pink","purple","r"])
plt.show()


# In[22]:


plt.figure(figsize=(13,13))
plt.pie(list(batting_first['winner'].value_counts()),labels=list(batting_first['winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()


# # Batting Second

# In[23]:


BS= ipl[ipl['win_by_wickets']!=0]


# In[24]:


BS.head()


# In[25]:


plt.figure(figsize=(10,6))
plt.hist(BS['win_by_wickets'],bins=20)
plt.show()


# In[26]:


BS['winner'].value_counts()


# In[27]:


plt.figure(figsize=(13,10))
plt.bar(list(BS['winner'].value_counts()[0:5].keys()),list(BS['winner'].value_counts()[0:5]),color=["purple","b","r","yellow","pink"])
plt.show()


# In[28]:


plt.figure(figsize=(13,13))
plt.pie(list(BS['winner'].value_counts()),labels=list(BS['winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()


# # Matches Each Season

# In[29]:


ipl['season'].value_counts()


# # Matches Each City

# In[30]:


ipl["city"].value_counts()


# # Finding out how many times a team has won the match after winning the toss?

# In[31]:


np.sum(ipl['toss_winner']==ipl["winner"])


# In[32]:


393/756


# # New Data

# In[34]:


D=pd.read_csv('D:\Certifications\IPL Data\deliveries.csv')


# In[35]:


D.head()


# In[38]:


D['match_id'].unique()


# In[39]:


match_2=D[D['match_id']==2]


# In[48]:


match_2


# In[41]:


match_2.shape


# In[42]:


MI=match_2[match_2['inning']==1]


# In[43]:


MI['batsman_runs'].value_counts()


# In[44]:


MI['dismissal_kind'].value_counts()


# In[45]:


RSP=match_2[match_2['inning']==2]


# In[46]:


RSP['batsman_runs'].value_counts()


# In[47]:


RSP['dismissal_kind'].value_counts()


# In[ ]:




