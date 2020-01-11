#
# @license
# Copyright (c) 2020 XGDFalcon®. All Rights Reserved.
#
#
# XGDFalcon LLC retains all intellectual property rights to the code
# distributed as part of the Control Point System Software (CPSS) package.
#

"""
This python module provides...

Written by Larry Latouf (xgdfalcon@gmail.com)
"""

from twitter import *
from django.conf import settings
from django.contrib.sites.models import Site
from django.utils.translation import gettext as _
from django.db import models
from django.http import HttpRequest, HttpResponse
from twitter import Twitter
import uuid


class TwitterClientManager(models.Manager):
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class TwitterClientType(models.Model):
    id = models.UUIDField(verbose_name=_("ID"), primary_key=True,
                          default=uuid.uuid4, editable=False)
    twitter_consumer_key = models.CharField(
        verbose_name=_("Twitter API Key"), max_length=100, default="")
    twitter_consumer_secret = models.CharField(
        verbose_name=_("Twitter API Secret"), max_length=100, default="")
    twitter_access_token = models.CharField(
        verbose_name=_("Twitter Acdess Token"), max_length=100, default="")
    twitter_token_secret = models.CharField(
        verbose_name=_("Twitter Token Secret"), max_length=100, default="")
    twitter_user_name = models.CharField(
        verbose_name=_("Twitter User Name"), unique=True, max_length=100, default="")
    site = models.ForeignKey(
        Site, on_delete=models.CASCADE, null=True, verbose_name=_('Site'), blank=True)

    class Meta:
        abstract = True


class TwitterClientOption(TwitterClientType):
    objects = TwitterClientManager()

    class Meta:
        db_table = 'cpss_twitter_settings'
        verbose_name = _('CPSS Twitter Client Setting')
        verbose_name_plural = _('CPSS Twitter Client Settings')

    def __str__(self):
        return str(self.site.domain) + ": " + str(self.twitter_user_name)

    def get_user_timeline(self):
        t = Twitter(
            auth=OAuth(self.twitter_access_token, self.twitter_token_secret, self.twitter_consumer_key, self.twitter_consumer_secret))

        result = t.statuses.user_timeline(screen_name=self.twitter_user_name, count=10)

        return result

    def post_status(self, status_content):
        t = Twitter(
            auth=OAuth(self.twitter_access_token, self.twitter_token_secret, self.twitter_consumer_key, self.twitter_consumer_secret))

        result = t.statuses.update(status=status_content)

        return result
