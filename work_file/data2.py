# -*- coding: utf-8 -*-
# @Time :2021/7/12 15:58
# @Author : liufei
# @File :data2.PY

from openpyxl import load_workbook

def data_source():
    test_data=[]
    with open(r'D:\Python_files\Test_Development\work_file\moke(1).txt', mode='r') as f:
        row_data = f.readlines()
        for i in row_data:
            test_data.append(i.strip('\n'))
        return test_data



data = data_source()
print(data)