# -*- coding: utf-8 -*-
import re
from slackbot.bot import respond_to
# from slackbot.bot import listen_to

# import get API key function to get Pagerduty api
from apiKeyfunction import getApiKey, headers, api_url

# Request module for making api calls
import requests
import json
import os
import time

def get_schedules(schedule_name='', uri='/schedules'):
	url = "{}/{}".format(api_url, uri)
	payload = {
		'query': schedule_name,
		'limit': 100
	}
	r = requests.get(url, headers=headers, params=payload)
	return r.json()


@respond_to('ls schedules$', re.IGNORECASE)
@respond_to('ls schedule (.*)$', re.IGNORECASE)
def pd_schedules(message, schedule_name=''):
	if schedule_name != "":
		schedules = get_schedules(schedule_name)['schedules']
	else:
		schedules = get_schedules('')['schedules']
	reply_output = ""
	for schedule in schedules:
		user_list = ""
		for user in schedule['users']:
			user_list += "{}, ".format(user['summary'])
		reply_output += "Name: *{}*\nURL: *{}*\nTeam Members: *{}*\n---------------------------\n".format(schedule['name'], schedule['html_url'], user_list[:-2])
	message.reply(reply_output)


