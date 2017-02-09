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

def getServices(query, uri='/services'):
    url = "{}/{}".format(api_url, uri)
    payload = {
        'query': query,
        'limit': 100
    }
    r = requests.get(url, headers=headers, params=payload)
    return r.json()


def getIntegrationKey(servicesID, integrationID, uri='/services'):
	uri ='/services/{}/integrations/{}'.format(servicesID, integrationID)
	url = "{}/{}".format(api_url, uri)
	payload = {
        'include[]': [],
        'limit': 100
        }
        r = requests.get(url, headers=headers, params=payload)
        return r.json()


token=getApiKey()
def trigger_incident(serviceKey, description, reporterName):
    headers = {
        'Authorization': 'Token token={}'.format(token),
        'Content-type': 'application/json',
    }
    payload = json.dumps({
      "service_key": serviceKey,
      "event_type": "trigger",
      "description": description,
      "client": reporterName,
    })
    r = requests.post(
                    'https://events.pagerduty.com/generic/2010-04-15/create_event.json',
                    headers=headers,
                    data=payload,
    )
    if r.status_code == 400:
    	return r.status_code,r.text
    else:
    	return r.json()


def main(serviceName='HAIL-'):
	if serviceName == 'HAIL-':
		servicesList = getServices('HAIL-')['services']
		data = ""
		for servids in servicesList:
			data += "\n{}".format(servids['name'])
		return data
	else:
		servicesList = getServices(serviceName)['services']
		for servids in servicesList:
			sid= servids['id']
			iid= servids['integrations'][0]['id']
			return getIntegrationKey(sid, iid)['integration']['integration_key']

def get_UserName(userID):
	# userID = message._get_user_id()
	import slackbot_settings
	payload = {'token': slackbot_settings.SLACK_API_TOKEN, 'user': userID}
	r = requests.get('https://slack.com/api/users.info', params=payload)
	slack_res = r.json()
	userName = slack_res['user']['name']
	return userName


@respond_to('ls services$', re.IGNORECASE)
def pd_ls_hail_list(message):
	data = main()
	message.reply("```{}```".format(data))

@respond_to('ls service (.*)$', re.IGNORECASE)
@respond_to('ls service key (.*)$', re.IGNORECASE)
def pd_ls_services(message, serviceName):
	data = main(serviceName)
	message.reply("*{}* generic key is _{}_".format(serviceName, data))


@respond_to('trigger ([\w\-]+) (.+)$', re.IGNORECASE)
@respond_to('trig ([\w\-]+) (.+)$', re.IGNORECASE)
@respond_to('hail ([\w\-]+) (.+)$', re.IGNORECASE)
def pd_trigger(message, service_group, inc_description):
	userID = message._get_user_id()
	userName = get_UserName(userID)
	serKey = main(service_group.upper())
	req = trigger_incident(serKey, inc_description, userName)
	# if req[0] != 200:
	if type(req) is list:
		message.reply("*{} BAD REQUEST*\n ```Error Detail: {}```".format(req[0], req[1]))
	else:
		message.reply("```incident_key: {}\nStatus: {}```".format(req['incident_key'], req['status']))
