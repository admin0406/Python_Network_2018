#!/usr/local/bin/python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于教主VIP课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com


from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()

# varBindTable是个list，元素的个数可能有好多个。它的元素也是list，这个list里的元素是ObjectType，个数只有1个。
errorIndication, errorStatus, errorindex, varBindTable = cmdGen.nextCmd(
    cmdgen.CommunityData('qytangro'),  # 设置community
    cmdgen.UdpTransportTarget(('10.1.1.253', 161)),  # 设置IP地址和端口号
    '1.3.6.1.2.1.2.2.1.2',  # 设置OID
)

if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (
        errorStatus.,
        errorindex and varBinds[int(errorindex) - 1][0] or '?'
    )
          )

for varBindTableRow in varBindTable:
    for item in varBindTableRow:
        print(item)
