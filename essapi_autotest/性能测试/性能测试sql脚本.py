# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :essapi_autotest
# @File     :性能测试sql脚本
# @Date     :2021/12/9 10:07
# @Author   :LiuFei
# @Email    :fei.liu@hxgroup.com
# @Software :PyCharm
-------------------------------------------------
"""
"""
# 组织表
delete from nbp_organization where name like 'performance_org%';
select count(*) from nbp_organization where name like 'performance_org%';

# toC用户表
DELETE FROM nbp_customer where name LIKE 'performance_test%';
DELETE FROM nbp_customer_profile where email LIKE 'performance_test%';

# 电站表
select count(*) from scada_power_station;
DELETE FROM scada_power_station where name LIKE 'performance_power%';
select count(*) from scada_power_station where customer in (select customer from scada_power_station GROUP BY customer HAVING COUNT(customer)>1);

# sn号设备表
select count(*) from scada_sn_type;
delete from scada_sn_type where inverter_sn like 'performance_sn%';.
select count(*) from scada_sn_type;

# 电站下的设备表
select count(*) from scada_energy_storage;
delete from scada_energy_storage where name like 'performance_sn%';
select count(*) from scada_energy_storage;
"""
