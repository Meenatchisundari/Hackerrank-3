#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def wrapper(f):
    def fun(l):
        # complete the function
        # Standardize Mobile Number Using Decorators in python - Hacker Rank Solution START
        f(['+91 ' + c[-10:-5] + ' ' + c[-5:] for c in l])
        # Standardize Mobile Number Using Decorators in python - Hacker Rank Solution END
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 

