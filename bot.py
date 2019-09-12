import os
from dotenv import load_dotenv
import re
import slack

@slack.RTMClient.run_on(event='message')
def say_hello(**payload):
    data = payload['data']
    web_client = payload['web_client']
    rtm_client = payload['rtm_client']
    if 'Hello' in data['text']:
        channel_id = data['channel']
        thread_ts = data['ts']
        user = data['user']
        print(str(channel_id) + " " + str(thread_ts) + " " + str(user))
        print(data)

        web_client.chat_postMessage(
            channel=channel_id,
            text=f"Hi <@{user}>!"
        )
        
load_dotenv('.env')
slack_token = os.getenv('SLACK_API_TOKEN')
rtm_client = slack.RTMClient(token=slack_token)
rtm_client.start()