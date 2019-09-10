# Author: Mr.Xu
# @Time : 2019/9/9 20:54

import os

HOST = "127.0.0.1"
PORT = 8081

PRO_PATH = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(PRO_PATH,"db")
# SEND_DIR = os.path.join(DB_PATH,"Server_file_dir")
SERVER_FILE_DIR = os.path.join(DB_PATH,"Server_file_dir")
# RECV_DIR = os.path.join(DB_PATH,"Client_file_dir")
CLIENT_FILE_DIR = os.path.join(DB_PATH,"Client_file_dir")
JSON_FILE_DIR = os.path.join(DB_PATH,"manage.json")