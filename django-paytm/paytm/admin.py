# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin

from paytm.models import PaytmHistory


class PaytmHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'MID', 'TXNAMOUNT', 'STATUS')


admin.site.register(PaytmHistory, PaytmHistoryAdmin)
