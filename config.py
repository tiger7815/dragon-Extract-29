#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6232350725:AAFFT1PF5eKJYgTtuHt_DPFrM_u9kJflals")
    API_ID = int(os.environ.get("API_ID", "10577960"))
    API_HASH = os.environ.get("API_HASH", "80fd047285f4e94ca80311928b6bb5da")
    AUTH_USERS = "6253923773,6981453498"

