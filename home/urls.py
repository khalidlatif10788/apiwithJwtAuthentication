# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from home import views
app_name = "home"
urlpatterns = [

    # The home page
    path('', views.index, name='ho'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
