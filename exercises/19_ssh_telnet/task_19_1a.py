# -*- coding: utf-8 -*-
"""
Задание 19.1a

Скопировать функцию send_show_command из задания 19.1 и переделать ее таким образом,
чтобы обрабатывалось исключение, которое генерируется
при ошибке аутентификации на устройстве.

При возникновении ошибки, на стандартный поток вывода должно выводиться сообщение исключения.

Для проверки измените пароль на устройстве или в файле devices.yaml.
"""

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
#            print(f"{device['ip']} \n{result}")
    except:
        return print('Authentication failure: unable to connect')

if __name__ == "__main__":
    command = "sh ip int br"
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        pprint(send_show_command(dev,command))

