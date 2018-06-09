from app import app
from app.db import MysqlOption
from flask import render_template
import json
# 导入  资源管理模块  路由设计模块  参数解析器
from flask_restful import Resource, Api, reqparse, request
# 解决跨域问题
from flask_cors import CORS

# 将实例导入api中
api = Api(app)

# 设置跨域问题
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# 创建全局使用的数据库连接池对象
db_pool_object = MysqlOption()


# 功能类
class MysqlDataTool(object):
    """
    sql_row_value_one(tup,pos): 一行字段处理函数
        tup：sql返回结果的元组
        pos: 取row内部值的位置 int
    sql_more_row_select(tup,condition):多行字段条件选区
        tup:sql 返回结果的元组
        condition: 筛选条件
    sql_row_total_select(tup,condition):多行字段条件选取统计
        tup:sql 返回结果的元组
        condition: 筛选条件
    """

    def sql_row_value_one(self, tup, pos):
        # 遍历每一行字段
        try:
            if tup[0][pos]:
                return tup[0][pos]
            else:
                return None
        except Exception as err:
            print(err)
            return None

    def sql_more_row_select(self, tup, condition):
        try:
            for row in range(len(tup)):
                for value in range(len(row)):
                    if value == condition:
                        return row
        except Exception as err:
            print(err)
            return None

    def sql_row_total_select(self, tup, condition):
        cond_num = 0
        try:
            for row in range(len(tup)):
                for value in range(len(row)):
                    if value == condition:
                        cond_num += 1
        except Exception as err:
            print(err)
            return cond_num

    def transferContent(self, content):
        if content is None:
            return None
        else:
            string = ""
            for c in content:
                if c == '"':
                    string += '\\\"'
                elif c == "'":
                    string += "\\\'"
                elif c == "\\":
                    string += "\\\\"
                else:
                    string += c
            return string

# api资源 路由
# 定义一个分类api
class PostKind(Resource):
    def __init__(self):
        # parser是能够简单统一访问flask.request对象里任何变量
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('id', type=int)
        self.parser.add_argument('name', type=str)

    def get(self):
        sql = "select * from kind"
        res = db_pool_object.select(sql)  # ((2, 'python'), (3, 'javascript'))
        res_list = []  # 结果字典
        for item in res:
            dic = {}
            dic['kind_id'] = item[0]
            dic['kind_name'] = item[1]
            dic['post_num'] = 10
            res_list.append(dic)
        return json.dumps(res_list)

    def post(self):
        args = self.parser.parse_args()
        if args.get('name'):
            sql = "insert into kind(name) value ('{}')".format(args.get('name'))
            db_pool_object.insert(sql)

        # print(args.get('name'))

    def delete(self):
        # request请求变量集合
        args = self.parser.parse_args()
        id_ = args.get("id")
        sql = "delete from kind where id={}".format(id_)
        db_pool_object.delete(sql)


