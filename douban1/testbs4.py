from bs4 import  BeautifulSoup
import re
file = open("./netbian.html","rb")
html=file.read().decode("gbk")
bs = BeautifulSoup(html,"html.parser")
#print(type(bs.title.string))
#print(bs)
#1.Tag 标签以及其第一个内容

#print(bs.a.string)
#文档的遍历、文档的搜索
#print(bs.head.contents[1])

#更多内容 搜索文档
# #字符串过滤：会查找与字符串完全匹配的内容
#  t_list=bs.find_all("a")
# print(t_list)
name = re.compile(r'<h1>(.*?)</h1>')

downid=re.compile(r'src=/e/public/ViewClick/ViewMore.php?classid=53&id=(.*?)*')
test=re.compile(r'<script *(.*?)</script>')
#正则表达式搜索：使用search()方法来匹配

soup = BeautifulSoup(html,"html.parser")
for i in soup.find_all('html'): #查找符合的
    data = []
    i = str(i)
    n=re.findall(name,i)[0]
    data.append(n)
    id = re.findall(test,i)[5]
    linkid = re.split(';id=',id)[1]
    lid = re.split('&',linkid)[0]
    #src = "/e/public/ViewClick/ViewMore.php?classid=53&amp;id=1&amp;addclick=1" >
print(lid)
# def name_is_exists(tag):
#     return tag.has_attr("name")
#
# t_list = bs.find_all(name_is_exists)
#
# for item in t_list:
#     print(item)

#2.kwargs 参数

# t_list=bs.find_all(id="head")
# t_list=bs.find_all(class_=True)
# t_list = bs.find_all(text = ["hao123","地图","贴吧"])
# t_list = bs.find_all(text=re.compile("a"))

# t_list=bs.find_all("a",limit=3)
#选择器

# t_list=bs.select('#u1')
# t_list=bs.select("head>title")#通过查找子标签
# t_list=bs.select(".mnav ~ .bri")#通过查找兄弟标签
# for item in t_list:
#     print(item)