from bs4 import  BeautifulSoup #网页解析，获取数据
import sys #正则表达式，进行文字匹配
import re
import urllib.request,urllib.error #指定url，获取网页数据
import xlwt #使用表格
import sqlite3
import lxml

def main():
    baseurl ="https://movie.douban.com/top250?start="
    datalist = getData(baseurl)
    savepath=('douban.xls')
    saveData(datalist,savepath)
#影片播放链接
findLink = re.compile(r'<a href="(.*?)">')  #创建正则表达式对象，表示规则（字符串的模式）
#影片图片
findImg = re.compile(r'<img.*src="(.*?)" width="100"/>',re.S)#re.S取消换行符
#影片片面
findtitle= re.compile(r'<span class="title">(.*?)</span>')
#影片评分
fileRating = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
#找到评价的人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
#找到概识
findInq =re.compile(r'<span class="inq">(.*?)</span>')
#找到影片的相关内容
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)

def getData(baseurl):
    datalist=[]
    for i in range(0,10):#调用获取页面的函数10次
        url = baseurl + str(i*25)
        html = askURl(url)
    #逐一解析
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"):
        #print(item)
            data=[]
            item = str(item)

            link = re.findall(findLink,item)[0] #re库用来通过正则表达式查找指定的字符串
            data.append(link)
            titles =re.findall(findtitle,item)
            if(len(titles)==2):
                ctitle=titles[0].replace('\xa0',"")
                data.append(ctitle)#添加中文名
                otitle = titles[1].replace("\xa0/\xa0Perfume:","")
                data.append(otitle)#添加外国名
            else:
                data.append(titles[0])
                data.append(' ')#外国名字留空

            imgSrc = re.findall(findImg,item)[0]
            data.append(imgSrc)

            rating=re.findall(fileRating,item)[0]
            data.append(rating)

            judgenum = re.findall(findJudge,item)[0]
            data.append(judgenum)

            inq=re.findall(findInq,item)
            if len(inq) != 0:
                inq =inq[0].replace(".","")
                data.append(inq)
            else:
                data.append(" ")
            bd=re.findall(findBd,item)[0]
            bd=re.sub('<br(\s+)?/>(\s+)?'," ",bd) #去掉<br/>
            bd =re.sub('\xa0'," ",bd)
            data.append(bd.strip())  #去掉前后的空格

            datalist.append(data)  #把处理好的一部电影信息放入datalist

    return datalist

#得到指定一个url的网页内容
def askURl(url):

    head = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;WOW64) Apple"
        +"WebKit / 537.36(KHTML, likeGecko) Chrome / 78.0.3904.108 Safari / 537.36"
    }
#告诉豆瓣我们是浏览器我们可以接受什么水平的内容
    request = urllib.request.Request(url,headers=head)
    html=""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return  html

def saveData(datalist,savepath):
    print("保存中。。。")
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('douban',cell_overwrite_ok=True)  #创建工作表 cell_overwrite_ok表示直接覆盖
    col = ("电影详情链接","影片中文网","影片外国名","图片链接","评分","评价数","概况","相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i])
    for i in range(0,250):
        print("第%d条" %(i+1))
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])

    book.save(savepath)


def saveData2DB(datalist,dbpath):
    print("...")
def init_db(dbpath):
    sql = """create table movie250
        (
        id integer primary key autoincrement,
        info_link text,      
        cname varchar,
        ename varchar,
        pic_link text,
        score numeric,
        rated numeric,
        instroduction text,
        info text
        )"""
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    #main()
    init_db("movietest.db")
    print("okokoko!")