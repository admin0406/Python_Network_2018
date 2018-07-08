#!/usr/local/bin/python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于教主VIP课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com

import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)  # 清除报错
from scapy.all import *
from Part1_Classic_Protocols.Tools.GET_IP_IFCONFIG import get_ip_address_ifconfig  # 获取本机IP地址
from Part1_Classic_Protocols.Tools.GET_MAC import get_mac_address  # 获取本机MAC地址


def arp_request(ip_address, ifname='ens33'):
    # 获取本机IP地址
    localip = get_ip_address_ifconfig(ifname)['ip_address']
    # 获取本机MAC地址
    localmac = get_mac_address(ifname)
    try:  # 发送ARP请求并等待响应
        result_raw = srp(Ether(src=localmac, dst='FF:FF:FF:FF:FF:FF') /
                         ARP(op=1,
                             hwsrc=localmac, hwdst='00:00:00:00:00:00',
                             psrc=localip, pdst=ip_address),
                         iface=ifname,
                         timeout=1,
                         verbose=False)
        # 把响应的数据包对，产生为清单
        result_list = result_raw[0].res
        # [0]第一组响应数据包
        # [1]接受到的包，[0]为发送的数据包
        # 获取ARP头部字段中的['hwsrc']字段，作为返回值返回
        return ip_address, result_list[0][1].getlayer(ARP).fields['hwsrc']
    except IndexError:
        return ip_address, None


if __name__ == "__main__":
    # 使用Linux解释器
    print(arp_request('10.1.1.254'))
