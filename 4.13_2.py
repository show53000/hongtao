#！/usr/bin/nev python
#-*-coding:utf-8 -*-
#Author :show530

import pandas as pd
path = "D:/日常工作/发布站相关/发布站数据/baidu413.csv"
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns',None)
pd.set_option('display.width',5000)
pd.set_option('mode.chained_assignment',None)
date = pd.read_csv(path,delimiter="\t",encoding='gbk',header=6)
print(date.head(10))

