import time  # 引入time模块
import  calendar
def prinsub(par):
    print("hello",par)
    return

ticks = time.time()
localtime=time.localtime(ticks)
#获取格式化的时间 asctime
#asc是将其转为ascall码
ltime=time.asctime(localtime)
#格式化日期strftime
#print (time.strftime("%Y-%m-%d %H:%M:%S %w",time.localtime()))
cal = calendar.month(2016,1)
#$print("以下输入2016年1月的日历",cal)
#print (time.strftime("\n%Y %m %d %H:%M:%S",time.localtime()))
#print ("\n当前时间戳为:", ltime)
