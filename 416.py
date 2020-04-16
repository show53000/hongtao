#！/usr/bin/nev python
#-*-coding:utf-8 -*-
#Author :show530

import datetime
import time
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=2)
import pandas as pd
import datetime
path = "D:/日常工作/发布站相关/发布站数据/baidu414.csv"
date = pd.read_csv(path,encoding='gbk',header=6)
df = date.drop(['账户','匹配模式','关键词ID','商桥转化','网页转化'],axis=1)
CPC = df[df['消费']>0]['消费'].sum(axis=0) / df[df['点击']>0]['点击'].sum(axis=0)
click = df[df['点击']>0]['点击'].sum(axis=0)
consumption = df[df['消费']>0]['消费'].sum(axis=0)
consumption_cq = df[df['关键词']=='传奇']['消费'].sum(axis=0)
consumption_number = len(df[df['消费']>0]['消费'])
click_number = len(df[df['点击']>0]['点击'])
print("="*15 + str(yesterday) + " 数 据 日 报" + "="*15)
print( str(yesterday) + "（截止到24点），合计消费：" + str(round(consumption,2)) + "元" )
print(str(yesterday) + "（截止到24点），合计点击次数为：" + str(click) + "次" )
print("CPC（点击成本）为：" + str(round(CPC,2)) + "元/次" )
print("前50名合计消费：" + str(round(df['消费'].sort_values(ascending = False).head(50).sum(axis=0),3)) + "元" )
print("传奇几个关键词合计消费：" + str(round(consumption_cq,2)) + "元")
print("="*50)
print("传奇几个关键词消耗前20名见下表：")

