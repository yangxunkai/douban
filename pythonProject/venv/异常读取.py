
# try:
#     fh=open("file","w")
#     fh.write("这是一个测试文件，用于测试异常")
# except IOError:
#     print("Error:没有找到该文件或者读取文件失败")
# else:
#     print("内容写入成功")
#     fh.close()

import  os
os.remove("file")