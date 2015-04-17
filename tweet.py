"""Demonstrate Twitter API"""

import sys, os, twitter, markov


# Use Python os.environ to get at environmental variables
#
# Note: you must run `source secrets.sh` before running this file
# to make sure these environmental variables are set.

api = twitter.Api(
    consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
    consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
    access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
    access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

# This will print info about credentials to make sure they're correct
print api.VerifyCredentials()

source_filename = sys.argv[1:]
twitter_markov = markov.TwitterableMarkovGenerator(source_filename)

tweet = twitter_markov.make_text(twitter_markov.chains)
print tweet
# Send a tweet
status = api.PostUpdate(tweet)
#print status.text

# Now you can go to http://twitter.com/hackbright0 to see it
#
# (if you changed secrets.sh, you can go to your Twitter timeline to see it)