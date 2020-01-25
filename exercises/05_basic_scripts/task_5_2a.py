# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску, как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""


ip_address = input('Enter the ip address in format x.x.x.x/x: ')


ip_address1 = ip_address.replace('/','.')
ip_address2 = ip_address1.split(".")
ip_address3 = int(ip_address2[4])
maska0 = 32 - ip_address3
maska1 = '1' * ip_address3
maska2 = '0' * maska0
maska3 = maska1 + maska2
maska4 = maska3[0:8] + ' ' +maska3[8:16] + ' ' +maska3[16:24] + ' ' +maska3[24:33]
maska5 = maska4.split()
maska9 = int(maska5[0], 2)
maska10 = int(maska5[1], 2)
maska11 = int(maska5[2], 2)
maska12 = int(maska5[3], 2)

take_oktet0 = int(ip_address2[0]) & maska9
print(take_oktet0)
take_oktet1 = int(ip_address2[1]) & maska10
print(take_oktet1)
take_oktet2 = int(ip_address2[2]) & maska11
print(take_oktet2)
take_oktet3 = int(ip_address2[3]) & maska12
print(take_oktet3)

output = """
Network:
{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}

Mask:
/{4}
{9:<10}{10:<10}{11:<10}{12:<10}
{5:<10}{6:<10}{7:<10}{8:<10}
"""

print(output.format(take_oktet0, take_oktet1, take_oktet2, take_oktet3, int(ip_address2[4]), maska5[0], maska5[1], maska5[2], maska5[3], maska9, maska10, maska11, maska12 ))
