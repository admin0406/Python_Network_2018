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
from Tools.GET_MAC import get_mac_address


def icmpv6_rs():
    ll_mac = get_mac_address('ens33')

    base = IPv6(dst='ff02::2')
    router_solicitation = ICMPv6ND_RS()
    src_ll_addr = ICMPv6NDOptSrcLLAddr(lladdr=ll_mac)
    packet = base / router_solicitation / src_ll_addr
    # packet.show()
    result = sr1(packet, timeout=2, verbose=False)
    # result.show()
    print("gwmac: ", result.getlayer("ICMPv6 Neighbor Discovery Option - Source Link-Layer Address").fields['lladdr'])
    print("mtu: ", result.getlayer("ICMPv6 Neighbor Discovery Option - MTU").fields['mtu'])
    print("prefix: ", result.getlayer("ICMPv6 Neighbor Discovery Option - Prefix Information").fields['prefix'])


if __name__ == '__main__':
    icmpv6_rs()
