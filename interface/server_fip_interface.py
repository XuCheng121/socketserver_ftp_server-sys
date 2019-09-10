# Author: Mr.Xu
# @Time : 2019/9/9 20:46
import os
from conf import settings
from lib import common

def Server_download_interface(conn):
    # 先告诉别人我FTP服务器中有哪些文件可被下载
    file_list = os.listdir(settings.SERVER_FILE_DIR)
    resources_data = f"FTP服务器中文件：{file_list}"
    flag = common.common_tcp_send_data_interface(conn,resources_data)
    if not flag:
        return False

    # 拿到要下载的文件名
    file_name = common.common_tcp_recv_data_interface(conn)
    if not file_name:
        return False

    # 发送给别人
    msg = common.common_tcp_send_data_interface(conn, file_name=file_name, send_dir=settings.SERVER_FILE_DIR)
    if msg:
        print(f"客户机成功下载 {file_name}")
        common.common_tcp_send_data_interface(conn, f"{file_name} 下载成功")
        return True
    else:
        common.common_tcp_send_data_interface(conn, f"{file_name} 下载失败")
        return False

def Server_Upload_interface(conn):
    # 接收需要上传的文件名
    file_name = common.common_tcp_recv_data_interface(conn)

    # 接收文件,如果不成功则收到一段话
    flag = common.common_tcp_recv_data_interface(conn, file_name=file_name, recv_dir=settings.SERVER_FILE_DIR)
    if not isinstance(flag,str):
        print(f"客户机成功上传 {file_name}")
        common.common_tcp_send_data_interface(conn, f"{file_name} 上传成功")
        return True
    else:
        common.common_tcp_send_data_interface(conn, f"{file_name} 上传失败")
        return False

