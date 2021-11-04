# -*- coding: utf-8 -*-
# @Time :2021/7/8 13:14
# @Author : liufei
# @File :data.PY
import pandas as pd


# class GetData():
#     def __init__(self,file_name,sheet_name):
#         self.file_name = file_name
#         self.sheet_name = sheet_name

def get_data():
    test_data = {}
    df = pd.read_excel(r'D:\Python_files\Test_Development\work_file\数据.xlsx', sheet_name='GetProbes')
    data = df.iloc[0, 0]
    # print(data)


    for i in data:
        if i == 'target':
            data[i]['ip']='**'
            data[i]['port']='**'
            data[i]['protocol']='**'
        elif i == 'mac':
            data[i]='**'
        elif i == 'devname':
            data[i]='**'
        elif i == 'pppoename':
            data[i]='**'
        elif i == 'gateway_mac':
            data[i]='**'
        elif i == 'logic_id':
            data[i]='**'
        elif i == 'scan_id':
            data[i]='**'
    return data
data = get_data()
print(data)



