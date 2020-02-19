# -*- coding: utf-8 -*-
"""
Задание 11.2

Создать функцию create_network_map, которая обрабатывает
вывод команды show cdp neighbors из нескольких файлов и объединяет его в одну общую топологию.

У функции должен быть один параметр filenames, который ожидает как аргумент список с именами файлов, в которых находится вывод команды show cdp neighbors.

Функция должна возвращать словарь, который описывает соединения между устройствами.
Структура словаря такая же, как в задании 11.1:
    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}


Cгенерировать топологию, которая соответствует выводу из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt

В словаре, который возвращает функция create_network_map, не должно быть дублей.

С помощью функции draw_topology из файла draw_network_graph.py нарисовать схему на основании топологии, полученной с помощью функции create_network_map.
Результат должен выглядеть так же, как схема в файле task_11_2a_topology.svg


При этом:
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме

Не копировать код функций parse_cdp_neighbors и draw_topology.

Ограничение: Все задания надо выполнять используя только пройденные темы.

> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphvizi

> И модуль python для работы с graphviz:
> pip install graphviz

"""


from pprint import pprint
from draw_network_graph import draw_topology

def create_network_map(filenames):
    dictionary = {}
    results = {}
    for i in filenames:
        with open(i, 'r') as test:
            for cdp in test:
                if '>' in cdp:
                    r4 =  cdp.split('>')[0]
                elif '/' in cdp:
                    name, l_intf, l_n_intf, *other, r_intf = cdp.split()
                    local_interface = l_intf + l_n_intf
                    dest_interface = l_intf + r_intf
                    dictionary[(r4,local_interface)] = (name,dest_interface)
                    if not check_uniq(name,dest_interface,dictionary):
                        results[(r4,local_interface)] = (name,dest_interface)

    return results

def check_uniq(name,dest_interface,dictionary):
    '''
    Функция для проверки,чтобы значение не были в ключах
    Если значение не будет в ключах,значит возвращается false
    '''
    if dictionary.get((name,dest_interface)):
       return True
    else:
        return False
lists = ['sh_cdp_n_sw1.txt','sh_cdp_n_r1.txt','sh_cdp_n_r2.txt','sh_cdp_n_r3.txt']
#pprint(create_network_map(lists))

result = create_network_map(lists)
draw_topology(result)
