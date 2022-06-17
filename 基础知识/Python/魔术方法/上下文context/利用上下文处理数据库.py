"""
通过自定义上下文类，来实现上下文管理数据库
"""
import pymysql


class Database(object):
    def __init__(self):
        self.db = pymysql.connect("localhost", "root", "root", "test")
        self.cursor = self.db.cursor()

    def query(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        return result

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.db.close()


def main():
    sql = "SELECT password FROM USER WHERE username='{}' ORDER BY 1;".format('admin')
    with Database() as s:
        a = s.query(sql)
        print(a)


if __name__ == "__main__":
    main()

"""
通过contextlib模块来构造上下文管理器，进行处理数据库
"""

from contextlib import contextmanager

class Database(object):
    def __init__(self):
        self.db = pymysql.connect("localhost", "root", "root", "test")
        self.cursor = self.db.cursor()

    def query(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        return result


@contextmanager
def database_query():
    q = Database()
    yield q


def main():
    sql = "SELECT password FROM USER WHERE username='{}' ORDER BY 1;".format('admin')
    with database_query() as s:
        a = s.query(sql)
        print(a)


if __name__ == "__main__":
    main()