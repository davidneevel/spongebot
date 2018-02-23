

import random
from twython import Twython
import keys
from time import sleep
TWITTER_APP_KEY = keys.TWITTER_APP_KEY #this is the burnedyourtweet cred
TWITTER_APP_KEY_SECRET = keys.TWITTER_APP_KEY_SECRET
TWITTER_ACCESS_TOKEN = keys.TWITTER_ACCESS_TOKEN
TWITTER_ACCESS_TOKEN_SECRET = keys.TWITTER_ACCESS_TOKEN_SECRET


import tweepy


auth = tweepy.OAuthHandler(TWITTER_APP_KEY, TWITTER_APP_KEY_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

 

trump_dict = eval(open("dicts/trumpdict.txt").read())
print trump_dict
length = len(trump_dict)
# print "trump dictionary length = %d" % length
errors = 0
print "starting loop"
while True:
    for status in tweepy.Cursor(api.user_timeline, screen_name='@realDonaldTrump',tweet_mode="extended").items(3):
        print status._json['full_text']
        text = status._json['full_text']
        text = text.encode("utf-8")
        tweetId = status._json['id']                   # The tweet ID!

        

        print tweetId
        match = 0
        for i in range(0, length):
            if int(trump_dict[i]) == tweetId:
                match += 1
        if match > 0:
            print "already did this fucker."
        else: 
            trump_dict[length] = tweetId
            # print trump_dict
            length += 1
            print "new tweet! adding to dictionary"
            write_to = open('dicts/trumpdict.txt', 'w')
            write_to.write('{\n')
            for i in range(0, length):
                    newline = str(i) + " : " + str(trump_dict[i]) + ",\n"
                    write_to.write(newline)
            write_to.write('}')
            write_to.close()
        
        
        
        
            # print text.encode('ascii', 'ignore')   # this might be useful if there are problems showing ampersands and whatnot
            # text = text.encode('ascii', 'ignore')   # this might be useful if there are problems showing ampersands and whatnot

            
            listText = list(text)
            print listText

            lenText = len(listText)


            print len(listText)


            reconstituted = ".@RealDonaldTrump "
            for i in range(lenText):
                # if listText[i] == '"':
                #        listText[i] += "\"" 
                # if listText[i] == "'":
                #         print "it happened"
                #         listText[i] = '\'' 
                if listText[i].isalpha():
                    try:
                        if i % 2 == 1:
                            listText[i] = listText[i].capitalize()
                            
                        else:
                            listText[i] = listText[i].lower()
                        
                        reconstituted += listText[i]
                    except: 
                        print "skipped a letter"
                else:
                   
                    reconstituted += listText[i]
                
                
            print listText

            print reconstituted   # this is the spongebobified tweet!
            
            if len(reconstituted) > 280:
                reconstituted = reconstituted[0:280]
            
            
           
            try:
                api.update_status(reconstituted, in_reply_to_status_id = tweetId) #haven't tried it yet but this should retweet to the tweet.
            except: errors +=1
        
    print "Errors: %d" % errors    
    print 'sleeping'
    sleep(2)






       