# 定义文章api
class Post(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('post_id', type=int)
        self.parser.add_argument('kind_id', type=int)
        self.parser.add_argument('limit', type=int)
        self.parser.add_argument('all', type=int)
        self.parser.add_argument('random_num', type=int)
        self.sql_dispose = MysqlDataTool()

    def get(self):
        # 获取参数
        args = self.parser.parse_args()
        # 根据id获取文章信息
        if args.get('post_id'):
            try:
                sql = 'select title,author,content,publish_date from post where id={}'.format(args.get('post_id'))
                # print(sql)
                res = db_pool_object.select(sql)
                dic = {}
                for item in res:
                    dic['title'] = item[0]
                    dic['author'] = item[1]
                    dic['content'] = item[2]
                    dic['time'] = str(item[3])
                # print(dic)
                return json.dumps(dic)
            except Exception as err:
                print(err)
                return json.dumps({})

        # 根据分类的id获取文章
        elif args.get('kind_id'):
            try:
                sql = "select * from post inner join kind on post.kind_id={} and kind.id={}". \
                    format(args.get('kind_id'), args.get('kind_id'))
                res = db_pool_object.select(sql)
                # print(res)
                res_list = []  # 结果字典
                for item in res:
                    dic = {}
                    dic['id'] = item[0]
                    dic['date'] = str(item[5])  # 日期转换
                    dic['title'] = item[1]
                    dic['kind'] = item[-1]
                    dic['imgUrl'] = item[6]
                    dic['desc'] = item[2]
                    dic['view_num'] = item[4]
                    dic['thumbs'] = item[-5]
                    res_list.append(dic)
                return json.dumps(res_list)
            except Exception as err:
                print(err)
                return json.dumps({})
        # 根据最新时间返回指定个数
        elif args.get('limit'):
            try:
                sql = 'select * from post inner join kind on post.kind_id=kind.id order by post.publish_date desc limit {}'. \
                    format(args.get('limit'))
                res = db_pool_object.select(sql)
                # print(res)
                res_list = []  # 结果字典
                for item in res:
                    dic = {}
                    dic['id'] = item[0]
                    dic['date'] = str(item[5])  # 日期转换
                    dic['title'] = item[1]
                    dic['kind'] = item[-1]
                    dic['imgUrl'] = item[6]
                    dic['desc'] = item[2]
                    dic['view_num'] = item[4]
                    dic['thumbs'] = item[-5]
                    res_list.append(dic)
                return json.dumps(res_list)
            except Exception as err:
                print(err)
                return json.dumps({})
        # 返回所有文章
        elif args.get('all'):
            try:
                sql = 'select * from post inner join kind on post.kind_id=kind.id'
                res = db_pool_object.select(sql)
                print(res)
                res_list = []  # 结果字典
                for item in res:
                    dic = {}
                    dic['id'] = item[0]
                    dic['date'] = str(item[5])  # 日期转换
                    dic['title'] = item[1]
                    dic['kind'] = item[-1]
                    dic['imgUrl'] = item[6]
                    dic['desc'] = item[2]
                    dic['view_num'] = item[4]
                    dic['thumbs'] = item[-5]
                    res_list.append(dic)
                return json.dumps(res_list)
            except Exception as err:
                print(err)
                return json.dumps({})

        # 随机文章
        elif args.get('random_num'):
            try:
                sql = "select id,title from post limit {}".format(args.get('random_num'))
                res = db_pool_object.select(sql)
                # print(res)
                res_list = []
                for item in res:
                    dic = {}
                    dic['post_id'] = item[0]
                    dic['title'] = item[1]
                    res_list.append(dic)
                return json.dumps(res_list)
            except Exception as err:
                print(err)
                return json.dumps({})

        else:
            try:
                sql = 'select * from post inner join kind on post.kind_id=kind.id'
                res = db_pool_object.select(sql)
                res_list = []  # 结果字典
                for item in res:
                    dic = {}
                    dic['id'] = item[0]
                    dic['date'] = str(item[5])  # 日期转换
                    dic['author'] = item[-3]
                    dic['title'] = item[1]
                    dic['kind'] = item[-1]
                    res_list.append(dic)
                return json.dumps(res_list)
            except Exception as err:
                print(err)
                return json.dumps({})

    def post(self):
        # 获取前台传来的json数据
        post_data = request.json
        print(post_data)  # dict类型
        # 查找类名
        try:
            sql_s_kind = "select id from kind where name='{}'".format(post_data.get('kind'))
            kind_name = db_pool_object.select(sql_s_kind)
            # print(self.sql_dispose.sql_row_value_one(kind_name, 0))
            p_title = post_data.get('title')
            p_desc = post_data.get('desc')
            p_author = post_data.get('author')
            p_date = post_data.get('date')
            p_content=self.sql_dispose.transferContent(post_data.get('content'))
            # p_content = post_data.get('content')
            p_kind = self.sql_dispose.sql_row_value_one(kind_name, 0)
            # sql = "insert into post(title,desc_info,content,publish_date,kind_id,author) " \
            #       "value ('{}','{}','{}','{}','{}','{}')".format(p_title, p_desc, p_content,
            #                                                      p_date, p_kind, p_author)
            sql = "insert into post(title,content) VALUE ('%s','%s')" % (p_title, p_content)
            db_pool_object.insert(sql)
        except Exception as err:
            print(err)

    def put(self):
        pass

    def delete(self):
        args = self.parser.parse_args()
        try:
            if args.get('post_id'):
                sql = "delete from post where id={}".format(args.get('post_id'))
                db_pool_object.delete(sql)
        except Exception as err:
            print(err)


# 设置真正的路由
api.add_resource(PostKind, '/api/v_1.0/kind/')
api.add_resource(Post, '/api/v_1.0/post/')
