#!/usr/local/bin/python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于教主VIP课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com


import struct
import optparse


def Change_IP_To_Bytes(IP):
    section1 = int(IP.split('.')[0])
    section2 = int(IP.split('.')[1])
    section3 = int(IP.split('.')[2])
    section4 = int(IP.split('.')[3])
    Bytes_IP = struct.pack('>4B', section1, section2, section3, section4)
    return Bytes_IP


if __name__ == "__main__":
    parser = optparse.OptionParser('用法：\n python3 Change_IP_To_Bytes.py --ip IP地址')
    parser.add_option('--ip', dest='ip', type='string', help='IP地址')
    (options, args) = parser.parse_args()
    ip = options.ip
    if ip == None:
        print(parser.usage)
    else:
        print(Change_IP_To_Bytes(ip))
