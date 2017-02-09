# Pagerduty Chatbot Python
###### A pagerduty chat bot using [lins05/slackbot](https://github.com/lins05/slackbot) as a framework.

# Installation
```git clone https://github.com/aikram24/python-pagerduty-chatbot.git```

```pip install -r requirements.txt```

# Usage
#### Generate tokens
1. Generate an api token on [slack web api page](https://api.slack.com/web)
 * Update **SLACK_API_TOKEN** in slackbot_settings.py
2. Generate bot user integration by going https://**<domain name>**.slack.com/apps/build/custom-integration
 * Update **API_TOKEN** in slackbot_settings.py
3. Genrate [Pagerduty token V2](https://support.pagerduty.com/hc/en-us/articles/202829310-Generating-an-API-Key)
 * Update **PAGER_DUTY_API** in slackbot_settings.py

# Run the bot
```python run_bot.py ```

# Available Commands
* ls oncall - _list oncall users_
* who( is|se) oncall - _list oncall users_
* eoc - _list oncall users_
* Oncall for `<Schedule Name>`
* ls oncall for `<Schedule Name>` - _list oncall users for specific schedule_
* who( is|se) oncall for `<Schedule Name>` - _list oncall users for specific schedule_
* eoc for `<Schedule Name>` - _list oncall users for specific schedule_

**Team Member assoicate with Schedule**
* ls schedule <schedule name> - _list all members for mentioned schedule_

**Services / Alert Help**
* ls services - _list all the services available for hail through API_
* ls service for `<Service Name>` - _Give the service API Key_
* trigger | trig | hail `<Service Name>` `<Message>` = _Ping the group with message and will you give you the incident_key_'
