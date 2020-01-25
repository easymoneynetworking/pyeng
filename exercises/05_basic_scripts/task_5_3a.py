# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""
type_interface = input('Enter interface type access/trunk: ')
interface = input('Enter interface name: ')

sum_str = type_interface  + '_template'

access_template = [
        "switchport mode access",
        "switchport access vlan {}",
        "switchport nonegotiate",
        "spanning-tree portfast",
        "spanning-tree bpduguard enable",
]

trunk_template = [
        "switchport trunk encapsulation dot1q",
        "switchport mode trunk",
        "switchport trunk allowed vlan {}",
]

mode_dict = {'access_template': access_template, 'trunk_template': trunk_template}
key_mode = (mode_dict[sum_str])


mode2_dict = dict(access_template='Enter VLAN number: ', trunk_template='Enter valid Vlans: ')

vlan = input(mode2_dict[sum_str])

print('\n' + ' ' * 30)
print('interface {}'.format(interface))
print('\n'.join(key_mode).format(vlan))

