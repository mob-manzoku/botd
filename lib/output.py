#!/usr/bin/env python3
from abc import ABCMeta, abstractmethod
import json


class Output(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def send(self, message):
        pass

    def logging(self, message):
        log = {
            'name': self.name,
            'type_name': self.type_name,
            'message': message
        }

        print(json.dumps(log))
