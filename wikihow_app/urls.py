from django.urls import path
from . import views

urlpatterns=[
    path("dockertest", views.firstTest),
    path("dbtest", views.PersonList.as_view()),
    path("search", views.searchWikihow),
]