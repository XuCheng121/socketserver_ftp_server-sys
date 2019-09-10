# Author: Mr.Xu
# @Time : 2019/9/9 20:47
import struct
import json
import os
import hashlib
from conf import settings

def common_tcp_send_data_interface(conn, data=None, file_name = None, send_dir = None):
    dic = {"data_size": None, "file_md5": None, "file_name": file_name}

    # 如果不是文件
    if data:
        dic["data_size"] = len(data.encode("utf8"))
        dic_byters = (json.dumps(dic)).encode("utf8")
        head = struct.pack("i",len(dic_byters))

        conn.send(head)
        conn.send(dic_byters)
        conn.send(data.encode("utf8"))
        return True
    else:
        file_path = os.path.join(send_dir,file_name)

        if not os.path.exists(file_path):
            return False
        
        # 获取MD5值
        md = hashlib.md5()
        with open(file_path,"rb") as f:
            avg_size = os.path.getsize(file_path)//10 + 1   # 均等10份
            for i in range(0,10):
                md.update(f.read(10))
                f.seek(i*avg_size,0)
        with open(file_path,'rb') as f:
            data = f.read()

        # 放MD5值
        dic["file_md5"] = md.hexdigest()
        # 放文件长度
        dic["data_size"] = os.path.getsize(file_path)

        dic_byters = (json.dumps(dic)).encode("utf8")
        head = struct.pack("i", len(dic_byters))

        conn.send(head)
        conn.send(dic_byters)
        conn.send(data)
        return f"{file_name} 下载成功"

def common_tcp_recv_data_interface(conn,file_name=None,recv_dir=None):
    # 得到头
    head = conn.recv(4)
    # 得到字典长度
    head_dic_len = struct.unpack("i", head)[0]  # 元祖类型
    # 得到字典数据并反序列化
    head_dic_byte = conn.recv(head_dic_len)
    head_dic = json.loads(head_dic_byte)  # json可以直接反序列化bytes类型

    if not head_dic.get("file_name"):
        # 得到数据长度
        data_len = head_dic.get("data_size")
        str_data = ""
        while data_len:
            if data_len > 1024:
                data = conn.recv(1024)  # 你要接收的数据长度必须等于真实接收到的数据长度才可以停止
                str_data += data.decode("utf8")
                data_len -= len(data)
            else:
                data = conn.recv(data_len)
                str_data += data.decode("utf8")
                data_len -= len(data)
        return str_data
    else:

        file_path = os.path.join(recv_dir, file_name)

        # 拿到真正的数据长度
        file_data_len = head_dic.get("data_size")

        data = {}
        if os.path.exists(settings.JSON_FILE_DIR):
            with open(settings.JSON_FILE_DIR, "r") as rf:
                data = json.load(rf)

        with open(settings.JSON_FILE_DIR, "w", ) as wf:
            data[file_name] = head_dic.get("file_md5")
            json.dump(data, wf)

            # 写入数据
            with open(file_path, "wb") as f:
                while file_data_len:
                    if file_data_len > 1024:
                        data_recv = conn.recv(1024)  # 你要接收的数据长度必须等于真实接收到的数据长度才可以停止
                        f.write(data_recv)
                        file_data_len -= len(data_recv)
                    else:
                        data_recv = conn.recv(file_data_len)
                        f.write(data_recv)
                        file_data_len -= len(data_recv)
        return True






