# -*- coding: utf-8 -*-

"""
Задание 25.1d

Изменить класс Topology из задания 25.1c

Добавить метод add_link, который добавляет указанное соединение, если его еще нет в топологии
Если соединение существует, вывести сообщение "Такое соединение существует",
Если одна из сторон есть в топологии, вывести сообщение "Cоединение с одним из портов существует"


Создание топологии
In [7]: t = Topology(topology_example)

In [8]: t.topology
Out[8]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [9]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))

In [10]: t.topology
Out[10]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [11]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
Такое соединение существует

In [12]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/5'))
Cоединение с одним из портов существует


"""

from pprint import pprint

class Topology:
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)


    def _normalize(self, topology_dict):
        topology_dic = {}
        for key,value in topology_dict.items():
            if not topology_dic.get(value) == key:
                topology_dic[key] = value
        return topology_dic

    def delete_link(self, name_link_left, name_link_right):
        if self.topology.get(name_link_left):
            del self.topology[name_link_left]
        elif self.topology.get(name_link_right):
            del self.topology[name_link_right]
        else:
            print('Такого соединения нет')

    def delete_node(self, name_node):
        lenght_before_loop = len(self.topology)
        for key, value in list(self.topology.items()):
            if key[0] == name_node:
                del self.topology[key]
            elif value[0] == name_node:
                del self.topology[key]
        lenght_after_loop = len(self.topology)
        if lenght_before_loop == lenght_after_loop:
            print('Такого устройства нет')

    def add_link(self, name_link_left, name_link_right):
        variable_flag = True
        for key, value in list(self.topology.items()):
            if value == name_link_right and key == name_link_left:
                pprint('Такое соединение существует')
            elif value == name_link_right or key == name_link_left:
                variable_flag = False
        if variable_flag == False:
            print('Cоединение с одним из портов существует')
        else:
            self.topology[name_link_left] = name_link_right

topology_example = {
    ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
    ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
    ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
    ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
    ("R3", "Eth0/1"): ("R4", "Eth0/0"),
    ("R3", "Eth0/2"): ("R5", "Eth0/0"),
    ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
    ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
    ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
}

top = Topology(topology_example)
#pprint(top.topology)

top.delete_link(("R5", 'Eth0/0'), ("R3", "Eth0/2"))
#pprint(top.topology)

top.delete_node("R1")
pprint(top.topology)

top.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
pprint(top.topology)
