# -*- coding: utf-8 -*-

"""
Задание 26.3

В этом задании необходимо создать класс IPAddress.

При создании экземпляра класса, как аргумент передается IP-адрес и маска,
а также выполняется проверка корректности адреса и маски:
* Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой
   - каждое число в диапазоне от 0 до 255
* маска считается корректной, если это число в диапазоне от 8 до 32 включительно

Если маска или адрес не прошли проверку, необходимо сгенерировать исключение ValueError с соответствующим текстом (смотри вывод ниже).

Также, при создании класса, должны быть созданы два атрибута экземпляра: ip и mask, в которых содержатся адрес и маска, соответственно.

Пример создания экземпляра класса:
In [1]: ip = IPAddress('10.1.1.1/24')

Атрибуты ip и mask
In [2]: ip1 = IPAddress('10.1.1.1/24')

In [3]: ip1.ip
Out[3]: '10.1.1.1'

In [4]: ip1.mask
Out[4]: 24

Проверка корректности адреса (traceback сокращен)
In [5]: ip1 = IPAddress('10.1.1/24')
---------------------------------------------------------------------------
...
ValueError: Incorrect IPv4 address

Проверка корректности маски (traceback сокращен)
In [6]: ip1 = IPAddress('10.1.1.1/240')
---------------------------------------------------------------------------
...
ValueError: Incorrect mask

"""
from pprint import pprint
import re

class IPAddress:
    def __init__(self, ip):
        address, mask = ip.split("/")
        self._check_correct_address(address)
        self._check_correct_mask(mask)
        self.ip = address
        self.mask = int(mask)

    def _check_correct_address(self, address):
        octets = address.split(".")
        correct_ip = True
        if len(octets) != 4:
            correct_ip = False
        else:
            for octet in octets:
                if not (octet.isdigit() and int(octet) in range(256)):
                    correct_ip = False
                    break
        if not correct_ip:
            raise ValueError('Incorrect IPv4 address')

    def _check_correct_mask(self, mask):
        if not int(mask) in range(8,33):
            raise ValueError('Incorrect mask')

#    def ip(self, ip):
#        return self.ip

#    def mask(self, mask):
#        masks = int(mask)
#        return masks



#ip = IPAddress('10.1.26.1/24')
ip1 = IPAddress('10.1.26.1/24')
pprint(ip1.mask)
