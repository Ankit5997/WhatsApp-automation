#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import pandas as pd
import random
from time import sleep
import os
from openpyxl import load_workbook
from selenium.webdriver.common.keys import Keys


# In[2]:


def NoAttach():
    driver.find_element_by_xpath('//span[@data-icon="send"]').click()
    sleep(random.randint(4,10))


# In[5]:


t1 = "Hi"
t2 = "This"
t3 = "is"
t4 = "a Testing"
t5 = "Message"

y = ['918800580566']

driver = webdriver.Chrome()
for i in range(len(y)):
    #name=cd['Name'][i]
    phone=y[i]
    
    message='''Dear,                                                                                                                                                                                             {j}
                                                                                                                                                         {k}
                                                                                                                                                            {l}
                                                                                                                                                            {m}
                                                                                                                                          {n}'''.format(j=t1, k=t2,l=t3,m=t4,n=t5)
    
    
    driver.get('https://web.whatsapp.com/send?phone='+phone+'&text='+message)
    sleep(30)
    NoAttach()

