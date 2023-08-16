import datetime
from api import db, ma

# Database models

# All keywords that are streaming or have been streamed
class xxxxx(db.Model):
    twitter_stream_id = db.Column(db.String(30), primary_key=True)
    keyword = db.Column(db.Text())
    geography = db.Column(db.Text())
    user_id = db.Column(db.Text())
    date = db.Column(db.DateTime, default = datetime.datetime.now)
    # tweets = db.relationship('Streamed', backref='allkeywords')

    def __init__(self, keyword, twitter_stream_id, user_id):
        self.keyword = keyword
        self.twitter_stream_id = twitter_stream_id
        self.user_id = user_id
        

class xxxx(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Allkeywords

xxxx = xxxx()

# Active keywords being streamed
class xxxxx(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    keyword = db.Column(db.Text())
    geography = db.Column(db.Text())
    twitter_stream_id = db.Column(db.String(30))
    user_id = db.Column(db.Text())
    date = db.Column(db.DateTime, default = datetime.datetime.now)

    def __init__(self, keyword, twitter_stream_id, user_id):
        self.keyword = keyword
        self.twitter_stream_id = twitter_stream_id
        self.user_id = user_id
        
class xxxxx(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Keywords

keyword_schema = KeywordSchema()
keywords_schema = KeywordSchema(many=True)

# All tweets streamed
class xxxx(db.Model):
    id = db.Column(db.Integer, primary_key=True) #id
    tweet_id = db.Column(db.String(100)) #id_str
    tweet_text = db.Column(db.Text())
    tweet_quote_count = db.Column(db.Integer) #quote_count
    tweet_reply_count = db.Column(db.Integer) #reply_count
    tweet_retweet_count = db.Column(db.Integer) #retweet_count
    tweet_like_count = db.Column(db.Integer) #like_count
    tweet_geo = db.String(200) #coordindates
    user_ID = db.Column(db.String(100)) #user.id
    user_name = db.Column(db.String(100)) #user.name
    user_description = db.Column(db.Text()) #text
    profile_image_url = db.Column(db.Text()) #text
    user_location = db.Column(db.Text())
    user_created_at = db.Column(db.String(100)) #user.created_at
    user_username = db.Column(db.String(100)) #user.username
    user_followers = db.Column(db.Integer) #user.followers_count
    user_following = db.Column(db.Integer) #user.followers_count
    user_tweet_count = db.Column(db.Integer) #user.followers_count
    user_listed_count = db.Column(db.Integer) #user.followers_count
    date = db.Column(db.DateTime, default = datetime.datetime.now)
    created_at = db.Column(db.String(100)) #created_at
    matching_rule_id = db.Column(db.String(30))
    matching_rule_tag = db.Column(db.Text())
    checked = db.Column(db.Integer, default=0)
    replied = db.Column(db.Integer, default=0)

    def __init__(self, tweet_id, tweet_text, tweet_quote_count, tweet_reply_count, tweet_retweet_count, 
    tweet_like_count, tweet_geo, user_ID, user_name, user_description, profile_image_url, user_location, user_created_at, user_username, 
    user_followers, user_following, user_tweet_count, user_listed_count, created_at, matching_rule_id, matching_rule_tag):
        self.tweet_id = tweet_id
        self.tweet_text = tweet_text
        self.tweet_quote_count = tweet_quote_count
        self.tweet_reply_count = tweet_reply_count
        self.tweet_retweet_count = tweet_retweet_count
        self.tweet_favorite_count = tweet_like_count
        self.tweet_coordinates = tweet_geo
        self.user_ID = user_ID
        self.user_name = user_name
        self.user_description = user_description
        self.profile_image_url = profile_image_url
        self.user_location = user_location
        self.user_created_at = user_created_at
        self.user_username = user_username
        self.user_followers = user_followers
        self.user_following = user_following
        self.user_tweet_count = user_tweet_count
        self.user_listed_count = user_listed_count
        self.created_at = created_at
        self.matching_rule_id = matching_rule_id
        self.matching_rule_tag = matching_rule_tag

class TweetSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Streamed

tweet_schema = TweetSchema()
tweets_schema = TweetSchema(many=True)

# Data for all users that have logged in
class xxxxx(db.Model):
    username = db.Column(db.String(40), primary_key=True, unique=True, nullable=False)
    access_token = db.Column(db.Text, nullable=False)
    private_token = db.Column(db.Text, nullable=False)

    def __init__(self, username, access_token, private_token):
        self.username = username
        self.access_token = access_token
        self.private_token = private_token

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

user_schema = UserSchema()
