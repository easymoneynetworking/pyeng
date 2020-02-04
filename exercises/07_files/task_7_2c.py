# -*- coding: utf-8 -*-
"""
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ignore = ["duplex", "alias", "Current configuration"]

from sys import argv

with open(argv[1], 'r') as src, open(argv[2], 'w') as dest:
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

