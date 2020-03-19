# -*- coding: utf-8 -*-
"""
Задание 17.1

Создать функцию write_dhcp_snooping_to_csv, которая обрабатывает
вывод команды show dhcp snooping binding из разных файлов и записывает обработанные данные в csv файл.

Аргументы функции:
* filenames - список с именами файлов с выводом show dhcp snooping binding
* output - имя файла в формате csv, в который будет записан результат

Функция ничего не возвращает.

Например, если как аргумент был передан список с одним файлом sw3_dhcp_snooping.txt:
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
00:E9:BC:3F:A6:50   100.1.1.6        76260       dhcp-snooping   3    FastEthernet0/20
00:E9:22:11:A6:50   100.1.1.7        76260       dhcp-snooping   3    FastEthernet0/21
Total number of bindings: 2

В итоговом csv файле должно быть такое содержимое:
switch,mac,ip,vlan,interface
sw3,00:E9:BC:3F:A6:50,100.1.1.6,3,FastEthernet0/20
sw3,00:E9:22:11:A6:50,100.1.1.7,3,FastEthernet0/21


Проверить работу функции на содержимом файлов sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt.
Первый столбец в csv файле имя коммутатора надо получить из имени файла, остальные - из содержимого в файлах.

"""

import re
from pprint import pprint
import csv
import glob

dhcp_snoop_files = glob.glob("*_dhcp_snooping.txt")
#pprint(dhcp_snoop_files)

def write_dhcp_snooping_to_csv(filenames,output):
    finish_list = []
    headers = ['switch','mac','ip','vlan','interface']
    switch_regex = r'(?P<device>sw\d+)\S+'
    attribute_regex = (r'(?P<mac>\w+:\w+:\w+:\w+:\w+:\w+) +'
                      r'(?P<ip>\d+[.]\d+[.]\d+[.]\d+) +'
                      r'\w+ +\w+[-]\w+ +(?P<vlan>\d+) +'
                      r'(?P<interface>\w+\d+[/]\d+)')
    finish_list.append(headers)
    for f in filenames:
        switch_match = re.search(switch_regex, f)
        if switch_match:
            hostname = switch_match.group('device')
        with open(f, 'r')as fi:
            all_file = re.finditer(attribute_regex, fi.read())
            for all_files in all_file:
                device = []
                device.append(hostname)
                params = all_files.group('mac', 'ip', 'vlan', 'interface')
                device.extend(params)
                finish_list.append(device)
    with open(output, 'w') as csv_f:
        writer = csv.writer(csv_f)
        for row in finish_list:
            writer.writerow(row)

if __name__ == '__main__':
    (write_dhcp_snooping_to_csv(dhcp_snoop_files,'csv_file'))

# Все отлично, немного изменила

# вариант решения
import csv
import re
import glob


def write_dhcp_snooping_to_csv(filenames, output):
    regex = r"(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)"
    with open(output, "w") as dest:
        writer = csv.writer(dest)
        writer.writerow(["switch", "mac", "ip", "vlan", "interface"])
        for filename in filenames:
            switch = filename.split("_")[0]
            with open(filename) as f:
                for line in f:
                    match = re.search(regex, line)
                    if match:
                        writer.writerow((switch,) + match.groups())


if __name__ == "__main__":
    sh_dhcp_snoop_files = glob.glob("*_dhcp_snooping.txt")
    write_dhcp_snooping_to_csv(sh_dhcp_snoop_files, "example_csv.csv")

