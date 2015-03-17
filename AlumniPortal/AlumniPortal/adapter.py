__author__ = 'Prateek'

from allauth.account.adapter import DefaultAccountAdapter
from settings_dev import LOGIN_REDIRECT_URL, LINKEDIN_LINK_URL
from django.shortcuts import resolve_url
from datetime import datetime, timedelta

class AccountAdapter(DefaultAccountAdapter):

    # Ensure that user is redirected to SIGN-UP/LinkedIn linkup page on his first login.
    def get_login_redirect_url(self, request):
        threshold = 30 #seconds

        if (request.user.last_login - request.user.created_at).seconds < threshold:
            url = LINKEDIN_LINK_URL
        else:
            url = LOGIN_REDIRECT_URL
        return resolve_url(url)