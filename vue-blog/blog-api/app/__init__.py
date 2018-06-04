# coding:utf-8
from flask import Flask
app = Flask(__name__)

# 在实例创建完之后进行导入
from app.api import view
