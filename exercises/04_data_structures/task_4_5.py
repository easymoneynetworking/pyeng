# -*- coding: utf-8 -*-
"""
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2 (пересечение).

Результатом должен быть список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'
#разбиваем строку на части для того,чтобы получить значение vlans в одно значение
split1 =  command1.split()
#print(split1)
split2 = command2.split()
#print(split2)
#Из получившихся стрки разделенной на части обращаемся к последнему элементу,
#Зная заранее,что при выводе команды значение vlan идут в конце
vlan1 = split1[-1]
#print(vlan1)
vlan2 = split2[-1]
#print(vlan2)
#Преобразуем в множества для того,чтобы найти пересечение
set1 = set(vlan1)
set2 = set(vlan2)
#print(set1)
#print(set2)
#Находим пересечение,только вот запятая мешает.
#Поэтому сначала удалим запятую
set1.discard(',')
set2.discard(',')
#print(set1)
#print(set2)
peresechenie = set1.intersection(set2)
#print(peresechenie)
list = list(peresechenie)
print(list)


# Все отлично
# только вот set примененный к строке помог в этом случае потому что все числа были < 10
# если бы числа были >= 10, то примерение set дало бы такой результат
#In [1]: vlans = '1,2,3,10,15'

#In [2]: set(vlans)
#Out[2]: {',', '0', '1', '2', '3', '5'}

# вланов 10 и 15 нет, так как set превращает строку в множество из символов

# вариант решения

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"

vlans1 = command1.split()[-1].split(",")
vlans2 = command2.split()[-1].split(",")

intersection = sorted(set(vlans1) & set(vlans2))
print(intersection)
