# -*- coding: utf-8 -*-
"""
Задание 19.1b

Скопировать функцию send_show_command из задания 19.1a и переделать ее таким образом,
чтобы обрабатывалось не только исключение, которое генерируется
при ошибке аутентификации на устройстве, но и исключение,
которое генерируется, когда IP-адрес устройства недоступен.

При возникновении ошибки, на стандартный поток вывода должно выводиться сообщение исключения.

Для проверки измените IP-адрес на устройстве или в файле devices.yaml.
"""
from netmiko import ConnectHandler, NetmikoAuthenticationException, NetmikoTimeoutException

import yaml
from pprint import pprint
from netmiko import ConnectHandler
#command = "sh ip int br"

def send_show_command(device,command):
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            result = ssh.send_command(command)
        return result
    except NetmikoAuthenticationException:
        return print('Authentication failure: unable to connect')
    except NetmikoTimeoutException:
        return print('Connection to device timed-out')

if __name__ == "__main__":
    command = "sh ip int br"
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
        for dev in devices:
            pprint(send_show_command(dev,command))


# Все отлично

# вариант решения
import yaml
import sys
from netmiko import (
    ConnectHandler,
    NetMikoAuthenticationException,
    NetMikoTimeoutException,
)


def send_show_command(device, command):
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            result = ssh.send_command(command)
            return result
    except (NetMikoAuthenticationException, NetMikoTimeoutException) as error:
        print(error)


if __name__ == "__main__":
    command = "sh ip int br"
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    r1 = devices[0]
    result = send_show_command(r1, command)
    print(result)
