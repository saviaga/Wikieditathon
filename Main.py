import got
import tweepy

import peewee
from dbwikipedia import *


def main():


    #status = "Testing!"
    #api.update_status(status=status)

    db = SqliteDatabase('wikipedians2.db')
    db.connect()

    def printTweet(descr, t):
        print descr
        print "Username: %s" % t.username
        print "Retweets: %d" % t.retweets
        print "Text: %s" % t.text
        print "Mentions: %s" % t.mentions
        print "Hashtags: %s\n" % t.hashtags

    # Example 1 - Get tweets by username
    #tweetCriteria = got.manager.TweetCriteria().setUsername('barackobama').setMaxTweets(1)
    #tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]

    #printTweet("### Example 1 - Get tweets by username [barackobama]", tweet)

    # Example 2 - Get tweets by query search
    #tweetCriteria = got.manager.TweetCriteria().setQuerySearch('europe refugees').setSince("2015-05-01").setUntil("2015-09-30").setMaxTweets(1)
    #tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]

    #printTweet("### Example 2 - Get tweets by query search [europe refugees]", tweet)

    # Example 3 - Get tweets by username and bound dates
    #tweetCriteria = got.manager.TweetCriteria().setUsername("barackobama").setSince("2015-09-10").setUntil("2015-09-12").setMaxTweets(1)
    #tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]

    #printTweet("### Example 3 - Get tweets by username and bound dates [barackobama, '2015-09-10', '2015-09-12']", tweet)

    # Example 2 - Get tweets by query search
    list_user = []
    list_hashtag = []
    list_tweets = []
    #query= '#dssenwikidata'
    query = input("Hashtag?")

    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(query).setMaxTweets(10000)
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)
    conta = 0
  #  for elem in tweet:
  #      printTweet("### Example 2 - Get tweets by query search [#dssenwikidata]", elem)


    print('users found saved to the database: ')
    for elem in tweet:
        # print(elem)

        print("username: ",elem.username)



        print("tweet id ",elem.id )

        print("retweets: ",elem.retweets)
        print("text: ",elem.text)
        print("mentions: ",elem.mentions)
        print("hashtags: ", elem.hashtags)
        twitter_user_id = 0
        conta = conta + 1
        print("contador ",conta)



        list_user.append({'twitter_user_id': twitter_user_id, 'screen_name': elem.username,'description':' '})
        list_hashtag.append({'user_of_hashtag': elem.username, 'hashtag_text': query})
        list_tweets.append({'tweet_id':elem.id,'user_tweets': elem.username, 'tweet_message': elem.text, 'mentions': elem.mentions, 'retweets': elem.retweets, 'hashtags_in_tweets': elem.hashtags})




   # for itemr,  itemt,itemh in zip(list_user, list_hashtag, list_tweets):
   # for itemr,  itemh in zip(list_user,  list_tweets):
    cont = 0
    for itemr in list_user:
        try:
            a = Recruited.create(twitter_user_id=itemr['twitter_user_id'], screen_name=itemr['screen_name'],
                             description=itemr['description'])
            a.save(force_insert=True)
        except IntegrityError:
            pass

    for itemr,itemt, itemh in zip(list_user, list_hashtag,list_tweets):
        try:
             cont = cont + 1
             print("saving in database", cont)
            # The following is the same as the short version Recruited.create(**itemr)
             b = Tweets.create(tweet_id=itemh['tweet_id'],user_tweets=itemh['user_tweets'], tweet_message=itemh['tweet_message'],  hashtags_in_tweets=itemh['hashtags_in_tweets'], mentions=itemh['mentions'],retweets=itemh['retweets'])
             c = Hashtag.create(user_of_hashtag=itemt['user_of_hashtag'], hashtag_text=itemt['hashtag_text'])
             b.save(force_insert=True)
             c.save(force_insert=True)
        except IntegrityError:
             pass

    db.close()

if __name__ == '__main__':



    main()
