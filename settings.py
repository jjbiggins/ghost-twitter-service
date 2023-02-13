#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from decouple import config

OAUTH_CONSUMER_KEY = config('OAUTH_CONSUMER_KEY')
OAUTH_CONSUMER_SECRET = config('OATH_CONSUMER_SECRET')
OAUTH_ENDPOINT = config('OAUTH_ENDPOINT')

TWEETS_ENDPOING = "https://api.twitter.com/2/tweet://api.twitter.com/2/tweets"



