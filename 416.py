import datetime
import time
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=0)
import pandas as pd
import datetime
path = "D:/日常工作/发布站相关/发布站数据/baidu416.csv"
date = pd.read_csv(path,encoding='gbk',header=6)
df = date.drop(['账户','匹配模式','关键词ID','商桥转化','网页转化'],axis=1)
path2 = "D:/日常工作/发布站相关/发布站数据/time_baidu416.csv"
date2 = pd.read_csv(path2,encoding='gbk',header=6)
df2 = date2.drop(['账户','商桥转化','网页转化'],axis=1)
CPC = df[df['消费']>0]['消费'].sum(axis=0) / df[df['点击']>0]['点击'].sum(axis=0)
click = df[df['点击']>0]['点击'].sum(axis=0)
consumption = df[df['消费']>0]['消费'].sum(axis=0)
consumption_cq = df[df['关键词']=='传奇']['消费'].sum(axis=0)
consumption_number = len(df[df['消费']>0]['消费'])
click_number = len(df[df['点击']>0]['点击'])
print("="*5 + str(yesterday) + " 数 据 日 报" + "="*5)
print( str(yesterday) + "截止到"+ str(int(df2['小时'][-1:])) + "点，合计消费：" + str(round(consumption,2)) + "元" )
print(str(yesterday) + "截止到"+ str(int(df2['小时'][-1:])) + "点，合计点击次数为：" + str(click) + "次" )
print("CPC（点击成本）为：" + str(round(CPC,2)) + "元/次" )
print("前50名合计消费：" + str(round(df['消费'].sort_values(ascending = False).head(50).sum(axis=0),3)) + "元" )
print("传奇几个关键词合计消费：" + str(round(consumption_cq,2)) + "元")
df_groupby = df2[['消费','小时']].groupby(by='消费',as_index=False).max()
print(str(yesterday) + "消费高峰时段为：" + str(int(df_groupby['小时'][-1:])) + "点至"+ str(int(df_groupby['小时'][-1:]+1))+"点,高峰时段合计消费为：" + str(int(df_groupby['消费'][-1:])) + "元")
df_mean = df2['消费'][9:-1].mean(axis=0)
print(str(yesterday) + "上午9点到" + str(int(df2['小时'][-1:])) + "点每小时平均消费为：" + str(round(df_mean,2)) + "元")
print("="*20)
print("传奇几个关键词消耗前20名见下表：")
df.sort_values(['消费'], ascending = False).head(20)
