# coding:utf-8

# 导入运行对象
from app import app
from app import config

# 配置文件
app.config.from_object(config)
if __name__ == '__main__':
    app.run(debug=True)
