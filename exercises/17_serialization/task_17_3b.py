# -*- coding: utf-8 -*-
"""
Задание 17.3b

Создать функцию transform_topology, которая преобразует топологию в формат подходящий для функции draw_topology.

Функция ожидает как аргумент имя файла в формате YAML, в котором хранится топология.

Функция должна считать данные из YAML файла, преобразовать их соответственно, чтобы функция возвращала словарь такого вида:
    {('R4', 'Fa 0/1'): ('R5', 'Fa 0/1'),
     ('R4', 'Fa 0/2'): ('R6', 'Fa 0/0')}

Функция transform_topology должна не только менять формат представления топологии, но и удалять дублирующиеся соединения (их лучше всего видно на схеме, которую генерирует draw_topology).

Проверить работу функции на файле topology.yaml. На основании полученного словаря надо сгенерировать изображение топологии с помощью функции draw_topology.
Не копировать код функции draw_topology.

Результат должен выглядеть так же, как схема в файле task_17_3b_topology.svg

При этом:
* Интерфейсы должны быть записаны с пробелом Fa 0/0
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме
* На схеме не должно быть дублирующихся линков


> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

"""
import re
from pprint import pprint
import yaml
from draw_network_graph import draw_topology

def transform_topology(yml_file):
    dictionary = {}
    finish_dictionary = {}
    with open(yml_file) as f:
        templates = yaml.safe_load(f)
        for k, value in templates.items():
            keys1 = k
            for k2,value2 in value.items():
                keys2 = (keys1,k2)
                for k3,value3 in value2.items():
                    dictionary[keys2] = (k3,value3)
    for k4,value4 in dictionary.items():
        if not dictionary.get(value4) == k4:
            finish_dictionary[k4] = value4
#                pprint(keys2)
    return finish_dictionary

if __name__ == "__main__":
    infiles = 'cdp_neigbors.yml'
    topology = transform_topology(infiles)
    draw_topology(topology)
