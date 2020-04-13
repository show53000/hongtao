#！/usr/bin/nev python
#-*-coding:utf-8 -*-
#Author :show530

import pandas as pd
# import numpy as np
#
# obj = pd.Series([4,-5,6,7],index=['a','b','c','d'])
# print(obj)
# print(obj.values)
# print(obj.index)
# print(obj['a'])

sdata = {'Ohio':35000,'Texas':71000,'Oregon':16000,'Utah':5000}
obj3 = pd.Series(sdata)
# print(obj3)
states = ['California','Ohio','Oregon','Texas']
obj4 = pd.Series(sdata,index=states)
print(obj3+obj4)