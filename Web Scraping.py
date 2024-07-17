#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')


# In[3]:


print(soup)


# In[4]:


soup.find('table', class_ = 'wikitable sortable')


# In[7]:


table = soup.find_all('table')[1]


# In[8]:


print(table)


# In[82]:


world_titles = soup.find_all('th')[:7]


# In[83]:


world_titles


# In[84]:


world_table_titles = [title.text.strip() for title in world_titles]

print(world_table_titles)


# In[85]:


import pandas as pd


# In[86]:


df = pd.DataFrame(columns=world_table_titles)
df


# In[87]:


column_data = table.find_all('tr')
column_data


# In[97]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [column_data.text.strip() for column_data in row_data]
    #print(individual_row_data)
    length = len(df)
    df.loc[length] = individual_row_data


# In[98]:


print(individual_row_data)


# In[99]:


df


# In[103]:


pd.DataFrame.to_csv(df,'/Users/hasibazami/Downloads/web_scraping')


# In[105]:


df.to_csv('/Users/hasibazami/Downloads/web_scraping.csv')


# In[ ]:




