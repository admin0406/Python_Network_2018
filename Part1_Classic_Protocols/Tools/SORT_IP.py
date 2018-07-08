#!/usr/local/bin/python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于教主VIP课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com


IP_LIST = ['172.16.12.123',
           '172.16.12.3',
           '172.16.12.234',
           '172.16.12.12',
           '172.16.12.23',
           ]


def sort_ip(ips):  # 定义获取MAC地址的模块，传入接口名字
    sorted_ip = []
    sorted_last_section = []
    first_3_section = ips[0].split('.')[0] + '.' + ips[0].split('.')[1] + '.' + ips[0].split('.')[2] + '.'
    for ip in ips:
        sorted_last_section.append(int(ip.split('.')[3]))
    sorted_last_section = sorted(sorted_last_section)
    for i in sorted_last_section:
        sorted_ip.append(first_3_section + str(i))
    return sorted_ip


if __name__ == "__main__":
    print(sort_ip(IP_LIST))
