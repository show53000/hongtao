#！/usr/bin/nev python
#-*-coding:utf-8 -*-
#Author :show530
import pandas as pd
data = {'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
        'year':[2000,2001,2002,2001,2002],
        'pop':[1.5,1.7,3.6,2.4,2.9]}
frame = pd.DataFrame(data)
# print(frame)
# print(pd.DataFrame(data,columns=['year','state','pop']))
frame2 = pd.DataFrame(data,columns=['year','state','pop','debt'],index=['one','two','three','four','five'])
# print(frame2['state'])
# print(frame2.year)
val = pd.Series([-1.2,-1.5,-1.7],index=['two','four','five'])
frame2['debt'] = val
frame2['eastern'] = frame2.state == 'Ohio'
del frame2['eastern']
print(frame2)
print(frame2.columns)

