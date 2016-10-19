#!/usr/bin/env python3
from urllib.parse import urlencode
import urllib.request as urlrequest
import json
from lib import output


class Output_slack(output.Output):

    def __init__(self, conf):
        self.type_name = "slack"
        self.name = conf.get("name")
        self.bot_name = conf.get("bot_name", "botd")
        self.channel = conf.get("channel")
        self.hool_url = conf.get("hook_url")

    def send(self, message):
        payload = {
            'username': self.bot_name,
            'text': message
        }

        payload_json = json.dumps(payload)
        data = urlencode({"payload": payload_json})

        req = urlrequest.Request(self.hool_url)
        opener = urlrequest.build_opener(urlrequest.HTTPHandler())

        with opener.open(req, data.encode('utf-8')) as res:
            self.logging(res.read().decode('utf-8'))
