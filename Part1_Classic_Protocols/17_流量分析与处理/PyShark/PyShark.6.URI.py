#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import pyshark

pkt_list = []

cap = pyshark.FileCapture('dos.pcap', keep_packets=False, display_filter='http')

url_dict = {}


def print_highest_layer(pkt):
    try:
        host_list = pkt.http.host.split('.')
        if len(host_list[-1]) == 2:  # 如果最后一段只有两位,例如'cn','us'!我们就取后三个部分,例如sina.com.cn
            host = host_list[-3] + '.' + host_list[-2] + '.' + host_list[-1]
        elif len(host_list[-1]) == 3:  # 如果最后一段只有三位,例如'com','net'!我们就取后两个部分,例如sina.com
            host = host_list[-2] + '.' + host_list[-1]
        else:
            next

        # 字典数据结构如下
        # 键为method和host, 值为数量
        counts = url_dict.get((pkt.http.request_method, host), 0)
        counts += 1
        url_dict[(pkt.http.request_method, host)] = counts
    except:
        pass


# 应用函数到数据包
cap.apply_on_packets(print_highest_layer)


if __name__ == '__main__':
    # 使用matplot进行图形化展示
    import matplotlib.pyplot as plt

    url = []
    hits = []
    for x,y in url_dict.items():
        url.append(x[1])
        hits.append(y)

    plt.barh(url, hits, height=0.5)

    ###########################添加注释###################################
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文
    plt.title('站点访问量统计')  # 主题
    plt.xlabel('访问数量')  # X轴注释
    plt.ylabel('站点')  # Y轴注释
    ###########################添加注释###################################

    plt.show()
