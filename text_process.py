#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#text process for turning messages into list of words 

import string 
from nltk.corpus import stopwords
def text_process(mess):
    no_punc=[char for char in mess if char not in string.punctuation]
    no_punc=''.join(no_punc)
    return [word for word in no_punc.split() if word.lower() not in stopwords.words('english')]

