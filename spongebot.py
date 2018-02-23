# works! this was the evolution of servo_print_vid_twit_reply
# in this version moved servo shit into servo_shit.py


import time
from time import sleep

import subprocess
import os

# twitter shit
from twython import Twython
TWITTER_APP_KEY = '7x6A0ravZTsdWduW90HjPK9Tw' #this is the burnedyourtweet cred
TWITTER_APP_KEY_SECRET = 'lSs2HAA8oqKAB2jNpYawhjWv1sKMo53tPCbowjFGiHbfarVLbz'
TWITTER_ACCESS_TOKEN = '843771913231093760-8NEn0S3Xhoy5DJ2IUNfPSC8X9h9v7An'
TWITTER_ACCESS_TOKEN_SECRET = 'ZniPgmy710riapjONVFdxunABDbhhXnzekC5vP2tsnKEL'


client_args = {
    'timeout': 1300
}

t = Twython(app_key=TWITTER_APP_KEY,
            app_secret=TWITTER_APP_KEY_SECRET,
            oauth_token=TWITTER_ACCESS_TOKEN,
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET,
            client_args=client_args)









'''    ____ _____ _____   _______        _______ _____ _____ ____
        / ___| ____|_   _| |_   _\ \      / / ____| ____|_   _/ ___|
        | |  _|  _|   | |     | |  \ \ /\ / /|  _| |  _|   | | \___ \
        | |_| | |___  | |     | |   \ V  V / | |___| |___  | |  ___) |
        \____|_____| |_|     |_|    \_/\_/  |_____|_____| |_| |____/
'''



# NOW GET THOSE TRUMPY TWEETS
print "OK GETTING TRUMP TWEETS NOW"
search_for = 'RealDonaldTrump'
user_timeline = t.get_user_timeline(screen_name = search_for,
    count = 5, include_retweets=False, tweet_mode=extended)

for tweet in user_timeline:
    # tweetText = tweet['text'] gets raw tweet text.
    # the .encode bit ignores all non-ascii chars! phew.
    tweetText = tweet['text'].encode('ascii', 'ignore')


    idstring = str(tweet['id_str'])


    trump_dict = eval(open("dicts/trumpdict.txt").read())
    #print trump_dict
    length = len(trump_dict)
    print "trump dictionary length = %d" % length

    match = 0
    for i in range(0, length):
        if trump_dict[i] == idstring:
            match += 1
    if match > 0:
        print "MATCHED, already burned this fucker"
    elif match == 0: #new tweet! add it to the dictionary
        print tweetText
        print idstring
        print "NEW TWEET! adding to dictionary"
        newlength = length + 1
        trump_dict[length] = idstring
        print "updated trump dictionary, added %s" % idstring
        print trump_dict
        write_to = open('dicts/trumpdict.txt', 'w')
        write_to.write('{\n')
        for i in range(0, newlength):
            newline = str(i) + " : '" + trump_dict[i] + "',\n"
            write_to.write(newline)

        write_to.write('}')
        write_to.close()
        #and add it to the todo list
        print "tweetText = %s" % tweetText
        reply_to = '@' + search_for
        todoItem = [reply_to, idstring, tweetText]
  

   
   




if 0:   # turn off or on Vid upload
    
    msg = ".%s I burned your tweet." % doUser

    video = open(uploadvidname, 'rb')
    response = t.upload_video(media=video,media_type='video/mp4')
    t.update_status(status=msg, media_ids=[response['media_id']],
        in_reply_to_status_id=doId)

