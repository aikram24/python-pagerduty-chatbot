# -*- coding: utf-8 -*-
import re
from slackbot.bot import respond_to

# import get API key function to get Pagerduty api
from apiKeyfunction import getApiKey, headers, api_url

# Request module for making api calls
import requests
import json
import os
import time

TEAM_IDS = []
INCLUDE = []


def list_users(query, uri='/users'):
    url = "{}/{}".format(api_url, uri)
    payload = {
        'query': query,
        'team_ids[]': TEAM_IDS,
        'include[]': INCLUDE,
        'limit': 100
    }
    r = requests.get(url, headers=headers, params=payload)
    return r.json()
@respond_to('ls user (.*) (.*)$', re.IGNORECASE)
def pd_users(message, userFirstName, userLastName):
	if userFirstName == None or userLastName == None:
		message.reply("Please pass in the user first and last name")
	else:
		userArray = ""
		data = list_users('{} {}'.format(userFirstName, userLastName))
		if len(data['users']) == 0:
			message.reply("I'm not able to find user {} {}".format(userFirstName, userLastName))
		else:
			user_data = data['users'][0]
			userArray+='```Name: {} \n'.format(user_data['name'])
			userArray+='Email: {}```'.format(user_data['email'])
			message.reply(userArray) 

