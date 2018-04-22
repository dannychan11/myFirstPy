import  xlrd as xlsr
import  xlwt as xlsw
import sys
from datetime import datetime,date,time
from exam.importExcel.readRoundData import operExcel as opE
'''
这里介绍了常用的解析excel的方法和参数
'''
data = xlsr.open_workbook(r'D:\11.xlsx',formatting_info=True)
sheetNum=data.nsheets #返回excel的sheet数量
sheetnames=data.sheet_names() #返回excel的各个sheet名称的元祖
sheet1= data.sheet_by_index(0) #取第几个sheet的对象
for sheet in data.sheets(): #遍历所有sheet
    print(opE.data2Arr(data,sheet))
