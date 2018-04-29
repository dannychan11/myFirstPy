"""日模块将所有操作excel的方法进行提供，并提供main方法调试"""

from datetime import datetime

import xlrd
from xlutils.copy import copy


def read_excel_for2003(workbook_, sheet_):
    """
    将excel封装成一个二位数组,暂时只支持xls.

    :param workbook_: excel的文件对象，用来解决日期问题的问题

    :param sheet_: sheet对象 ，必须要formatting_info=True

    :return xls_list: 返回一个二维数组

    """
    xls_list = []  # 存储最终结果集
    temp_cell = {}  # 存储合并单元格的位置与值的字典
    for merged_cell in sheet_.merged_cells:  # 将合并单元格的数据都赋值成同一个
        min_row, max_row, min_col, max_col = merged_cell
        for start_row_index in range(min_row, max_row):
            for endCol_index in range(min_col, max_col):
                temp_cell[str(start_row_index) + str(endCol_index)] = sheet_.cell(min_row, min_col).value
    for row_index in range(sheet_.nrows):
        row_list = []  # 存储每一行的数据
        for col_index in range(sheet_.ncols):
            """ 这里判断当前单元格是否为空，为空是就取上个单元格的值，如果上一个也没值就取上上个，
            主要解决合并单元格的问题，但单元格本身为空时无法解决，下一次解决，xls是可以解决的。
            2018-4-29，肖志君修改将2003版本与2007版本分开读写都是               
            """
            if sheet_.cell(row_index, col_index).value == '':
                if str(row_index)+str(col_index) in temp_cell.keys():
                    row_list.append(temp_cell.get(str(row_index)+str(col_index)))
                else:
                    row_list.append('')
            else:
                if sheet_.cell(row_index, col_index).ctype == 3:
                    date_value = xlrd.xldate_as_tuple(sheet_.cell(row_index,
                                                                  col_index).value, workbook_.datemode)
                    date_tmp = datetime(*date_value).strftime('%Y/%m/%d %H:%M:%S')
                    row_list.append(date_tmp)
                else:
                    row_list.append(sheet_.cell(row_index, col_index).value)
        xls_list.append(row_list)
    return xls_list


def read_excel_for2007(sheet_):
    """
    将excel封装成一个二位数组,暂时只支持xlsx.

    :param sheet_: excel的sheet对象

    :return: 二维数组

    """

    temp_cell = {}  # 将合并单元格的格子都赋值成一个值，先存到一个字典中
    for merged_cell in sheet_.merged_cells:
        for first_str in range(merged_cell.min_row, merged_cell.max_row + 1):
            for sedStr in range(merged_cell.min_col, merged_cell.max_col + 1):
                temp_cell[str(first_str) + str(sedStr)] = \
                    sheet_.cell(merged_cell.min_row, merged_cell.min_col).value

    clo_num = 0  # 计算出第一行的列数，按此列数循环
    for row_ in sheet_.rows:
        clo_num = len(row_)
        break
    xls_list = []
    for row_index in range(sheet_.max_row):
        row_list = []  # 只取第一行的列数
        for clo_index in range(clo_num):
            if sheet_.cell(row_index + 1, clo_index + 1).value is None:  # 下标从一开始所以都要加1
                if str(row_index) + str(row_index + 1) in temp_cell.keys():
                    row_list.append(temp_cell[str(row_index) + str(row_index + 1)])
                else:
                    row_list.append('')
            else:
                if isinstance(sheet_.cell(row_index + 1, clo_index + 1).value, datetime):
                    row_list.append(sheet_.cell(row_index + 1, clo_index + 1).value.strftime('%Y/%m/%d %H:%M:%S'))
                else:
                    row_list.append(sheet_.cell(row_index + 1, clo_index + 1).value)
        xls_list.append(row_list)
    return xls_list


def write_row_for2007(workbook_, file_path_, sheet_, value_list):
    """
    在excel文件的最后插入一行数据.

    :param workbook_: excel object

    :param file_path_: 文件路径

    :param sheet_: sheet object

    :param value_list: 需要插入的值数组

    """
    max_row_index = sheet_.max_row
    for cell_index in range(1, len(value_list) + 1):
        sheet_.cell(max_row_index + 1, cell_index, value_list[cell_index - 1])
    workbook_.save(file_path_)


def write_row_for2003(workbook_, file_path_, sheet_, value_list):
    """
    在excel文件的最后插入一行数据.

    :param workbook_: 文件对象必须要formatting_info=True

    :param file_path_: 文件路径

    :param sheet_: excel的sheet对象

    :param value_list: 需要插入的值数组

    """
    new_wb = copy(workbook_)
    new_sheet = new_wb.get_sheet(0)
    for cell_index in range(0, len(value_list)):
        if isinstance(value_list[cell_index], datetime):
            new_sheet.write(sheet_.nrows, cell_index, value_list[cell_index].strftime('%Y/%m/%d %H:%M:%S'))
        else:
            new_sheet.write(sheet_.nrows, cell_index, value_list[cell_index])
    new_wb.save(file_path_)


class FileNamedError(Exception):
    def __init__(self, err='文件命名异常'):
        super(FileNamedError, self).__init__(self, err)


if __name__ == '__main__':  # 此为测试方法
    file_path_test = r'D:\11.xls'
    if len(file_path_test.split(r'.')) > 2:
        raise FileNamedError('文件名非法%s' % file_path_test)
    elif file_path_test.split(r'.')[1] == 'xls':
        workbook_w = xlrd.open_workbook(file_path_test, formatting_info=True)
        sheet_w = workbook_w.sheet_by_index(0)
        write_row_for2003(workbook_w, file_path_test, sheet_w,
                          ['1', '2', '3', '2018/1/3  12:12:12', datetime.now()])
        workbook_r = xlrd.open_workbook(file_path_test, formatting_info=True)
        sheet_r = workbook_r.sheet_by_index(0)
        print(read_excel_for2003(workbook_r, sheet_r))
    elif file_path_test.split(r'.')[1] == 'xlsx':
        import openpyxl
        workbook_adv = openpyxl.load_workbook(file_path_test)
        sheet_adv = workbook_adv.active
        write_row_for2007(workbook_adv, file_path_test, sheet_adv,
                          ['1', '2', '3', '2018/1/3  12:12:12', datetime.now()])
        print(read_excel_for2007(sheet_adv))
    else:
        raise FileNamedError('文件名非法%s' % file_path_test)
