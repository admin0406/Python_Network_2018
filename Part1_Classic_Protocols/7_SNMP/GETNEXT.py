#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a


from pysnmp.entity.rfc3413.oneliner import cmdgen


def snmpv2_getnext(ip, community, oid, port=161):
    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorindex, varBindTable = cmdGen.nextCmd(
        cmdgen.CommunityData(community),  # 设置community
        cmdgen.UdpTransportTarget((ip, port)),  # 设置IP地址和端口号
        oid,  # 设置OID
    )
    # 错误处理
    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (
            errorStatus.prettyPrint(),
            errorindex and varBinds[int(errorindex) - 1][0] or '?'
        )
              )

    result = []
    # varBindTable是个list，元素的个数可能有好多个。它的元素也是list，这个list里的元素是ObjectType，个数只有1个。
    for varBindTableRow in varBindTable:
        for item in varBindTableRow:
            result.append((item.prettyPrint().split("=")[0].strip(), item.prettyPrint().split("=")[1].strip()))
    return result


if __name__ == "__main__":
    # 使用Linux解释器 & WIN解释器
    print(snmpv2_getnext("10.1.1.253", "tcpipro", "1.3.6.1.2.1.2.2.1.2", port=161))
    for x, y in snmpv2_getnext("10.1.1.253", "tcpipro", "1.3.6.1.2.1.2.2.1.2", port=161):
        print(x, y)