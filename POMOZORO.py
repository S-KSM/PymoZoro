
# coding: utf-8

# In[48]:

import time
import winsound


# In[49]:

def stopWatch(value):
    for i in range(value):
        print("%d : %d"%((value-i)//60,((value-i)%60)))
        time.sleep(1)
    print("*"*11)
    for i in range(10):
        print(" "*(10 - i)+"*")
    print("*"*11)
    winsound.PlaySound('sound.wav', winsound.SND_FILENAME)


        


# In[50]:

my_session = [30,5,30,5,30,5,30]


# In[51]:

for i in my_session:
    stopWatch(i*60)


# In[ ]:



