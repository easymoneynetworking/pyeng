# -*- coding: utf-8 -*-
"""
Задание 17.4

Создать функцию write_last_log_to_csv.

Аргументы функции:
* source_log - имя файла в формате csv, из которого читаются данные (пример mail_log.csv)
* output - имя файла в формате csv, в который будет записан результат

Функция ничего не возвращает.

Функция write_last_log_to_csv обрабатывает csv файл mail_log.csv.
В файле mail_log.csv находятся логи изменения имени пользователя. При этом, email
пользователь менять не может, только имя.

Функция write_last_log_to_csv должна отбирать из файла mail_log.csv только
самые свежие записи для каждого пользователя и записывать их в другой csv файл.

Для части пользователей запись только одна и тогда в итоговый файл надо записать только ее.
Для некоторых пользователей есть несколько записей с разными именами.
Например пользователь с email c3po@gmail.com несколько раз менял имя:
C=3PO,c3po@gmail.com,16/12/2019 17:10
C3PO,c3po@gmail.com,16/12/2019 17:15
C-3PO,c3po@gmail.com,16/12/2019 17:24

Из этих трех записей, в итоговый файл должна быть записана только одна - самая свежая:
C-3PO,c3po@gmail.com,16/12/2019 17:24

Для сравнения дат удобно использовать объекты datetime из модуля datetime.
Чтобы упростить работу с датами, создана функция convert_datetimestr_to_datetime - она
конвертирует строку с датой в формате 11/10/2019 14:05 в объект datetime.
Полученные объекты datetime можно сравнивать между собой.

Функцию convert_datetimestr_to_datetime использовать не обязательно.

"""

import datetime
import re
from pprint import pprint
import csv

def convert_datetimestr_to_datetime(datetime_str):
    """
    Конвертирует строку с датой в формате 11/10/2019 14:05 в объект datetime.
    """
    return datetime.datetime.strptime(datetime_str, "%d/%m/%Y %H:%M")

def write_last_log_to_csv(source_log,output):
    finish_dictionary = {}
    finish_lists = []
    with open(source_log) as f:
        reader = csv.reader(f)
        full_list_with_headers = list(reader)
        full_list_withot_headers = full_list_with_headers[1::]
        finish_lists.append(full_list_with_headers[0])
        sorted_full_list = sorted(full_list_withot_headers, key=lambda x: convert_datetimestr_to_datetime(x[2]), reverse=True)
        for all_list in sorted_full_list:
            sorted_dictionary = {}
            sorted_dictionary[all_list[1]] = [all_list[0],all_list[2]]
            for key, values in sorted_dictionary.items():
                if key not in finish_dictionary:
                    finish_dictionary[key] = values
        print(finish_dictionary)
        for key2,values2 in finish_dictionary.items():
            values2.insert(1, key2)
            finish_lists.append(values2)
        with open(output, 'w') as fi:
            writer = csv.writer(fi)
            for row in finish_lists:
                writer.writerow(row)


if __name__ == "__main__":
    write_last_log_to_csv('mail_log.csv','ma_last_log.csv')



# Все отлично

# вариант решения
import csv


def write_last_log_to_csv(source_log, output):
    with open(source_log) as f:
        data = list(csv.reader(f))
        header = data[0]
    result = {}
    sorted_by_date = sorted(
        data[1:], key=lambda x: convert_datetimestr_to_datetime(x[2])
    )
    for name, email, date in sorted_by_date:
        result[email] = (name, email, date)
    with open(output, "w") as dest:
        writer = csv.writer(dest)
        writer.writerow(header)
        for row in result.values():
            writer.writerow(row)


if __name__ == "__main__":
    write_last_log_to_csv("mail_log.csv", "example_result.csv")
