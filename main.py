import os
from slackclient import SlackClient
token = ''

def list_users():
	try:
		users_call = sc.api_call("users.list")
		users = []
		if users_call.get('ok'):
			return users_call['members']
	except:
		print("users error")
	return None

def send_message(userid):
	sc.api_call(
		"chat.postMessage",
		channel=userid,
		text="Hey there, just wanted to remind you to join <#CQCKS8UN6|secret-snowflake-fa19> by Wednesday night, if you want to participate in Secret Santa this year. It will be lots of fun!",
		username="Reminder",
		icon_emoji=":santa:"
	)

if __name__ == '__main__':
	token = open(r"token.txt","r").read() # store actual in txt file and don't upload to github for security purposes
	sc = SlackClient(token)
	users = list_users()

	channel_members = sc.api_call(
											"channels.info",
											channel="CQCKS8UN6"
										)['channel']['members']
	if users:
		for u in users:
			try:
				if not u['id'] in channel_members:
					send_message(u['id'])
			except:
				pass
	else:
		print("unable to authenticate")