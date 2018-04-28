import  xlrd as xlsr
import  xlwt as xlsw
import sys
from datetime import datetime,date,time
from exam.importExcel.readRoundData import operExcel as opE
import openpyxl as  advRWE
'''
这里介绍了常用的解析excel的方法和参数
'''
data= None
sheet= None
filePath=r'D:\11.xls'
if len(filePath.split(r'.'))>2:
    print('文件名非法%s'%filePath)
elif filePath.split(r'.')[1]=='xls':
    data = xlsr.open_workbook(filePath, formatting_info=True)
    exl_sheet= data.sheet_by_index(0)
    print(opE.data2ArrFor2003(data,exl_sheet))
else:
    data = advRWE.load_workbook(filePath)
    sheet=data.active
    print(opE.data2ArrFor2007(sheet))
