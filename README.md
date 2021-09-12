# Reddit-Feed-Bot
Discord bot using the Discord.py API to display the top hot posts from a given subreddit on discord as taken from reddit by the PRAW API.

## Installation
To run this script, you will need a .env file in the main directory that contains the bot token for the bot you wish to use to run the script. Within the .env file enter: `DC_BOT_TOKEN='your_bot_token'` and the bot will work as intended within your server.

You'll also need to get OAuth2 permissions for a reddit script bot as well in order for the bot to gather posts from reddit. Within the .env, enter:
```
RD_BOT_CLIENT_ID='your bot's client ID'
RD_BOT_CLIENT_SECRET='your bot's secret ID'
RD_BOT_USERNAME='your bot's username'
RD_BOT_PASSWORD='your bot's password'
```

## Commands
`!news`: get the top 10 hot posts from r/news and display them as embedded hyperlinks to the articles.\n
`!get 'subreddit_name'`: get the top 10 hot posts from a specified subreddit along with links to the reddit posts.
