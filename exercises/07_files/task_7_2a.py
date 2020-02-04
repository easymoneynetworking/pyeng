# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "Current configuration"]


from sys import argv

with open(argv[1], 'r') as f:
        for test in f:
            a = test.replace('!','')
            line = a.rstrip('\n')

            ignore_line = False
            for word in ignore:
                if word in line:
                    ignore_line = True
            if ignore_line == True:
                pass
            elif ignore_line == False:
                print(line)

# Все отлично

# вариант решения

filename = "config_sw1.txt"

with open(filename) as f:
    for line in f:
        skip_line = False
        for ignore_word in ignore:
            if ignore_word in line:
                skip_line = True
                break
        if not line.startswith("!") and not skip_line:
            print(line.rstrip())
