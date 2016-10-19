#!/usr/bin/env python3
from lib import output


class Output_cli(output.Output):

    def __init__(self, conf):
        self.type_name = "cli"

    def send(self, message):
        print(message)
