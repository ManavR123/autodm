import os
from slackclient import SlackClient
token = ''

def list_users():
	try:
		users_call = sc.api_call("users.list")
		if users_call.get('ok'):
			return users_call['members']
	except:
		print("users error")
	return None

def send_message(userid):
	try:
		group = sc.api_call(
			"usergroups	.create",
			token=token,
			channels="{0},UB7DJ5SL9".format(userid),
			name="Reminder {0}".format(userid),
		)
	except e:
		print(e.message)
		print("group error")

	if group['ok']:
		sc.api_call(
			"chat.postMessage",
			channel=group['id'],
			text="Hey there, just wanted to remind you to join <#CQCKS8UN6|secret-snowflake-fa19> by Wednesday night, if you want to participate in Secret Santa this year. It will be lots of fun!",
			username="Reminder",
			icon_emoji=":santa:",
			as_user=True
		)

if __name__ == '__main__':
	token = open(r"token.txt","r").read() # store actual in txt file and don't upload to github for security purposes
	print(token)
	sc = SlackClient(token)
	users = list_users()
	if users:
		print("Users: ")
		for u in users:
			try:
				if u['real_name'] == 'Akash Rathod':
					print(u['real_name'], u['id'])
					send_message(u['id'])
			except:
				pass
	else:
		print("unable to authenticate")