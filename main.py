from discord.utils import get
import praw
import discord
import os
from dotenv import load_dotenv
from praw import reddit

load_dotenv('.env')
MAX_POSTS = 10

client = discord.Client()

@client.event
async def on_ready():
    # print the bot's name when login is complete to verify process completed
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    # when a user inputs the "!news" command, output the top 10 news posts and a link to their articles
    if message.author == client.user:
        return

    if message.content.startswith('!news'):
        # if the user input matches the command, print the top 10 posts from r/news
        # TODO: need to use asyncpraw for this part
        reddit = get_reddit()
        subreddit = reddit.subreddit('news')
        posts = get_hot_posts(subreddit)

        embedVar = discord.Embed(title="Here are the current hottest news posts:")
        for post in posts:
            embedVar.add_field(name="\u200b", value="[{}]({})".format(post.title, post.url))
        await message.channel.send(embed=embedVar)

def get_reddit():
    # get the credentials of the reddit user & bot
    reddit = praw.Reddit(
        user_agent = "comment-gathering script by u/DirkIsTheGOAT41",
        username = os.getenv('RD_BOT_USERNAME'),
        password = os.getenv('RD_BOT_PASSWORD'),
        client_id = os.getenv('RD_BOT_CLIENT_ID'),
        client_secret = os.getenv('RD_BOT_CLIENT_SECRET'),
    )
    return reddit

def get_hot_posts(subreddit):
    # get the top x posts from a given subreddit (set to 20 by default)
    posts = []
    i = 0
    for submission in subreddit.hot(limit=MAX_POSTS):
        # traverse through the top x posts in r/news, store them in an instance of Post, & display basic info on each
        posts.append(Post(submission.title, submission.permalink, submission.selftext, submission.url, submission.score))
        i += 1
    
    return posts

class Post:
    # Post class creates an instance of a post on the subreddit along with some important info (i.e. subtext)
    def __init__(self, title, permalink, selftext, url, score):
        self.title = title
        self.permalink = permalink
        self.selftext = selftext
        self.url = url
        self.score = score

def main():
    client.run(os.getenv('DC_BOT_TOKEN'))

if __name__ == '__main__':
    main()
