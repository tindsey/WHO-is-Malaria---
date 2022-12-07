#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


malaria_df = pd.read_csv('total number of malaria cases.csv', dtype = 'string')

malaria_cases =  malaria_df[['ParentLocation','Location','Period','FactValueNumeric']]
malaria_cases.columns = ['Region','Country','Year','Number of Cases']

#row_index = 'Region'
#malaria_cases = malaria_cases.set_index(row_index)
print(malaria_cases)




# In[3]:


import numpy as np
americas_df = malaria_cases[malaria_cases['Region']== 'Americas']
row_index = 'Region'
americas_df = americas_df.set_index(row_index)
print(americas_df)

europe_df = malaria_cases[malaria_cases['Region']== 'Europe']
row_index = 'Region'
europe_df = europe_df.set_index(row_index)
#print(europe_df)

africa_df = malaria_cases[malaria_cases['Region']== 'Africa']
row_index = 'Region'
africa_df = africa_df.set_index(row_index)
#print(africa_df)

easternmed_df = malaria_cases[malaria_cases['Region']== 'Eastern Mediterranean']
row_index = 'Region'
easternmed_df = easternmed_df.set_index(row_index)
#print(easternmed_df)

westernpacific_df = malaria_cases[malaria_cases['Region']== 'Western Pacific']
row_index = 'Region'
westernpacific_df = westernpacific_df.set_index(row_index)
#print(westernpacific_df)

SEA_df = malaria_cases[malaria_cases['Region']== 'South-East Asia']
row_index = 'Region'
SEA_df = SEA_df.set_index(row_index)
#print(SEA_df)



# In[4]:


america_count = [0]*11
indexOfCount = 0

for year in range (2010,2021):
    for ind, row in americas_df.iterrows(): ## ind = Americas, rows = each row of Americas
        if (int(row['Year']) == int(year)):
            america_count[indexOfCount] += int(row['Number of Cases'])
    indexOfCount += 1
    
years = range(2010,2021)
#print(years)
#print(america_count)
plt.bar(years,america_count)
plt.title('Malaria Cases in Americas from 2010-2020')
plt.xticks(np.arange(min(years), max(years)+1, 1.0))
plt.xlabel('Year')
plt.ylabel('Number of Cases')
plt.show()




# In[22]:


europe_count = [0]*11
indexOfCount = 0

for year in range (2010,2021):
    for ind, row in europe_df.iterrows(): ## ind = Europe, rows = each row of Americas
        if (int(row['Year']) == int(year)):
            europe_count[indexOfCount] += int(row['Number of Cases'])
    indexOfCount += 1
    
years = range(2010,2021)
#print(years)
#print(europe_count)
plt.bar(years,europe_count, color= 'purple')
plt.title('Malaria Cases in Europe from 2010-2020')
plt.xticks(np.arange(min(years), max(years)+1, 1.0))
plt.xlabel('Year')
plt.ylabel('Number of Cases')
plt.show()


# In[21]:


africa_count = [0]*11
indexOfCount = 0

for year in range (2010,2021):
    for ind, row in africa_df.iterrows(): ## ind = Africa, rows = each row of Americas
        if (int(row['Year']) == int(year)):
            africa_count[indexOfCount] += int(row['Number of Cases'])
    indexOfCount += 1
    
years = range(2010,2021)
#print(years)
#print(america_count)
plt.bar(years,africa_count, color='green')
plt.title('Malaria Cases in Africa from 2010-2020')
plt.xticks(np.arange(min(years), max(years)+1, 1.0))
plt.xlabel('Year')
plt.ylabel('Number of Cases')
plt.ticklabel_format(useOffset=False, style='plain')
plt.show()


# In[20]:


easternmed_count = [0]*11
indexOfCount = 0

for year in range (2010,2021):
    for ind, row in easternmed_df.iterrows(): ## ind = Eastern Med , rows = each row of Americas
        if (int(row['Year']) == int(year)):
            easternmed_count[indexOfCount] += int(row['Number of Cases'])
    indexOfCount += 1
    
years = range(2010,2021)
#print(years)
#print(easternmed_count)
plt.bar(years,easternmed_count, color = 'yellow')
plt.title('Malaria Cases in the Eastern Mediterranean from 2010-2020')
plt.xticks(np.arange(min(years), max(years)+1, 1.0))
plt.xlabel('Year')
plt.ylabel('Number of Cases')
plt.ticklabel_format(useOffset=False, style='plain')
plt.show()


# In[19]:


westernpacific_count = [0]*11
indexOfCount = 0

for year in range (2010,2021):
    for ind, row in westernpacific_df.iterrows(): ## ind = Western Pacific, rows = each row of Americas
        if (int(row['Year']) == int(year)):
            westernpacific_count[indexOfCount] += int(row['Number of Cases'])
    indexOfCount += 1
    
years = range(2010,2021)
#print(years)
#print(westernpacific_count)
plt.bar(years,westernpacific_count, color = 'orange')
plt.title('Malaria Cases in the Western Pacific from 2010-2020')
plt.xticks(np.arange(min(years), max(years)+1, 1.0))
plt.xlabel('Year')
plt.ylabel('Number of Cases')
plt.ticklabel_format(useOffset=False, style='plain')
plt.show()



# In[18]:


SEA_count = [0]*11
indexOfCount = 0

for year in range (2010,2021):
    for ind, row in SEA_df.iterrows(): ## ind = SouthEast Asia, rows = each row of Americas
        if (int(row['Year']) == int(year)):
            SEA_count[indexOfCount] += int(row['Number of Cases'])
    indexOfCount += 1
    
years = range(2010,2021)
#print(years)
#print(SEA_count)
plt.bar(years,SEA_count, color ='red')
plt.title('Malaria Cases in Southeast Asia from 2010-2020')
plt.xticks(np.arange(min(years), max(years)+1, 1.0))
plt.xlabel('Year')
plt.ylabel('Number of Cases')
plt.ticklabel_format(useOffset=False, style='plain')
plt.show()

