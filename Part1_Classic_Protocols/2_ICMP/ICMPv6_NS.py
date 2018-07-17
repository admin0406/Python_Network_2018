#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

# IPv6参考文档
# https://www.idsv6.de/Downloads/IPv6PacketCreationWithScapy.pdf
# https://www.ernw.de/download/Advanced%20Attack%20Techniques%20against%20IPv6%20Networks-final.pdf

import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)  # 清除报错
from scapy.all import *
from Tools.GET_MAC_netifaces import get_mac_address
from Tools.IPv6_IP_TO_MAC import Solicited_node_multicast_address


# Windows 查看IPv6邻居 netsh int ipv6 show neigh
# IOS     查看IPv6邻居 show ipv6 neighbors
# Linux   查看IPv6邻居 ip -6 neigh                 | ping6 2001:1::200

def icmpv6_ns(host, ifname):
    ll_mac = get_mac_address(ifname)
    packet = IPv6(dst=Solicited_node_multicast_address(host)) / ICMPv6ND_NS(tgt=host) / ICMPv6NDOptSrcLLAddr(
        lladdr=ll_mac)
    result = sr1(packet, timeout=2, verbose=False)
    return result.getlayer("ICMPv6 Neighbor Discovery Option - Destination Link-Layer Address").fields['lladdr']


if __name__ == '__main__':
    print(icmpv6_ns("2001:1::253", 'ens33'))
