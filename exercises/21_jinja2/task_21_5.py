# -*- coding: utf-8 -*-
"""
Задание 21.5

Создать шаблоны templates/gre_ipsec_vpn_1.txt и templates/gre_ipsec_vpn_2.txt,
которые генерируют конфигурацию IPsec over GRE между двумя маршрутизаторами.

Шаблон templates/gre_ipsec_vpn_1.txt создает конфигурацию для одной стороны туннеля,
а templates/gre_ipsec_vpn_2.txt - для второй.

Примеры итоговой конфигурации, которая должна создаваться на основе шаблонов в файлах:
cisco_vpn_1.txt и cisco_vpn_2.txt.

Шаблоны надо создавать вручную, скопировав части конфига в соответствующие шаблоны.

Создать функцию create_vpn_config, которая использует эти шаблоны для генерации конфигурации VPN на основе данных в словаре data.

Параметры функции:
* template1 - имя файла с шаблоном, который создает конфигурацию для одной строны туннеля
* template2 - имя файла с шаблоном, который создает конфигурацию для второй строны туннеля
* data_dict - словарь со значениями, которые надо подставить в шаблоны

Функция должна возвращать кортеж с двумя конфигурациямя (строки), которые получены на основе шаблонов.

Примеры конфигураций VPN, которые должна возвращать функция create_vpn_config в файлах
cisco_vpn_1.txt и cisco_vpn_2.txt.
"""
from jinja2 import Environment, FileSystemLoader
import yaml
from pprint import pprint
import os

def create_vpn_config(template1, template2, data_dict):
    to_yaml = {'data': data_dict}
    with open('data_files/gres.yml', 'w') as fi:
        yaml.dump(to_yaml, fi)

    with open('data_files/gres.yml') as f:
        data = yaml.safe_load(f)

    templ_dir1, templ_file1 = os.path.split(template1)
    templ_dir2, templ_file2 = os.path.split(template2)
    env = Environment(
        loader=FileSystemLoader(templ_dir1), trim_blocks=True, lstrip_blocks=True
    )
    template1 = env.get_template(templ_file1)
    template2 = env.get_template(templ_file2)
    str_template1 = template1.render(data)
    str_template2 = template2.render(data)
    return str_template1, str_template2

if __name__ == '__main__':
    data = {
        "tun_num": 17,
        "wan_ip_1": "80.241.1.1",
        "wan_ip_2": "90.18.10.2",
        "tun_ip_1": "10.255.1.1 255.255.255.252",
        "tun_ip_2": "10.255.1.2 255.255.255.252",
    }
    template_file1 = 'templates/gre_ipsec_vpn_1.txt'
    template_file2 = 'templates/gre_ipsec_vpn_2.txt'
    pprint(create_vpn_config(template_file1,template_file2,data))
