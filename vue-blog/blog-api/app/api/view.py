from app import app
from app.db import MysqlOption
import json
# 导入  资源管理模块  路由设计模块  参数解析器
from flask_restful import Resource, Api, reqparse
# 解决跨域问题
from flask_cors import CORS

# 将实例导入api中
api = Api(app)

# 设置跨域问题
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# 创建全局使用的数据库连接池对象
db_pool_object = MysqlOption()


# api资源 路由

# 定义一个admin任务获取所有的账号,查询和添加单个账号,
class Admin(Resource):
    def get(self):
        sql = 'select * from admin;'
        res = db_pool_object.select(sql)
        return json.dumps(res)

    def post(self):
        sql = 'insert into admin(username,password) values("test","123");'
        db_pool_object.insert(sql)
        return 'success'

    def delete(self):
        sql = 'delete from admin where username="test"'
        db_pool_object.delete(sql)
        return 'delete'

    def put(self):
        sql = 'update admin set username="test" where username="user"'
        db_pool_object.update(sql)
        return 'update'


# 定义一个分类
class PostKind(Resource):
    def __init__(self):
        # 全局parser是能够简单统一访问flask.request对象里任何变量
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('id', type=int)
        self.parser.add_argument('name', type=str)

    def get(self):
        args = self.parser.parse_args()
        if args.get('name'):
            print(args.get('name'))
            # 条件的单引号不能少
            sql = "select * from kind where name='{}'".format(args.get('name'))
            res = db_pool_object.select(sql)
            if res:
                return "error"
        else:
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


# 设置真正的路由
# api.add_resource(Admin, '/')
api.add_resource(PostKind, '/')
# api.add_resource(PostKind, '/<int:id>')
