# -*- coding: utf-8 -*-
"""
Задание 21.1

Создать функцию generate_config.

Параметры функции:
* template - путь к файлу с шаблоном (например, "templates/for.txt")
* data_dict - словарь со значениями, которые надо подставить в шаблон

Функция должна возвращать строку с конфигурацией, которая была сгенерирована.

Проверить работу функции на шаблоне templates/for.txt и данных из файла data_files/for.yml.

"""
# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader
import yaml
from pprint import pprint
import os


def generate_config(template,data_dict):
    templ_dir, templ_file = os.path.split(template)
    env = Environment(
        loader=FileSystemLoader(templ_dir), trim_blocks=True, lstrip_blocks=True
            )
    template = env.get_template(templ_file)
    str_template = template.render(data_dict)

    return str_template

if __name__ == '__main__':
    data_file = 'data_files/for.yml'
    template_file = 'templates/for.txt'
    with open(data_file) as f:
        data = yaml.safe_load(f)
    pprint(generate_config(template_file,data))
