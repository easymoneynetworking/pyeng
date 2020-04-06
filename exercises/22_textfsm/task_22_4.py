# -*- coding: utf-8 -*-
"""
Задание 22.4

Создать функцию send_and_parse_show_command.

Параметры функции:
* device_dict - словарь с параметрами подключения к одному устройству
* command - команда, которую надо выполнить
* templates_path - путь к каталогу с шаблонами TextFSM
* index - имя индекс файла, значение по умолчанию "index"

Функция должна подключаться к одному устройству, отправлять команду show с помощью netmiko,
а затем парсить вывод команды с помощью TextFSM.

Функция должна возвращать список словарей с результатами обработки вывода команды (как в задании 22.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br и устройствах из devices.yaml.
"""
import yaml
from pprint import pprint
from netmiko import ConnectHandler
import clitable

def send_and_parse_show_command(device_dict, command, templates_path, index='index'):
    finish_dic = {}
    attributes = {'Command': command , 'Vendor': 'cisco_ios'}
    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
        cli_table = clitable.CliTable(index, templates_path)
        cli_table.ParseCmd(result, attributes)
        return [dict(zip(cli_table.header, item)) for item in cli_table]

if __name__ == "__main__":
    command = "sh ip int br"
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
        pprint(send_and_parse_show_command(devices[0], command, 'templates', 'index'))

