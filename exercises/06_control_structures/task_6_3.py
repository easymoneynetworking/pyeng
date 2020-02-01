# -*- coding: utf-8 -*-
"""
Задание 6.3

В скрипте сделан генератор конфигурации для access-портов.

Сделать аналогичный генератор конфигурации для портов trunk.

В транках ситуация усложняется тем, что VLANов может быть много, и надо понимать,
что с ним делать.

Поэтому в соответствии каждому порту стоит список
и первый (нулевой) элемент списка указывает как воспринимать номера VLAN,
которые идут дальше.

Пример значения и соответствующей команды:
	['add', '10', '20'] - команда switchport trunk allowed vlan add 10,20
	['del', '17'] - команда switchport trunk allowed vlan remove 17
	['only', '11', '30'] - команда switchport trunk allowed vlan 11,30

Задача для портов 0/1, 0/2, 0/4:
- сгенерировать конфигурацию на основе шаблона trunk_template
- с учетом ключевых слов add, del, only

Код не должен привязываться к конкретным номерам портов. То есть, если в словаре
trunk будут другие номера интерфейсов, код должен работать.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan",
]

access = {"0/12": "10", "0/14": "11", "0/16": "17", "0/17": "150"}
trunk = {"0/1": ["add", "10", "20"], "0/2": ["only", "11", "30"], "0/4": ["del", "17"]}

for intf, vlan in access.items():
    print("interface FastEthernet" + intf)
    for command in access_template:
        if command.endswith("access vlan"):
            print(" {} {}".format(command, vlan))
        else:
            print(" {}".format(command))


for tru, vla in trunk.items():
    print('\n' + '-' * 30)
    print("interface FastEthernet" + tru)
    for command1 in trunk_template:
        if vla[0] == "add" and  command1.endswith("allowed vlan"):
            first, *other = vla
            new = str(other).replace(']','').replace('[','').replace("'","").replace(" ","")
            print("{} add {}".format(command1, new))
        elif vla[0] == "only" and  command1.endswith("allowed vlan"):
            first, *other = vla
            new = str(other).replace(']','').replace('[','').replace("'","").replace(" ","")
            print("{} {}".format(command1, new))
        elif vla[0] == "del" and  command1.endswith("allowed vlan"):
            new = str(other).replace(']','').replace('[','').replace("'","").replace(" ","")
            print("{} remove {}".format(command1, new))
        else:
            print("{}".format(command1))

