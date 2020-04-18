# -*- coding: utf-8 -*-

"""
Задание 27.2d

Дополнить класс MyNetmiko из задания 27.2c или задания 27.2b.

Добавить параметр ignore_errors в метод send_config_set.
Если передано истинное значение, не надо выполнять проверку на ошибки и метод должен работать точно так же как метод send_config_set в netmiko.

Если значение ложное, ошибки должны проверяться.

По умолчанию ошибки должны игнорироваться.


In [2]: from task_27_2d import MyNetmiko

In [3]: r1 = MyNetmiko(**device_params)

In [6]: r1.send_config_set('lo')
Out[6]: 'config term\nEnter configuration commands, one per line.  End with CNTL/Z.\nR1(config)#lo\n% Incomplete command.\n\nR1(config)#end\nR1#'

In [7]: r1.send_config_set('lo', ignore_errors=True)
Out[7]: 'config term\nEnter configuration commands, one per line.  End with CNTL/Z.\nR1(config)#lo\n% Incomplete command.\n\nR1(config)#end\nR1#'

In [8]: r1.send_config_set('lo', ignore_errors=False)
---------------------------------------------------------------------------
ErrorInCommand                            Traceback (most recent call last)
<ipython-input-8-704f2e8d1886> in <module>()
----> 1 r1.send_config_set('lo', ignore_errors=False)

...
ErrorInCommand: При выполнении команды "lo" на устройстве 192.168.100.1 возникла ошибка "Incomplete command."
"""

from netmiko.cisco.cisco_ios import CiscoIosBase
from pprint import pprint
import re

class ErrorInCommand(Exception):
    pass

class MyNetmiko(CiscoIosBase):
    def __init__(self, **device_params):
        self.ip = device_params['ip']
        super().__init__(**device_params)
        self.enable()


    def _check_error_in_command(self, command, result):
        regex_for_errors = r'% (.*)'
        found_error = re.search(regex_for_errors, result)
        if found_error:
            error = found_error.group(1)
            if 'Invalid input detected' in result:
                raise ErrorInCommand(f'При выполнении команды {command} на устройстве {self.ip} возникла ошибка {error}')
            elif 'Incomplete command' in result:
                raise ErrorInCommand(f'При выполнении команды {command} на устройстве {self.ip} возникла ошибка {error}')
            elif 'Ambigious command' in result:
                raise ErrorInCommand(f'При выполнении команды {command} на устройстве {self.ip} возникла ошибка {error} ')


    def send_command(self, command, **kwargs):
        output = super().send_command(command, **kwargs)
        self._check_error_in_command(command, output)
        return output

    def send_config_set(self, command, ignore_errors=True):
        for com in command:
            output = super().send_config_set(com)
            if ignore_errors == False:
                self._check_error_in_command(com, output)
        return output


if __name__ == "__main__":
    device_params = {
    "device_type": "cisco_ios",
    "ip": "192.168.100.1",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
    }
    r1 = MyNetmiko(**device_params)
    result = r1.send_config_set('lo', ignore_errors=True)
    pprint(result)
