# -*- coding: utf-8 -*-

"""
Задание 26.3a

Изменить класс IPAddress из задания 26.3.

Добавить два строковых представления для экземпляров класса IPAddress.
Как дожны выглядеть строковые представления, надо определить из вывода ниже:

Создание экземпляра
In [5]: ip1 = IPAddress('10.1.1.1/24')

In [6]: str(ip1)
Out[6]: 'IP address 10.1.1.1/24'

In [7]: print(ip1)
IP address 10.1.1.1/24

In [8]: ip1
Out[8]: IPAddress('10.1.1.1/24')

In [9]: ip_list = []

In [10]: ip_list.append(ip1)

In [11]: ip_list
Out[11]: [IPAddress('10.1.1.1/24')]

In [12]: print(ip_list)
[IPAddress('10.1.1.1/24')]

Для этого задания нет теста!
"""
from pprint import pprint


class IPAddress:
    def __init__(self, ip):
        address, mask = ip.split("/")
        self._check_correct_address(address)
        self._check_correct_mask(mask)
        self.ip = address
        self.mask = int(mask)

    def __str__(self):
        return f"IP address {self.ip}/{self.mask}"

    def __repr__(self):
        return f"IP address('{self.ip}/{self.mask}')"

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

ip1 = IPAddress('10.1.26.1/24')
ip_list = []
ip_list.append(ip1)
pprint(ip_list)

# Все отлично

