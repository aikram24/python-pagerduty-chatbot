# -*- coding: utf-8 -*-
import re
from slackbot.bot import respond_to
# from slackbot.bot import listen_to

# import get API key function to get Pagerduty api
from apiKeyfunction import getApiKey, headers, api_url
from help_menu import menu
# Request module for making api calls
import requests
import json
import os
import time


def return_help(help_menu):
	help_string = ""
	for help_item in help_menu:
		help_string += "{}\n".format(help_item)
	return help_string



@respond_to('ls help$', re.IGNORECASE)
@respond_to('help$', re.IGNORECASE)
def pd_help(message):
    message.reply(return_help(menu)) 