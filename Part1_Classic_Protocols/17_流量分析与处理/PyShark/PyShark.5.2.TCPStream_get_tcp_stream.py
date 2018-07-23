#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import pyshark


def get_tcp_stream(pcapfile, id):
    # 提取PCAP文件中,特定tcp流ID的数据包
    tcp_stream_pkt_list = []  # 最终返回的特定流ID的数据包清单

    cap = pyshark.FileCapture(pcapfile, keep_packets=False)  # 打开PCAP文件

    for pkt in cap:  # 遍历包
        try:
            if str(pkt.tcp.stream) == str(id):  # 把特定流ID的数据包放入清单
                tcp_stream_pkt_list.append(pkt)
        except:
            pass
    return tcp_stream_pkt_list  # 返回清单


if __name__ == '__main__':
    i = 1
    for pkt in get_tcp_stream('dos.pcap', 10):
        print('='*30, i, '='*30)
        pkt.pretty_print()
        i += 1
