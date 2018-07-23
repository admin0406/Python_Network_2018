#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a


import pyshark


pkt_list = []

# 分析现象级数据包,"tcp重传的数据包"
cap = pyshark.FileCapture('dos.pcap', keep_packets=False, display_filter='tcp.analysis.retransmission')


def print_highest_layer(pkt):
    # 通过过滤得到数据包清单
    pkt_list.append(pkt)


cap.apply_on_packets(print_highest_layer)

# pretty_print TCP重传的数据包
for x in pkt_list:
    print('='*80)
    x.pretty_print()