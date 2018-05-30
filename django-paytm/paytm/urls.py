# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'paytm.views.home', name='home'),
    url(r'^payment/', 'paytm.views.payment', name='payment'),
    url(r'^response/', 'paytm.views.response', name='response'),
]
