from django.urls import path, include

import views

urlpatterrs = [
    path("", views.past_list)
]