import tweepy
from threading import Timer
from discord.ext import commands

CONSUMER_KEY = 'wkyCWX6tbqoMzofxNxNvaj4uO'
CONSUMER_SECRET = 'E5JLWc5J7XJh3BdiplqTcsHDA8xTcqywxU1IOz6tf93cP6y0mm'
ACCESS_KEY = '1357426169210142720-DaManMmLL3dZG7euYb5hi7A2GjYuD6'
ACCESS_SECRET = 'giV2No9db7htJAIt3X3VZ4RiUDTBF614YklzTRGQvPccS'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

Client = commands.Bot(command_prefix='/')

tweets = []
userID = 'thebigamil'

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
            message_channel = Client.get_channel(840954658788343829)
            await message_channel.send(newtweet)
        Client.loop.create_task(timer())  
    Timer(3, checkfortweet).start()

checkfortweet()
Client.run('ODc3OTE4NDAyMTI2MTcyMjAx.YR5nOg.si1SP7E36NOHcEOPFh5mtBYpdC0')

         