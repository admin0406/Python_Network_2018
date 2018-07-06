#!/usr/local/bin/python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于教主VIP课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com


from minimumTFTP.minimumTFTP import Client


def qyt_ftpclient(server, filedir, file, operation=1):
    tftpClient = Client(server, filedir, file)
    if operation == 1:
        tftpClient.get()
    if operation == 2:
        tftpClient.put()
    print()


if __name__ == '__main__':
    # 使用Linux解释器
    # 正常安装有问题,需要把minimumTFTP.py文件放入如下的路径
    # /usr/local/lib/python3.6/site-packages/minimumTFTP/minimumTFTP.py
    qyt_ftpclient('10.1.1.80', '.', 'testupload.txt', operation=1)
    # qyt_ftpclient('10.1.1.80', '.', 'testupload.txt', operation=2)
