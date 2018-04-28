import  xlrd as xlsr
import  xlwt as xlsw
import sys
from datetime import datetime,date,time
from exam.importExcel.readRoundData import OperExcel as opE
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
    workbook_data = xlsr.open_workbook(filePath, formatting_info=True)
    exl_sheet= workbook_data.sheet_by_index(0)

    print(opE.data2arr_for2003(workbook_data,exl_sheet))
else:
    workbook_data = advRWE.load_workbook(filePath)
    sheet=data.active
    opE.write_onerow_for2007(workbook_data, filePath, exl_sheet, ['1', '2', '3'])
    print(opE.data2arr_for2007(sheet))
