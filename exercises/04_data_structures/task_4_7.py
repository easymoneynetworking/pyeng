# -*- coding: utf-8 -*-
"""
Задание 4.7

Преобразовать MAC-адрес в строке mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

mac = "AAAA:BBBB:CCCC"
tochka1 = ''
tochka2 = ''
net_dvoetochie = (f'AAAA{tochka1}BBBB{tochka2}CCCC')
new = bin(int(net_dvoetochie, 16))
print(new)

