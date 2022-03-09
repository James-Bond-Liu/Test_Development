# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :test_data
# @File     :GetInverterData2
# @Date     :2022/1/7 9:44
# @Author   :LiuFei
# @Email    :fei.liu@hxgroup.com
# @Software :PyCharm
-------------------------------------------------
"""
"""新机型"""
# 每5分钟发送一次数据
import random, requests, datetime, time, sys,logging

ayear = None
amonth = None
aday = None
E_Today = 0
E_Month = 0
E_Year = 0
E_Total = 0
time_number = 0
E_five = 0

class First():

    def get_sn(self):
        sn = []
        for i in range(1, 501):
            s = 'snjj'+str(i)
            sn.append(s)
        return sn

    def write_total(self, data):
        with open(r'data1.txt', mode='w', encoding='utf-8') as file:
            file.write(data)
    def read_total(self):
        with open(r'data1.txt', mode='r', encoding='utf-8') as file:
            data = file.readlines()
        return data

    def get_data(self):
        global ayear, aday, amonth, E_Today, E_Year, E_Total, E_Month, time_number,E_five
        sn_data = self.get_sn()
        test_data = []
        for sn in sn_data:
            B1 = f'RS 1.5,{sn},000_100000_1_DD'
            B2 = 'CN0000,G9500-058300-00_000119,AU0200'

            V1 = 15  # 0.1V
            I1 = 150  # 0.01A
            M1 = f'{V1},{I1},{15000},{I1}' # 0.1v,0.01A,0.1w,0.01A
            V2 = 15
            I2 = 150
            M2 = f'{V2},{I2},{15000},{I2}'
            V3 = 15
            I3 = 150
            M3 = f'{V3},{I3},{15000},{I3}'
            p_total = 45000  # 0.1w
            time1 = (datetime.datetime.now().strftime('%Y%m%d'))
            day = time1[0:8]
            time2 = (datetime.datetime.now().strftime('%H%M'))
            hour = time2[0:2]
            minute1 = time2[2]
            minute2 = int(time2[3])
            if minute2 > 5:
                time3 = hour + minute1 + '5'
            if minute2 < 5:
                time3 = hour + minute1 + '0'
            if minute2 == 5:
                time3 = time2
            MAIN = f'15000,{E_Today},{E_Month},{E_Year},{E_Total},{time_number * 5},36,3,{day},{time3},0'
            AC = f'{p_total},5000,{V1},{I1},{V2},{I2},{V3},{I3}'
            test_data1 = f'B1={B1}&B2={B2}&MAIN={MAIN}&M1={M1}&M2={M2}&M3={M3}&AC={AC}'
            test_data.append(test_data1)
        return test_data


    def out_log(self):
        logger = logging.getLogger('PANDA')  # 设定日志器，并取名
        logger.setLevel('DEBUG')  # 用来设定日志级别
        if not logger.handlers:
            ch = logging.FileHandler('./report.log', encoding='utf-8')
            # 设定格式器
            formatter = logging.Formatter(fmt="%(asctime)s %(name)s %(levelname)s %(filename)s %(message)s",
                                          datefmt="%Y-%m-%d %H:%M:%S")
            ch.setFormatter(formatter)  # 将格式器加入到处理器中
            logger.addHandler(ch)
        return logger

    def run(self):
        global time_number
        global E_Today, E_Year, E_Total, E_Month, aday, ayear, amonth
        logger = self.out_log()
        while True:
            time_number += 1
            time2 = (datetime.datetime.now().strftime('%Y%m%d'))
            day = time2[0:8]
            year = time2[0:4]
            month = time2[0:6]
            if ayear is None or ayear == year:
                ayear = year
                E_Year += 1
            else:
                ayear = year
                E_Year = 0
            if amonth is None or amonth == month:
                amonth = month
                E_Month += 1
            else:
                amonth = month
                E_Month = 0
            if aday is None or aday == day:
                aday = day
                E_Today += 1
            else:
                aday = day
                E_Today = 0
            read_total = self.read_total()
            E_Total = int(read_total[0]) + 1
            # E_Total += 1
            data1 = self.get_data()
            for request_data in data1:
                sn = request_data.split(',')[1]
                logger.info(f'盛能杰{sn}::request_data{str(time_number)}::{request_data}')
                header = {'Connection':'close'}
                res1 = requests.post(url='http://192.168.108.160:10003/Fes/GetInverterData2', data=request_data, headers = header)
                logger.info(f'盛能杰{sn}::reponse_data{str(time_number)}::{res1.status_code}::{res1.text}')
            write_data = f'{str(E_Total)}'
            self.write_total(write_data)
            time.sleep(300)

if __name__ == '__main__':
    f = First()
    while True:
        f.run()
