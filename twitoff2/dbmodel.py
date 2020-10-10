from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class User(DB.Model):
    Id = DB.Column(DB.BigInteger, primary_key=True)
    username = DB.Column(DB.String(80), unique=True, nullable=False)
    followers = DB.Column(DB.String(120), unique=True, nullable=False)
    #Tweet Ids are ordinal ints, so we can fetch most recent
    newest_tweet_id = DB.Column(DB.BigInteger, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Tweet(DB.Model):
    Id = DB.Column(DB.BigInteger, primary_key=True)
    tweet = DB.Column(DB.String(280), nullable=False)
    embedding = DB.Column(DB.PickleType, nullable = False)
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.Id'), nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweet', lazy=True))

    def __repr__(self):
        return '<Tweet %r>' % self.tweet
