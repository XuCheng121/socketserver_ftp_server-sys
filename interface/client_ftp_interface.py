# Author: Mr.Xu
# @Time : 2019/9/9 20:46
import os
from conf import settings
from lib import common

# 客户端下载接口
def Client_download_interface(soc):
    # 先拿可下载的内容信息
    msg = common.common_tcp_recv_data_interface(soc)
    print(msg)

    # 输入下载文件名
    file_name = input("请输入需要下载的文件")
    flag = common.common_tcp_send_data_interface(soc,file_name)
    if not flag:
        return False

    # 接收文件(文件名，接收目录)
    flag = common.common_tcp_recv_data_interface(soc, file_name=file_name, recv_dir=settings.CLIENT_FILE_DIR)
    if not isinstance(flag,str):
        msg = common.common_tcp_recv_data_interface(soc)
        print(msg)
        return True
    else:
        # 上传失败
        print(flag)
        return False

# 客户端上传接口
def Client_Upload_interface(soc):
    print("目录文件：",os.listdir(settings.CLIENT_FILE_DIR))
    # 输入下载文件名
    file_name = input("请输入需要上传的文件")
    flag = common.common_tcp_send_data_interface(soc, file_name)
    if not flag:
        return False

    # 上传文件(文件名，接收目录)
    flag = common.common_tcp_send_data_interface(soc, file_name=file_name, send_dir=settings.CLIENT_FILE_DIR)
    if flag:
        # 成功上传，接收消息
        msg = common.common_tcp_recv_data_interface(soc)
        print(msg)
        return True
    else:
        # 发送错误信息
        common.common_tcp_send_data_interface(soc,"输入错误，文件不存在")
        msg = common.common_tcp_recv_data_interface(soc)
        print(msg)
        return False




