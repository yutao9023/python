#!/usr/bin/env python
# -*-coding:utf-8-*-

# 第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
# 使用 Python 如何生成 200 个激活码（或者优惠券）？
import random,string

def gen_code(num):
    code = []
    base_str = string.ascii_letters + string.digits
    for i in range(200):
        single_code = ''.join([random.choice(base_str) for _ in range(num)])
        code.append(single_code)
    for j in code:
        print(j)

if __name__ == '__main__':
    gen_code(20)
