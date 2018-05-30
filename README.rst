============
Django-Paytm
============

Django-Paytm is an application to integrate paytm gateway with your django project.

Forked from here: [paytm-django](https://github.com/harishbisht/paytm-django)

Installation
-----------

You can install Django-paytm using pip.

    `pip install django-paytm`

Quick start
-----------

1. Add "paytm" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'paytm',
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r'^paytm/', include('paytm.urls')),

3. Put below variables into your settings file.

    PAYTM_MERCHANT_KEY=  "<YOUR-PAYTM-MERCHANT-KEY>"

    PAYTM_MERCHANT_ID = "<YOUR-PAYTM-MERCHANT-ID>"

    PAYTM_CALLBACK_URL = "http://localhost:8000/response/"

4. Migrate and create paytm models.

    python manage.py migrate

5. Paytm reference APIs and SDK:

    [PAYTM API DOCUMENTATION](http://paywithpaytm.com/developer/paytm_api_doc/)
    [SDK DOCUMENTATION](http://paywithpaytm.com/developer/paytm_sdk_doc/)
