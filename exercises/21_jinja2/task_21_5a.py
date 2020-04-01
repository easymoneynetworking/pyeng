# -*- coding: utf-8 -*-
"""
Задание 21.5a

Создать функцию configure_vpn, которая использует шаблоны из задания 21.5 для настройки VPN на маршрутизаторах на основе данных в словаре data.

Параметры функции:
* src_device_params - словарь с параметрами подключения к устройству
* dst_device_params - словарь с параметрами подключения к устройству
* src_template - имя файла с шаблоном, который создает конфигурацию для одной строны туннеля
* dst_template - имя файла с шаблоном, который создает конфигурацию для второй строны туннеля
* vpn_data_dict - словарь со значениями, которые надо подставить в шаблоны

Функция должна настроить VPN на основе шаблонов и данных на каждом устройстве.
Функция возвращает вывод с набором команд с двух марушртизаторов (вывод, которые возвращает send_config_set).

При этом, в словаре data не указан номер интерфейса Tunnel, который надо использовать.
Номер надо определить самостоятельно на основе информации с оборудования.
Если на маршрутизаторе нет интерфейсов Tunnel, взять номер 0, если есть взять ближайший свободный номер,
но одинаковый для двух маршрутизаторов.

Например, если на маршрутизаторе src такие интерфейсы: Tunnel1, Tunnel4.
А на маршрутизаторе dest такие: Tunnel2, Tunnel3, Tunnel8.
Первый свободный номер одинаковый для двух маршрутизаторов будет 9.
И надо будет настроить интерфейс Tunnel 9.

Для этого задания нет теста!
"""
import logging
import netmiko
from netmiko import ConnectHandler, NetMikoTimeoutException
from concurrent.futures import ThreadPoolExecutor, as_completed
from task_21_5 import create_vpn_config
from pprint import pprint
import yaml
import re
logging.getLogger("paramiko").setLevel(logging.WARNING)


def configure_vpn(src_device_params, dst_device_params, src_template, dst_template, vpn_data_dict):
    """
    Функция для паралельного подключения к двум устройствам.
    Как аргументы передаются разные файлы с командами и
    параметры подключения,поэтому для начало нужно обьединить их.
    """
    ## С помощью функции find_tunnel_number найдем номер тунеля
    ## Заменим значение тунеля в словаре vpn_data_dict
    tunnel_number = find_tunnel_number(src_device_params, dst_device_params)
    vpn_data_dict["tun_num"] = tunnel_number
    ## Применяю функцию из задания 21.5 для генерации шаблонов и распоковываю шаблоны в переменные
    str_template1, str_template2 = create_vpn_config(src_template, dst_template, vpn_data_dict)
    commands = {}
    src_dest_dev = []
    ##Получаю словарь commands  вида {ipаддрес: команды(в виде строк)}
    commands[src_device_params['ip']] = str_template1
    commands[dst_device_params['ip']] = str_template2
    ##Обьединяю два словаря с параметрами подключения
    ##и создаю список из словарей src_dest_dev
    src_dest_dev = [src_device_params]
    src_dest_dev.append(dst_device_params)
    with ThreadPoolExecutor(max_workers=2) as executor:
        future_list = []
        for ddevice in src_dest_dev:
            future = executor.submit(show_command, ddevice, commands[ddevice["ip"]])
            future_list.append(future)
        for f in as_completed(future_list):
            results = f.result()

def find_tunnel_number(src_template, dst_template):
    '''
    Функция для поиска номера тунеля с помощью regex
    Буду использовать функцию max для номера тунеля
    '''
    regex = r'Tunnel(\d+)'
    with ConnectHandler(**src_template) as ssh1:
        ssh1.enable()
        src_result = ssh1.send_command('show ip int br')
        match1 = re.findall(regex, src_result)
        convert_to_digit =  [int(items1) for items1 in match1]
    with ConnectHandler(**dst_template) as ssh2:
        ssh2.enable()
        src_result = ssh2.send_command('show ip int br')
        match2 = re.findall(regex, src_result)
        convert_to_digit2 = [int(items2) for items2 in match2]
    if not match1 and not match2:
        tunnel_number = 0
        return tunnel_number
    else:
        list_digit = convert_to_digit + convert_to_digit2
        tunnel_number = max(list_digit) + 1
        return tunnel_number




def show_command(devices, command):
    '''
    Функция для подключения к устройству и выполнения комманд.
    Возвращает результат выполненных комманд
    '''
#    logging.basicConfig(filename='test.log', level=logging.DEBUG)
#    logger = logging.getLogger("netmiko")
    with netmiko.ConnectHandler(**devices) as ssh:
        ssh.enable()
        result = ssh.send_config_set(command)
        ssh.exit_config_mode()
    return result


if __name__ == '__main__':
    data = {
        "tun_num": None,
        "wan_ip_1": "192.168.100.1",
        "wan_ip_2": "192.168.100.2",
        "tun_ip_1": "10.0.1.1 255.255.255.252",
        "tun_ip_2": "10.0.1.2 255.255.255.252",
    }
    with open('devices1.yml') as f:
        device1 = yaml.safe_load(f)
    with open('devices2.yml') as f:
        device2 = yaml.safe_load(f)
        configure_vpn(device1, device2, 'templates/gre_ipsec_vpn_1.txt', 'templates/gre_ipsec_vpn_2.txt', data)

