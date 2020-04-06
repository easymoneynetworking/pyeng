# -*- coding: utf-8 -*-

"""
Задание 25.1c

Изменить класс Topology из задания 25.1b.

Добавить метод delete_node, который удаляет все соединения с указаным устройством.

Если такого устройства нет, выводится сообщение "Такого устройства нет".

Создание топологии
In [1]: t = Topology(topology_example)

In [2]: t.topology
Out[2]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Удаление устройства:
In [3]: t.delete_node('SW1')

In [4]: t.topology
Out[4]:
{('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Если такого устройства нет, выводится сообщение:
In [5]: t.delete_node('SW1')
Такого устройства нет

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

top.delete_node("R7")
pprint(top.topology)
