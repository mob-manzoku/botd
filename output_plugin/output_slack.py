#!/usr/bin/env python3
from lib import output


class Output_slack(output.Output):

    def __init__(self, conf):
        self.type_name = "slack"
        self.bot_name = conf.get("bot_name", "botd")
        self.api_key = conf.get("api_key")
