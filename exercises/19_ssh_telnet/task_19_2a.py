# -*- coding: utf-8 -*-
"""
Задание 19.2a

Скопировать функцию send_config_commands из задания 19.2 и добавить параметр log,
который контролирует будет ли выводится на стандартный поток вывода
информация о том к какому устройству выполняется подключение.

По умолчанию, результат должен выводиться.

Пример работы функции:

In [13]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...

In [14]: result = send_config_commands(r1, commands, log=False)

In [15]:

Скрипт должен отправлять список команд commands на все устройства из файла devices.yaml с помощью функции send_config_commands.
"""

import yaml
from pprint import pprint
from netmiko import ConnectHandler
from netmiko import Netmiko

#commands = ["logging 10.255.255.1", "logging buffered 20010", "no logging console"]

def send_config_commands(device,config_commands, log=True):
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        if log:
             print('Подключаюсь к {}'.format(device['ip']))
        result = ssh.send_config_set(config_commands)
    return result

if __name__ == "__main__":
    commands = ["logging 10.255.255.1", "logging buffered 20010", "no logging console"]
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
        for dev in devices:
            pprint(send_config_commands(dev,commands))

