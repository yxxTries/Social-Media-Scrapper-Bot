import tweepy
from threading import Timer
from discord.ext import commands

CONSUMER_KEY = 'KEY'
CONSUMER_SECRET = 'KEY'
ACCESS_KEY = 'KEY'
ACCESS_SECRET = 'KEY'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

Client = commands.Bot(command_prefix='/')

tweets = []
userID = 'nasa'

@Client.event
async def on_ready():
    print("we have logged in as {0.user}".format(Client))\

def checkfortweet():
    tweet = api.user_timeline(screen_name=userID, 
                                # 200 is the maximum allowed count
                                count=1, 
                                include_rts = False,
                                # Necessary to keep full_text 
                                # otherwise only the first 140 words are extracted
                                tweet_mode = 'extended'
                                )
    for info in tweet:
        tweetlink = ("https://twitter.com/twitter/statuses/{}".format(info.id))
        dateoftweet = (info.created_at)
        tweetext = (info.full_text)

    if tweetlink in tweets:
        None
    else:
        tweets.clear()
        tweets.append(tweetlink)
        newtweet = (str(tweets)[2:-2])
        print(newtweet)
        async def timer():
            await Client.wait_until_ready()
            message_channel = Client.get_channel(878548256538374204)
            await message_channel.send(newtweet)
        Client.loop.create_task(timer())  
    Timer(3, checkfortweet).start()

checkfortweet()
Client.run('KEY')

         
