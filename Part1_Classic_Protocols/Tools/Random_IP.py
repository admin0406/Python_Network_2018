#!/usr/local/bin/python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于教主VIP课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com


import random


def Random_Section():
    section = random.randint(1, 254)
    return section


def Random_IP():
    IP = str(Random_Section()) + '.' + str(Random_Section()) + '.' + str(Random_Section()) + '.' + str(Random_Section())
    return IP


if __name__ == '__main__':
    print(Random_IP())
