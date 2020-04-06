# -*- coding: utf-8 -*-
"""
Задание 22.5

Создать функцию send_and_parse_command_parallel.

Функция send_and_parse_command_parallel должна запускать в параллельных потоках функцию send_and_parse_show_command из задания 22.4.

В этом задании надо самостоятельно решить:
* какие параметры будут у функции
* что она будет возвращать


Теста для этого задания нет.
"""

import yaml
from pprint import pprint
from itertools import repeat
from concurrent.futures import ThreadPoolExecutor
from task_22_4 import send_and_parse_show_command

def send_and_parse_command_parallel(devices, command, templates_path):
    with ThreadPoolExecutor(max_workers=2) as executor:
        result = executor.map(send_and_parse_show_command, devices, templates_path, repeat(command))
        return resul


if __name__ == "__main__":
    command = "sh ip int br"
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
        for dev in devices:
            pprint(send_and_parse_show_command(dev, command, 'templates'))

# Все отлично

# вариант решения

from task_22_4 import send_and_parse_show_command
from concurrent.futures import ThreadPoolExecutor, as_completed
from pprint import pprint
import os
import yaml


def send_and_parse_command_parallel(devices, command, path, limit=3):
    with ThreadPoolExecutor(max_workers=limit) as executor:
        result_all = [
            executor.submit(send_and_parse_show_command, device, command, path)
            for device in devices
        ]
        output = [f.result() for f in as_completed(result_all)]
    return output


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    command = "sh ip int br"
    path_dir = f"{os.getcwd()}/templates"
    pprint(send_and_parse_command_parallel(devices, command, path_dir))
