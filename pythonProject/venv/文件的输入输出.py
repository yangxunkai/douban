#读取函数的区别


#str1 = input("请输入你要输入的值为：")
#print(str1)

#文件的打开和关闭

fo=open("foot.txt","r+")
#fo.write("dfsajifbkjfiuaguifgbuiakcoamcp\n")
str=fo.read(1)#参数代表意思是从头开始读10个有值数
# print(str)
# print("文件名：",fo.name)
# print("是否关闭文件：",fo.closed)
# print("访问模式",fo.mode)
loc=fo.tell()#读取读指针在文件中的位置
print("文件的当前位置为：",loc)
print(str)

position=fo.seek(0,1)#第一个为表示从哪个字节数开始读，第二个参数表示开始移动的字节参考位置
#第二个参数表示：0:表示从开头开始 1：表示从当前位置开始 2：表示从末尾开始作为参考位置
print("当前位置为",position)
str1=fo.read(8)
print(str1)

#


fo.close()
print("是否关闭文件：",fo.closed)
