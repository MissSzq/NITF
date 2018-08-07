import os
import pymysql


API_URL = 'http://hn2.api.okayapi.com/'

# 路径配置
BASE_PATH = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))
# excel测试用例存放位置
CASE_PATH = os.path.join(BASE_PATH, 'data')
# unittest测试用例文件存放位置
TEST_PATH = os.path.join(BASE_PATH, 'testcases')
# 测试报告路径
REPORT_PATH = os.path.join(BASE_PATH, 'report')

# 测试时自动查找excel用例文件的通配符
FILE_NAME = ''

# 服务相关配置
APP_KEY = 'Nemo\'s Interface Test Framework'
APP_SECRET = 'Nemo\'s Interface Test Framework'

# 数据库配置
# SQL_CONFIG = {
#     'host': '127.0.0.1',
#     'port': 3306,
#     'user': 'root',
#     'password': 'root',
#     'db': 'ecshop',
#     'charset': 'utf8mb4',
#     'cursorclass': pymysql.cursors.DictCursor  # 加上这个参数会将查询结果变为[{"字段名":"字段值",...},{}]的形式
# }
SQL_CONFIG = 'D:\PythonProject\Demo\myflask\db.db'
