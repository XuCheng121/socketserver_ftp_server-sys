# Author: Mr.Xu
# @Time : 2019/9/9 20:26
import socket
from interface import client_ftp_interface
from conf import settings
from lib import common


def run():
    soc = socket.socket()
    soc.connect((settings.HOST, settings.PORT))

    while 1:
        msg = common.common_tcp_recv_data_interface(soc)
        if not msg:
            print("出错了")
            break
        server_request = input(msg)
        flag = common.common_tcp_send_data_interface(soc,data=server_request)
        if not flag:
            print("出错了")
            break
        # 下载逻辑
        if server_request == "下载":
            client_ftp_interface.Client_download_interface(soc)
        # 上传逻辑
        elif server_request == "上传":
            client_ftp_interface.Client_Upload_interface(soc)
        # 错误逻辑
        else:
            print("输入错误")   # 输入错误直接重新开始


