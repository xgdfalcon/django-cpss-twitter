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

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models.client import TwitterClientOption

# @login_required
def get_timeline(request, username):
    option_instance = get_object_or_404(TwitterClientOption, twitter_user_name=username)
    return HttpResponse(option_instance.get_user_timeline())

# @login_required
def update_status(request, username):
    option_instance = get_object_or_404(TwitterClientOption, twitter_user_name=username)
    return HttpResponse(option_instance.update_status())

