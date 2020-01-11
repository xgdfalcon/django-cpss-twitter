#
# @license
# Copyright (c) 2020 XGDFalcon®. All Rights Reserved.
#
#
# XGDFalcon LLC retains all intellectual property rights to the code
# distributed as part of the Control Point System Software (CPSS) package.
# 

"""
This python module provides the models for the video vault application.

Written by Larry Latouf (xgdfalcon@gmail.com)
"""

from django.test import TestCase
from django.test.client import RequestFactory
from .models.client import TwitterClientOption
import os

CONSUMER_KEY = os.environ['CONSUMER_KEY'] 
CONSUMER_SECRET = os.environ['CONSUMER_SECRET'] 
ACCESS_TOKEN = os.environ['ACCESS_TOKEN'] 
ACCESS_SECRET = os.environ['ACCESS_SECRET'] 
USER_ID = os.environ['USER_ID'] 
CONTENT = "Testing django-cpss-twitter. https://github.com/xgdfalcon/django-cpss-twitter"

class TwitterDjangoTestCase(TestCase):
    def setUp(self):
        TwitterClientOption.objects.create(
            twitter_consumer_key=CONSUMER_KEY,
            twitter_consumer_secret=CONSUMER_SECRET,
            twitter_access_token=ACCESS_TOKEN,
            twitter_user_name=USER_ID,
            twitter_token_secret=ACCESS_SECRET)


    def test_post_status(self):
        collection = TwitterClientOption.objects.get(twitter_user_name=USER_ID)
        result = collection.post_status(CONTENT)
        print(result)

        
    def test_retrieve_timeline(self):
        collection = TwitterClientOption.objects.get(twitter_user_name=USER_ID)
        result = collection.get_user_timeline()
        print(result)
        
    # def test_get_timeline(self):
    #     rf = RequestFactory()
    #     get_request = rf.get('timeline/'+USER_ID)
    #     print(get_request)        

    # def test_post_update(self):
    #     rf = RequestFactory()
    #     request = rf.get('postupdate/'+USER_ID+'/'+CONTENT)
    #     print(request)
