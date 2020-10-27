import xlwt

# workbook = xlwt.Workbook(encoding="utf-8")#创建workbook对象
# worksheet = workbook.add_sheet('sheet1')
# worksheet.write(0,0,"hello")  #写入数据，第一个参数表示行，第二个参数表示列，第三个表示参数内容
# workbook.save('student.xls')

workbook = xlwt.Workbook(encoding="utf-8")#创建workbook对象
worksheet = workbook.add_sheet('sheet1')
for i in range(0,9):
    for j in range(0,i+1):
        worksheet.write(i,j,"%d * %d = %d"%(i+1,j+1,(i+1)*(j+1)))
        workbook.save('student.xls')