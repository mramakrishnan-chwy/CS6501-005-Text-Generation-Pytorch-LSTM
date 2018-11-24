
# coding: utf-8

# In[1]:


## Reading the input data
with open('trn-wiki.txt','r',encoding = 'UTF-8') as file:
    wiki_train = file.read().splitlines()
    
train_all = ' '.join(wiki_train)


# In[2]:


data_Test = '123'

