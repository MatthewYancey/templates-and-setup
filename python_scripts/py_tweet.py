from twitter import *
from time import gmtime, strftime

class direct_message(object):

    def __init__(self, msg):

        access_token = '727068165067264001-6txuLk1EPrSCpIThbnEyvIYMpxKHHw6'
        access_token_secret = 'bQjv2x1HgXcRH8CioXNsIGu72KbI5too6enWDTI4Ldy9i'
        consumer_key = 'vTfFOFQodNkWAZfX352WkXOAD'
        consumer_secret = 'BA2AR5vD0IUHp8cGppGMkOe9zuqUuvdqhIvcohEauyx3r2ZpHF'
        t = Twitter(auth = OAuth(access_token, access_token_secret, consumer_key, consumer_secret))

        tweet_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        t.statuses.update(status = msg + ' ' + tweet_time)
