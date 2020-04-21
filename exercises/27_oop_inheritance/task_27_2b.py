# -*- coding: utf-8 -*-

"""
Задание 27.2b

Дополнить класс MyNetmiko из задания 27.2a.

Переписать метод send_config_set netmiko, добавив в него проверку на ошибки с помощью метода _check_error_in_command.

Метод send_config_set должен отправлять команды по одной и проверять каждую на ошибки.
Если при выполнении команд не обнаружены ошибки, метод send_config_set возвращает вывод команд.

In [2]: from task_27_2b import MyNetmiko

In [3]: r1 = MyNetmiko(**device_params)

In [4]: r1.send_config_set('lo')
---------------------------------------------------------------------------
ErrorInCommand                            Traceback (most recent call last)
<ipython-input-2-8e491f78b235> in <module>()
----> 1 r1.send_config_set('lo')

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

    def send_config_set(self, command):
        for com in command:
            output = super().send_config_set(com)
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
    r1.send_config_set('lo')

# Все отлично

# вариант решения

from netmiko.cisco.cisco_ios import CiscoIosBase
import re
from task_27_2a import ErrorInCommand


class MyNetmiko(CiscoIosBase):
    def __init__(self, **device_params):
        super().__init__(**device_params)
        self.enable()

    def _check_error_in_command(self, command, result):
        regex = "% (?P<err>.+)"
        message = (
            'При выполнении команды "{cmd}" на устройстве {device} '
            'возникла ошибка "{error}"'
        )
        error_in_cmd = re.search(regex, result)
        if error_in_cmd:
            raise ErrorInCommand(
                message.format(
                    cmd=command, device=self.ip, error=error_in_cmd.group("err")
                )
            )

    def send_command(self, command):
        command_output = super().send_command(command)
        self._check_error_in_command(command, command_output)
        return command_output

    def send_config_set(self, commands):
        if isinstance(commands, str):
            commands = [commands]
        commands_output = ""
        self.config_mode()
        for command in commands:
            result = super().send_config_set(command, exit_config_mode=False)
            commands_output += result
            self._check_error_in_command(command, result)
        self.exit_config_mode()
        return commands_output

