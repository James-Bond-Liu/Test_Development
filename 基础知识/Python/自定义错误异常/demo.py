# 自定义异常类
class AgeError(Exception):

    def __init__(self, age):
        self.__age = age

    # 重写str方法
    def __str__(self):
        return "您传入的年龄不满足需求:age=%d" % self.__age


# 自定义一个类
class Person(object):

    def __init__(self, name, age):
        # 判断年龄
        if 0 < age <= 150:
            self.name = name
            self.age = age
        else:
            # 抛出自定义异常
            raise AgeError(age)

if __name__ == '__main__':
    sample = Person('panda', 4654)
