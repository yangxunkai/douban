import  os
#重命名文件
#os.rename("foot.txt","fooot.txt")

aa=open("test1.txt","a+")
aa.close()
os.remove("test1.txt")

#os.mkdir("test")
print( os.getcwd())
os.rmdir("test")