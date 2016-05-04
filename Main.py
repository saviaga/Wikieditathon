import got
import tweepy

#import peewee
from dbwikipedia import Recruited,Tweets,Hashtag, SqliteDatabase, IntegrityError


def main():


    #status = "Testing!"
    #api.update_status(status=status)

    db = SqliteDatabase('wikipedians.db')
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
    for elem in tweet:
        printTweet("### Example 2 - Get tweets by query search [#dssenwikidata]", elem)


    print('users found saved to the database: ')
    for elem in tweet:
        # print(elem)

        print("username: ",elem.username)





        print("retweets: ",elem.retweets)
        print("text: ",elem.text)
        print("mentions: ",elem.mentions)
        print("hashtags: ", elem.hashtags)
        twitter_user_id = 0



        list_user.append({'twitter_user_id': twitter_user_id, 'screen_name': elem.username,'description':' '})
        list_hashtag.append({'user_of_hashtag': elem.username, 'hashtag_text': query})
        list_tweets.append({'user_tweets': elem.username, 'tweet_message': elem.text, 'mentions': elem.mentions, 'retweets': elem.retweets, 'hashtags_in_tweets': elem.hashtags})




   # for itemr,  itemt,itemh in zip(list_user, list_hashtag, list_tweets):
   # for itemr,  itemh in zip(list_user,  list_tweets):
    for itemr,itemt, itemh in zip(list_user, list_hashtag,list_tweets):
        try:

            # The following is the same as the short version Recruited.create(**itemr)
             a=  Recruited.create(twitter_user_id= itemr['twitter_user_id'],screen_name = itemr['screen_name'],description = itemr['description'])
             b = Tweets.create(user_tweets=itemh['user_tweets'], tweet_message=itemh['tweet_message'],  hashtags_in_tweets=itemh['hashtags_in_tweets'], mentions=itemh['mentions'],retweets=itemh['retweets'])
             c = Hashtag.create(user_of_hashtag=itemt['user_of_hashtag'], hashtag_text=itemt['hashtag_text'])
             a.save()
             b.save()
             c.save()
        except IntegrityError:
             pass



if __name__ == '__main__':



    main()
