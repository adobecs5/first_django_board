from django.shortcuts import render
from list_posts.models import Post
from django.http import HttpResponseRedirect as HRR
from pprint import pprint

def basic_view(request):
    return render(request, "write_article.html")

def handle_article(request):
    if request.method == "POST":
        pprint(vars(request))
        post = Post()
        post.contents = request.POST.get("content")
        post.title = request.POST.get("title")
        post.writer = request.POST.get("writer")
        post.save()
        pprint (vars(post))
        redir = "/posts/%d" % post.postNum
        print(redir)
        return HRR(redir)
    else:
        raise Exception ("handle_article", request)
