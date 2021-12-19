from multiprocessing import Process, Pool
from 性能测试框架.lib.test_api import TestApi
from 性能测试框架.lib.get_all_testdata import GetRequestData
from 性能测试框架.lib.out_log import OutLog

process_list = []
test_data = GetRequestData.get_request_data()
logger = OutLog().out_log()
work_func = TestApi().work

logger.info('开始创建进程')
for i in range(1000):
    p = Process(target=work_func, name='Process'+str(i), args=(test_data,))
    p.start()
    logger.info(f'正在启动进程{p.name}, 进程ID{p.pid}')
    process_list.append(p)

for j in process_list:
    logger.info('阻塞主进程，使其等待子进程')
    j.join()

logger.info('任务结束，主进程关闭')


