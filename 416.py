import datetime
import time
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
import pandas as pd
import datetime
path = "D:/日常工作/发布站相关/发布站数据/baidu415.csv"
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
path2 = "D:/日常工作/发布站相关/发布站数据/time_baidu415.csv"
date2 = pd.read_csv(path2,encoding='gbk',header=6)
df2 = date2.drop(['账户','商桥转化','网页转化','小时'],axis=1)
df2['时段'] = ['0点-1点','1点-2点','2点-3点','3点-4点','4点-5点','5点-6点','6点-7点','7点-8点','8点-9点','9点-10点','10点-11点','11点-12点','12点-13点','13点-14点','14点-15点','15点-16点','16点-17点','17点-18点','18点-19点','19点-20点','20点-21点','21点-22点','22点-23点','23点-24点']
df_groupby = df2[['消费','时段']].groupby(by='消费',as_index=False).max()
print(str(yesterday) + "消费高峰时段为：" + str(df_groupby['时段'][23]) + ",高峰时段合计消费为：" + str(df_groupby['消费'][23]) + "元")
df_mean = df2['消费'][9:23].mean(axis=0)
print(str(yesterday) + "上午9点到24点每小时平均消费为：" + str(round(df_mean,2)) + "元")
print("="*50)
print("传奇几个关键词消耗前20名见下表：")
df.sort_values(['消费'], ascending = False).head(20)