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

outList = []
TIME_ZONE = 'EST'
INCLUDE = []
USER_IDS = []
ESCALATION_POLICY_IDS = []
SINCE = ''
UNTIL = ''
EARLIEST = False

def list_oncalls(scheduleID, uri='/oncalls'):
    url = "{}/{}".format(api_url, uri)
    payload = {
        'time_zone': TIME_ZONE,
        'include[]': INCLUDE,
        'user_ids[]': USER_IDS,
        'escalation_policy_ids[]': ESCALATION_POLICY_IDS,
        'schedule_ids[]': scheduleID,
        'since': SINCE,
        'until': UNTIL,
        'earliest': EARLIEST,
        'limit': 5
    }
    r = requests.get(url, headers=headers, params=payload)
    time.sleep(1/250)
    data = r.json()
    try:
        return data['oncalls'][0]['user']['summary']
    except IndexError:
        return 'nothing'


def list_schedules(query='',uri='/schedules'):
    url = "{}/{}".format(api_url, uri)
    payload = {
        'query': query,
        'limit': 40
    }
    r = requests.get(url, headers=headers, params=payload)
    data =  r.json()
    return data

@respond_to('EOC$', re.IGNORECASE)
@respond_to('ls oncall$', re.IGNORECASE)
@respond_to("^who(?:s| is|se)? (?:oncall)$", re.IGNORECASE)
def pd_oncall(message):
    data = ""
    for v in list_schedules('')['schedules']:
        user = list_oncalls(v['id'])
        out = "`{}`  -  *{}* \n".format(v['summary'], user)
        data += str(out)
    message.reply(data) 

@respond_to('EOC for (.*)$', re.IGNORECASE)
@respond_to("^who(?:s| is|se)? (?:oncall) for (.*)$", re.IGNORECASE)
@respond_to('ls oncall for (.*)$', re.IGNORECASE)
def pd_one_oncall(message, scheduleName):
    if scheduleName.lower() != "":
        data = ""
        for v in list_schedules('{}'.format(scheduleName))['schedules']:
            user = list_oncalls(v['id'])
            out = "`{}`  -  *{}* \n".format(v['summary'], user)
            data += str(out)
        message.reply(data) 
    else:
        message.reply('No schedule found with name {}'.format(scheduleName))
