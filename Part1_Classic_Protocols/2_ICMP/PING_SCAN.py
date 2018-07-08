#!/usr/local/bin/python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于教主VIP课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com


import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
import multiprocessing
from PING_ONE import scapy_ping_one
from scapy.all import *
from Part1_Classic_Protocols.Tools.SORT_IP import sort_ip


def scapy_ping_scan(network):
    net = ipaddress.ip_network(network)
    ip_list = []
    for ip in net:
        ip_list.append(str(ip))  # 把IP地址放入ip_list的清单
    pool = multiprocessing.Pool(processes=100)  # 创建多进程的进程池（并发为100）
    result = pool.map(scapy_ping_one, ip_list)  # 关联函数与参数，并且提取结果到result
    pool.close()  # 关闭pool，不在加入新的进程
    pool.join()  # 等待每一个进程结束
    scan_list = []  # 扫描结果IP地址的清单
    for ip, ok in result:
        if ok == 1:  # 如果范围值为1
            scan_list.append(ip)  # 把IP地址放入scan_list清单里边
    return sort_ip(scan_list)  # 排序并且打印清单


if __name__ == '__main__':
    # 使用Linux解释器
    import time

    t1 = time.time()
    print('活动IP地址如下:')
    for ip in scapy_ping_scan("10.1.1.0/24"):
        print(str(ip))
    t2 = time.time()
    print('本次扫描时间: %.2f' % (t2 - t1))  # 计算并且打印扫描时间
