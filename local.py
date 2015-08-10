# -*- coding: utf-8 -*-
a = 1
b = "123"
c = 'abc'
d = [a,b,c]
local_dic = locals()
print local_dic['a']
print local_dic['b']
print local_dic['c']
print local_dic['d']