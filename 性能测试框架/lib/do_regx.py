# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ess_api
# @File     :do_regx
# @Date     :2021/10/22 10:41
# @Author   :LiuFei
# @Email    :fei.liu@hxgroup.com
# @Software :PyCharm
-------------------------------------------------
"""
import re
from conf.global_data import GlobalData

class DoRegx():
    def do_regx(self, s):
        while re.search("\$\{(.*?)\}", s):
            key = re.search("\$\{(.*?)\}", s).group(0)
            value = re.search("\$\{(.*?)\}", s).group(1)
            s = s.replace(key, str(getattr(GlobalData, value)))
        return s

if __name__ == "__main__":
    s = str({
"adress": "power003",
"agent": "${organization_id}",
"chargingType": None,
"countryValue": "CN",
"currencyUnit": 3,
"downPrice": [{"price": "1.2", "startTime": 0, "endTime": "${liufei}"}],
"installer": None,
"installerName": "",
"isShown": 1,
"latitude": "30",
"longitude": "120",
"name": "power003",
"position": "",
"pvCapacity": 1000,
"systemType": 1,
"timezone": 94,
"timezoneName": "",
"upPrice": [{"price": "1.2", "startTime": 0, "endTime": 86400}]
})
    n = DoRegx().do_regx(s)
    print(n)