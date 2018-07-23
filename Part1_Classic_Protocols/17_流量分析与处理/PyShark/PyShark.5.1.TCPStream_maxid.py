#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import pyshark


def get_max_id(pcapfile):
    cap = pyshark.FileCapture(pcapfile, keep_packets=False)

    sess_index = []  # 所有的tcp流索引ID清单

    for pkt in cap:
        try:
            sess_index.append(pkt.tcp.stream)  # 把所有的tcp流索引ID放入清单
        except:
            pass

    if len(sess_index) == 0:  # 如果没有任何索引ID就打印错误
        print('No TCP Found')
    else:
        sess_index_int = [int(sid) for sid in sess_index]  # 把索引ID字符串转换为整数,便于排序

    return max(sess_index_int)  # 返回最大的索引ID


if __name__ == '__main__':
    print(get_max_id('dos.pcap'))
