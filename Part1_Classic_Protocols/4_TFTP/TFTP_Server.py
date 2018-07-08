#!/usr/local/bin/python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于教主VIP课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com


from Part1_Classic_Protocols.Tools.minimumTFTP import Server


def qyt_tftpserver(dir):
    tftpServer = Server(dir)
    tftpServer.run()


if __name__ == '__main__':
    # 使用Linux解释器
    # /usr/local/lib/python3.6/site-packages/minimumTFTP/minimumTFTP.py
    qyt_tftpserver('./tftpdir')
