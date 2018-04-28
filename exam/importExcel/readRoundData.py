import xlrd as xlsr
from datetime import datetime


# 操作数据
class OperExcel:

    def data2arr_for2003(workbook_data, exl_sheet):
        '''
        将excel封装成一个二位数组,暂时只支持xls.
        :param self
        :param data excel的文件对象，用来解决Date的问题
        :type workbook
        :param exl_sheet exceld sheet对象 ，必须要formatting_info=True
        :type sheet
        '''
        xlsArr = []
        tempCell = {}
        for merged_cell in exl_sheet.merged_cells:
            min_row, max_row, min_col, max_col = merged_cell
            for firstStr in range(min_row, max_row ):
                for sedStr in range(min_col, max_col):
                    tempCell[str(firstStr) + str(sedStr)] = \
                        exl_sheet.cell(min_row, min_col).value
        for row_index in range(exl_sheet.nrows):
            rowarr = []
            for col_index in range(exl_sheet.ncols):
                '''这里判断当前单元格是否为空，为空是就取上个单元格的值，如果上一个也没值就取上上个，
                主要解决合并单元格的问题，但单元格本身为空时无法解决，下一次解决，xls是可以解决的
                ，已经解决'''
                if exl_sheet.cell(row_index,col_index).value=='':
                    if str(row_index)+str(col_index) in tempCell.keys():
                        rowarr.append(tempCell.get(str(row_index)+str(col_index)))
                    else:
                        rowarr.append('')
                else:
                    if exl_sheet.cell(row_index,
                                col_index).ctype==3:
                        date_value=xlsr.xldate_as_tuple(exl_sheet.cell(row_index,col_index).value,workbook_data.datemode)
                        date_tmp=datetime(*date_value).strftime('%Y/%m/%d %H:%M:%S')
                        rowarr.append(date_tmp)
                    else:
                        rowarr.append(exl_sheet.cell(row_index,
                                              col_index).value)
            xlsArr.append(rowarr)
        return xlsArr


    def data2arr_for2007(exl_sheet):
        '''
        将excel封装成一个二位数组,暂时只支持xlsx.
        :param exl_sheet exceld sheet对象
        :type sheet
        '''
        #将合并单元格的格子都赋值成一个值，先存到一个字典中
        tempCell = {}
        for mergCells in exl_sheet.merged_cells:
            for firstStr in range(mergCells.min_row, mergCells.max_row + 1):
                for sedStr in range(mergCells.min_col, mergCells.max_col + 1):
                    tempCell[str(firstStr) + str(sedStr)] = \
                        exl_sheet.cell(mergCells.min_row, mergCells.min_col).value
        # 计算出第一行的列数，按此列数循环
        counter = 0
        for firRow in exl_sheet.rows:
            for a in firRow:
                counter += 1
            break
        xlsarr = []
        for row_index in range(exl_sheet.max_row):
            rowarr = []
            #只取第一行的列数
            for clo_index in range(counter):
                #下标从一开始所以都要加1
                if exl_sheet.cell(row_index + 1, clo_index + 1).value is None:
                    if str(row_index) + str(row_index + 1) in tempCell.keys():
                        rowarr.append(tempCell[str(row_index) + str(row_index + 1)])
                    else:
                        rowarr.append('')
                else:
                    if isinstance(exl_sheet.cell(row_index + 1, clo_index + 1).value, datetime):
                        rowarr.append(exl_sheet.cell(row_index + 1, clo_index + 1).value.strftime('%Y/%m/%d %H:%M:%S'))
                    else:
                        rowarr.append(exl_sheet.cell(row_index + 1, clo_index + 1).value)
            xlsarr.append(rowarr)
        return xlsarr

    def write_onerow_for2007(workbook_data,filePath,exl_sheet,valuesArr):
         '''
         在excel文件的最后插入一行数据,
         :param filePath: 文件路径
         :type String
         :param exl_sheet: excel的sheet对象
         :param valuesArr: 需要插入的值数组
         :return:true，flase
         '''
         for cell_index in range(1,len(valuesArr)+1):
            exl_sheet.cell(exl_sheet.max_row + 1, cell_index, valuesArr[cell_index-1])
         workbook_data.save(filePath)




