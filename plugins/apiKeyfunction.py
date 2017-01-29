import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import slackbot_settings
def getApiKey():
	api_key = slackbot_settings.PAGER_DUTY_API
	return api_key

headers = {
	        'Accept': 'application/vnd.pagerduty+json;version=2',
	        'Authorization': 'Token token={token}'.format(token=getApiKey())
	    }

api_url = "https://api.pagerduty.com"
