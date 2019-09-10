# Author: Mr.Xu
# @Time : 2019/9/9 20:27
import socketserver
from interface import server_fip_interface
from conf import settings
from lib import common

class MyTCP(socketserver.BaseRequestHandler):
    def handle(self):
        print(f"主机{self.client_address}连接成功,欢迎使用FTP服务器。。。")
        while 1:
            try:
                msg = "请问你需要上传还是下载."
                # 发数据
                common.common_tcp_send_data_interface(self.request,msg)
                # 收数据
                client_request = common.common_tcp_recv_data_interface(self.request)
                print(msg)

                # 根据请求进行判断
                if client_request == "下载":
                    # 发文件给客户机
                    server_fip_interface.Server_download_interface(self.request)
                elif client_request == "上传":
                    # 接收文件到服务器
                    server_fip_interface.Server_Upload_interface(self.request)
                else:
                    # 客户端输入错误，直接重新开始
                    continue
                    # common.common_tcp_send_data_interface(self.request,"输入错误")

            except:
                print("与客户机连接中断。。。\n")
                break

def run():
    server = socketserver.ThreadingTCPServer((settings.HOST, settings.PORT), MyTCP)
    # 一直在等待发送数据来
    server.serve_forever()