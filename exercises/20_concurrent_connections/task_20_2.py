# -*- coding: utf-8 -*-
"""
Задание 20.2

Создать функцию send_show_command_to_devices, которая отправляет
одну и ту же команду show на разные устройства в параллельных потоках,
а затем записывает вывод команд в файл.

Параметры функции:
* devices - список словарей с параметрами подключения к устройствам
* command - команда
* filename - имя файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в файл в таком формате (перед выводом команды надо написать имя хоста и саму команду):

R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.2   YES NVRAM  up                    up
Ethernet0/1                10.1.1.1        YES NVRAM  administratively down down
R3#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down

Для выполнения задания можно создавать любые дополнительные функции.

Проверить работу функции на устройствах из файла devices.yaml
"""
import subprocess
from pprint import pprint
from concurrent.futures import ThreadPoolExecutor
from itertools import repeat
import logging
import netmiko
import yaml

logging.getLogger("paramiko").setLevel(logging.WARNING)

def send_show_command_to_devices(devices,command,filename,limit=3):
    finish_list = []
    with ThreadPoolExecutor(max_workers=limit) as executor:
        result = executor.map(show_command, devices, repeat(command))
        with open(filename, 'w') as f:
            for device, output in result:
                header = device+command
                f.write(header + '\n')
                f.write(output + '\n')


def show_command(devices, command):
    logging.basicConfig(
            format = '%(threadName)s %(name)s %(levelname)s: %(message)s',
            level=logging.INFO)
    with netmiko.ConnectHandler(**devices) as ssh:
        ssh.enable()
        device = ssh.find_prompt()
#        logging.info(device)
        result = ssh.send_command(command)
    return device,result


if __name__ == '__main__':
     with open('devices.yaml') as f:
         devices = yaml.safe_load(f)
     send_show_command_to_devices(devices, 'sh ip int br', 'test.txt')

# Все отлично

# вариант решения

from itertools import repeat
from concurrent.futures import ThreadPoolExecutor

from netmiko import ConnectHandler
import yaml


def send_show_command(device, command):
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
        prompt = ssh.find_prompt()
    return f"{prompt}{command}\n{result}\n"


def send_show_command_to_devices(devices, command, filename, limit=3):
    with ThreadPoolExecutor(max_workers=limit) as executor:
        results = executor.map(send_show_command, devices, repeat(command))
        with open(filename, "w") as f:
            for output in results:
                f.write(output)


if __name__ == "__main__":
    command = "sh ip int br"
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    send_show_command_to_devices(devices, command, "result.txt")
