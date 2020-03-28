# -*- coding: utf-8 -*-
"""
Задание 20.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.
"""

import subprocess
from pprint import pprint
from concurrent.futures import ThreadPoolExecutor
import logging

def check_avalaibility(ip_address):
        reply = subprocess.run(['ping', '-c', '1', '-n', ip_address],
        stdout=subprocess.DEVNULL)
        if reply.returncode == 0:
            return True
        else:
            return False


def ping_ip_addresses(ip_address,limit=3):
    get_reach = []
    get_unreach = []
    with ThreadPoolExecutor(max_workers=limit) as executor:
        result = executor.map(check_avalaibility, ip_address)
        for code,address in zip(result, ip_address):
            if code:
                get_reach.append(address)
            else:
                get_unreach.append(address)
    return get_reach, get_unreach

if __name__ == '__main__':
    lists_ip = ["1.1.1", "8.8.8.8", "8.8.4.4", "8.8.7.1"]
    pprint(ping_ip_addresses(lists_ip,3))

# Все отлично

