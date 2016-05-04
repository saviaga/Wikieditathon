from peewee import *
import datetime

db=SqliteDatabase('wikipedians.db')

class BModel(Model):
    class Meta:
        database = db


class Recruited(BModel):
        user_id = IntegerField(primary_key=True,unique=True)
        twitter_user_id = IntegerField()
        screen_name = CharField(max_length=255, unique=True,index=True)
        description = TextField()


        class Meta:
             db_table = 'users_recruited'

class Tweets(BModel):
        #Saves the tweets that contain the hashtag that was used to recruit the user
        tweet_id = IntegerField(primary_key=True,unique=True)
        user_tweets = ForeignKeyField(Recruited, to_field='screen_name', related_name='tweets')
        tweet_message = TextField()
        #created_date = DateTimeField(default=datetime.datetime.now)
        hashtags_in_tweets = TextField()
        mentions = TextField()
        retweets = IntegerField()
        class Meta:
             db_table = 'user_tweets'

class Hashtag(BModel):
        hashtag_id = IntegerField(primary_key=True,unique=True)
        user_of_hashtag = ForeignKeyField(Recruited,to_field='screen_name', related_name='hashtag')
        hashtag_text =TextField()

        class Meta:
             db_table = 'user_hashtag'



if __name__ == '__main__':
     try:
        db.connect()
        db.create_tables([Recruited,Tweets,Hashtag])
     except OperationalError as e:
          print('Error: ', e)
