#!/usr/bin/env python
# -*-coding:utf-8-*-

# �� 0001 �⣺��Ϊ Apple Store App ���������ߣ���Ҫ����ʱ������Ϊ���Ӧ�����ɼ����루�����Ż�ȯ����
# ʹ�� Python ������� 200 �������루�����Ż�ȯ����
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
