from django.shortcuts import render

# Create your views here.

def twitter_login(req):
    return render(req, "twitter_login.html")
