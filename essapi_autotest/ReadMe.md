            此工程用于实现HESS户用储能系统的接口自动化测

1、框架介绍：conf——配置文件、全局变量数据；data——测试数据；lib——功能实现；log——日志输出；report——测试报告；template——生成HTML测试报告的模板

2、测试数据
    1、测试数据以Excel存储，具体形式：每个服务一个Excel文件，每个接口一个sheet表单
    2、已实现对MySQL数据库的增删改查操作
    3、使用ddt装饰数据驱动测试用例。一次性读取data目录下的所有数据，列表嵌套字典结构，然后驱动接口执行测试用例。
    4、





已经实现自动化的接口：Power Station Ctrller（findAllByCustomer、findAllNew、findOne）
