#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def fun(s):
    # return True if s is a valid email, else return Falseret
    try:
        username, url =s.split('@')
        website,extension =url.split('.')
    except ValueError:
        return False
    
    if username.replace('_','').replace('_','').isalnum() is False:
        return False
    
    elif website.isalnum() is False:
        return False
    
    elif len(extension) > 3:
        return False
    
    else:
        return True

