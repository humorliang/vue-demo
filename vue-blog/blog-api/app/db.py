# 数据库操作类
# 导入数据驱动
import pymysql
# 导入数据连接池
from DBUtils.PooledDB import PooledDB


# pymsql 获取数据操作
# fetchall()
# Fetch all the rows
#
# fetchmany(size=None)
# Fetch several rows
#
# fetchone()
# Fetch the next row


# 创建数据库操作类
class MysqlOption(object):
    '''
    数据库操作：
    __init__:初始化操作连接数据库
        db ：数据连接池对象
    '''

    def __init__(self):
        self.db = PooledDB(
            pymysql,
            10,
            # 以下是传给数据驱动的参数
            host="127.0.0.1",
            port=3306,
            user="root",
            password="123456",
            db="blog",
            charset='utf8'  # 一定要设置编码不然中文sql会出问题
        )

    def select(self, sql):
        # 数据库连接
        dbcon = self.db.connection()
        result = ''
        try:
            # 获取游标
            dbcur = dbcon.cursor()
            # dbcur.execute(sql) 执行sql语句 返回影响的行数 结果为int
            row_num = dbcur.execute(sql)
            if row_num != 0:
                result = dbcur.fetchall()
            else:
                result = None
        except Exception as err:
            print(err)
        finally:
            # 关闭连接
            dbcon.close()
        return result

    def insert(self, sql):
        dbcon = self.db.connection()
        dbcur = dbcon.cursor()
        try:
            # 游标执行查询语句
            dbcur.execute(sql)
            # 提交到数据库
            dbcon.commit()
        except Exception as err:
            print(err)
            # 数据库回滚
            dbcon.rollback()
        finally:
            dbcon.close()

    def update(self, sql):
        dbcon = self.db.connection()
        dbcur = dbcon.cursor()
        try:
            dbcur.execute(sql)
            dbcon.commit()
        except Exception as err:
            print(err)
            dbcon.rollback()
        finally:
            dbcon.close()

    def delete(self, sql):
        dbcon = self.db.connection()
        dbcur = dbcon.cursor()
        try:
            dbcur.execute(sql)
            dbcon.commit()
        except Exception as err:
            print(err)
            dbcon.rollback()
        finally:
            dbcon.close()


if __name__ == "__main__":
    mysql_ = MysqlOption()
    sql = "select post.id,post.title,post.publish_date,post.desc_info,post.content" \
          " from post inner join kind on post.kind_id=kind.id and kind.name='c++'"
    res = mysql_.select(sql)
    print(res)
