##Autodm

SlackBot code to direct message everyone in a workspace, except people in a certain channel.

#To Get Started

`pip install virtualenv`

`virtualenv env`

`env\Scripts\activate`

`pip install slackclient`

Go to https://api.slack.com/apps. Login with your credentials.

Once you click on Create an App, fill in the App name and choose your workspace.

Go to the bot users tab and click on add a bot user.

Then, go to the OAuth and Permissions tab to allow the bot to access information of the workspace.

Go back to OAuth and Permission and you will see two tokens now present. These tokens are incredibly important, make sure you don't give them to anyone who shouldn't have access to the bot.

Create a separate token.txt file to store your bot's authentication token. Make sure you don't add that to any public repositories.