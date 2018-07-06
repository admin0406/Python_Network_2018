#!/usr/local/bin/python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于教主VIP课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com


from minimumTFTP.minimumTFTP import Server


def qyt_tftpserver(dir):
    tftpServer = Server(dir)
    tftpServer.run()


if __name__ == '__main__':
    # 使用Linux解释器
    # 正常安装有问题,需要把minimumTFTP.py文件放入如下的路径
    # /usr/local/lib/python3.6/site-packages/minimumTFTP/minimumTFTP.py
    qyt_tftpserver('./tftpdir')
