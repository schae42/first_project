from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('blogs', views.index),
    path('blogs/new', views.new),
    path('blogs/create', views.create),
    path('blogs/<num>', views.show),
    path('blogs/<num>/edit', views.edit),
    path('blogs/<num>/destroy', views.destroy)
]

# @app.route('/')
# def hello_world():
    # return "stringy string"

# MVC                                               MTV

# Models            - Database                      Models
# Views (HTML/files/front end)            - User sees/Templates           Template
# Controllers (Functions that we run)       - Server Logic                  Views      