#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a


from pysnmp.entity.rfc3413.oneliner import cmdgen
from pysnmp.proto import rfc1902


def snmpv2_set(ip, community, oid, value, port=161):
    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorindex, varBinds = cmdGen.setCmd(
        cmdgen.CommunityData(community),  # 写入Community
        cmdgen.UdpTransportTarget((ip, port)),  # IP地址和端口号
        (oid, rfc1902.OctetString(value))  # OID和写入的内容，需要进行编码！
    )
    # 错误处理
    if errorIndication:
        print("写入错误!!!")
        print(errorIndication)
    elif errorStatus:
        print("写入错误!!!")
        print('%s at %s' % (
            errorStatus.prettyPrint(),
            errorindex and varBinds[int(errorindex) - 1][0] or '?'
        )
              )
    else:
        print("写入成功!!!")
    # 打印回显示结果
    for name, val in varBinds:
        print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))  # 打印修改的结果


if __name__ == "__main__":
    # 使用Linux解释器 & WIN解释器
    snmpv2_set("10.1.1.253", "tcpiprw", "1.3.6.1.2.1.1.5.0", "Python_Net_R1", port=161)