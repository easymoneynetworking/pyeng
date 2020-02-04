# -*- coding: utf-8 -*-
"""
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "Current configuration"]



from sys import argv

with open(argv[1], 'r') as src, open('config_sw1_cleared.txt', 'w') as dest:
        for file1 in src:
            line = file1
            ignore_line = False
            for word in ignore:
                if word in line:
                    ignore_line = True
            if ignore_line == True:
                pass
            elif ignore_line == False:
                dest.write(line)


# Все отлично

