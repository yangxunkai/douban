from bs4 import  BeautifulSoup #网页解析，获取数据
import sys #正则表达式，进行文字匹配
import re
import urllib.request,urllib.error #指定url，获取网页数据
import xlwt #使用表格
import urllib
import sqlite3
import lxml
def main():
    baseurl ="http://pic.netbian.com/tupian/"
    datalist = getData(baseurl)


    savepath=('彼岸图下载.xls')
    # askURl("https://movie.douban.com/top250?start=")
    saveData(datalist,savepath)
name = re.compile(r'<h1>(.*?)</h1>')
im = re.compile(r'src="(.*?)"')
lid=re.compile(r'<script *(.*?)</script>')
    #downlink = "http://pic.netbian.com/downpic.php?id="+downlinkid+"&classid=55"
def getData(baseurl):
    datalist=[]
    global me
    me=0
    for i in range(1,10000):#调用获取页面的函数10次

        if(i==1):url="http://pic.netbian.com/tupian/1.html"
        else:
            url = baseurl + str(i)+".html"
        me+=1
        html = askURl(url)
        if(html==""):me-=1
        print("加载第%d个网页"%(i))


    #逐一解析
        soup = BeautifulSoup(html,"html.parser")
        for i in soup.find_all('html'):  # 查找符合的
            data = []
            i = str(i)
            lookimg = "http://pic.netbian.com/" + re.findall(im, i)[3]
            data.append(lookimg)
            n = re.findall(name, i)[0]
            data.append(n)
            id = re.findall(lid, i)[5]
            linkid = re.split(';id=', id)[1]
            lnid = re.split('&', linkid)[0]
            downlink = "http://pic.netbian.com/downpic.php?id=" + lnid + "&classid=55"
            data.append(downlink)

            datalist.append(data)

    return datalist

def askURl(url):

    head = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 78.0.3904.108 Safari / 537.36"
    }
#告诉豆瓣我们是浏览器我们可以接受什么水平的内容
    request = urllib.request.Request(url,headers=head)
    html=""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("gbk")
        # print(html)
    except urllib.error.URLError as e:

        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
        html=""
    return  html



def saveData(datalist,savepath):
    print("保存中。。。")
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象

    sheet = book.add_sheet('douban', cell_overwrite_ok=True)  # 创建工作表 cell_overwrite_ok表示直接覆盖
    col = ("图片详情链接", "图片名字", "图片下载链接")
    for i in range(0, 3):
        sheet.write(0, i, col[i])
    for i in range(0, me):

        print("第%d张" % (i + 1))
        data = datalist[i]
        for j in range(0, 3):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)

if __name__ == '__main__':
    me=0
    main()