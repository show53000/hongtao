#！/usr/bin/nev python
#-*-coding:utf-8 -*-
#Author :show530

import pandas as pd

path = "D:/日常工作/发布站相关/发布站数据/new_word_report_20200412-20200412_661758.csv"

date = pd.read_csv(path,encoding='gbk',error_bad_lines=False)
csv_date = date.drop(date.index[4])
df = pd.DataFrame(csv_date)
print(df)
