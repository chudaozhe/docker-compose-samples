#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: aaron
@contact: hi121073215@gmail.com
@date: 2021-10-18
@version: 0.0.0
@license:
@copyright:
"""
import json
import requests
import time

from elastalert.alerts import Alerter, DateTimeEncoder
from elastalert.util import elastalert_logger, EAException
from requests.exceptions import RequestException


class FeishuAlert(Alerter):
    required_options = frozenset(
        ['feishualert_botid', "feishualert_body"])

    def __init__(self, rule):
        super(FeishuAlert, self).__init__(rule)
        self.url = self.rule.get(
            "feishualert_url", "https://open.feishu.cn/open-apis/bot/v2/hook/")
        self.bot_id = self.rule.get("feishualert_botid", "")
        self.body = self.rule.get("feishualert_body", "")
        self.skip = self.rule.get("feishualert_skip", {})
        if self.bot_id == "" or self.body == "":
            raise EAException("Configure botid|body is invalid")

    def get_info(self):
        return {
            "type": "FeishuAlert"
        }

    def get_rule(self):
        return self.rule

    def alert(self, matches):
        now = time.strftime("%H:%M:%S", time.localtime())
        if "start" in self.skip and "end" in self.skip:
            if self.skip["start"] <= now and self.skip["end"] >= now:
                print("Skip match in silence time...")
                return

        headers = {
            "Content-Type": "application/json;",
        }
        body = {
            "msg_type": "interactive",
            "card": {
                "schema": "2.0",
                "body": {
                    "elements": []
                }
            }
        }

        if len(matches) > 0:
            try:
                exception = matches[0].get("exception", {})
                self.rule["feishualert_message"] = (exception if isinstance(exception, dict) else {}).get("message", "")
                self.rule["feishualert_time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                # 排除 type 键(规则中的type和日志中的type类型不同)
                rule_copy = {k: v for k, v in self.rule.items() if k != 'type'}
                merge = dict(**matches[0], **rule_copy)
                body['card']['body']['elements'] = [
                    {
                        "tag": "div",
                        "text": {
                            "tag": "plain_text",
                            "content": self.body.format(**merge)
                        }
                    },
                    {
                        "tag": "markdown",
                        "content": "```\n{}\n```".format(json.dumps(matches[0], ensure_ascii=False, indent=4))
                    }

                ]
                print("xxxx-ok...")
                print(json.dumps(body))
                print("xxxx-matches...")
                print(json.dumps(matches))
            except Exception as e:
                # 打印异常
                print("xxxx-err...")
                print(e)
                pass

        try:
            url = self.url + self.bot_id
            res = requests.post(data=json.dumps(
                body), url=url, headers=headers)
            res.raise_for_status()

        except RequestException as e:
            raise EAException("Error request to feishu: {0}".format(str(e)))
