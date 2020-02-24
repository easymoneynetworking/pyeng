# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

import subprocess
from pprint import pprint

def ping_ip_addresses(ip_address):
        """
        Ping IP address and return tuple:
        On success:
        * True
        * command output (stdout)
        On failure:
        * False
        * error output (stderr)
        """
        get_reach = []
        get_unreach = []
        for ip_li in ip_address:
            if ip_li[0].isdigit():
                reply = subprocess.run(['ping', '-c', '1', '-n', ip_li],
                                      stdout=subprocess.DEVNULL)
                if reply.returncode == 0:
                    get_reach.append(ip_li)
                else:
                    get_unreach.append(ip_li)
        return get_reach,get_unreach

if __name__ == '__main__':
    lists_ip = ["1.1.1", "8.8.8.8", "8.8.4.4", "8.8.7.1"]
    print(ping_ip_addresses(lists_ip))
