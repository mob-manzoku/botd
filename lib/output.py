#!/usr/bin/env python3
from abc import ABCMeta, abstractmethod


class Output(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def send(self, message):
        pass
