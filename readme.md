

# 基于socketserver模块实现ftp服务器项目

版本: version 0.1

* **客户端**
* **服务端**

## 简介:

1. 基于TCP协议，同时支持多用户同时 **上传** 和 **下载 **操作，实现ftp服务器
2. 上传内容均使用md5进行内容校验。上传文件内容相同则会极速上传成功
3. 上传内容均通过json文件保存文件内容的md5值，作为上传文件内容信息记录

* conf目录：项目配置
* core目录：用户视图层源码
* db目录：该目录存放用户 上传和下载的文件
* interface目录：接口处源码，对接用户视图层，主要处理项目业务逻辑
* lib目录：通用接口
* server_start.py文件：FTP服务端入口
* client_start.py文件：FTP客户端入口