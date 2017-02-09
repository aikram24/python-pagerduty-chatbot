# Pagerduty Chatbot Python
###### A pagerduty chat bot using [lins05/slackbot](https://github.com/lins05/slackbot) as a framework.

# Installation
```git clone https://github.com/aikram24/python-pagerduty-chatbot.git```
```pip install -r requirements.txt```

# Usage
#### Generate tokens
1. Generate an api token on [slack web api page](https://api.slack.com/web).
..* Update **SLACK_API_TOKEN** in slackbot_settings.py
2. Generate bot user integration by going https://**<domain name>**.slack.com/apps/build/custom-integration
..* Update **API_TOKEN** in slackbot_settings.py
3. Genrate [Pagerduty token V2](https://support.pagerduty.com/hc/en-us/articles/202829310-Generating-an-API-Key)
..* Update **PAGER_DUTY_API** in slackbot_settings.py

# Run the bot
```python run_bot.py ```
