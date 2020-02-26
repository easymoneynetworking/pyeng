# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список, где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список IP-адресов и/или диапазонов IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последний октет адреса.

Функция возвращает список IP-адресов.


Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""
from pprint import pprint
import ipaddress

def convert_ranges_to_ip_list(ip_address):
    """
    Ping IP address and return tuple:
    On success:
    * True
    * command output (stdout)
    On failure:
    * False
    * error output (stderr)
    """
    ip_lists = []
    for ip_li in ip_address:
        if '-' not in ip_li:
            ip_lists.append(ip_li)
        if '-' in ip_li:
            command_list = ip_li.split('-')
            if len(command_list[1]) == 1:
                first_list = command_list[0].split('.')
                first_ipadd = ipaddress.ip_address(command_list[0])
                ip_lists.append(command_list[0])
                diapazon2 = int(command_list[1])
                diapazon1 = int(first_list[3])
                for i in range(diapazon1,diapazon2 ):
                    fist_lis = first_ipadd + i
                    ip_lists.append(str(fist_lis))
            else:
                ip_lists.append(command_list[0])
                list1_for_minus = command_list[1].split('.') 
                chetvertiy_oktet_odin = int(list1_for_minus[3])
                list2_for_minus = command_list[0].split('.')
                chetvertiy_oktet_dva = int(list2_for_minus[3])
                first_ipadd2 = ipaddress.ip_address(command_list[0])
                minus = int(chetvertiy_oktet_odin) - int(chetvertiy_oktet_dva)
                minus2 = minus + 1
                for f in range(1, minus2):
                    first_list_add = first_ipadd2 + f
                    ip_lists.append(str(first_list_add))
    return ip_lists

if __name__ == '__main__':
    lists_ip = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
    print(convert_ranges_to_ip_list(lists_ip))
