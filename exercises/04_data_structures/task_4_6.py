# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ospf_route = "O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
#Пока достичь результата,у меня получается с помощью костыльных методов
#Для начала я удаляю символы,которые мне мешают в последствии- это квадратные скобки и запятые
ospf1 = ospf_route.replace(',', '').replace('[','').replace(']','')
#print(ospf1)
#Далее методом split получаю список strings для того,чтобы к ним можно обращаться по индексу
ospf2 = (ospf1.split())
#Далее использую метод format,обращаясь к разным индексам для корректного вывода.
ip_template = '''
Protocol:             {0:>}
Prefix:               {1:>}
AD/Metric             {2:>} 
Next-Hop:             {3:>}
Last update:          {4:>}     
Outbound Interface:   {5:>}
'''
print(ip_template.format('OSPF', ospf2[1], ospf2[2], ospf2[4], ospf2[5],  ospf2[6]))

