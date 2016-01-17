from django.shortcuts import render
from list_posts.models import Post, Comment
from django.http import HttpResponseRedirect as HRR
from pprint import pprint
# Create your views here.

def list_posts(request):
    # need to get only 5 posts from the db
    posts = Post.objects.all()
    # now render the posts
    return render(request, 'post_listing.html', { "post1": posts[0], "post2":posts[1], "list": posts })

def give_post_tag(request):
    posts = Post.objects.all()
    posts = posts[:5]
    return render(request, 'post_listing_with_post_tag.html', {"list":posts})

def show_a_post(request, postnum):
    print postnum
    post = Post.objects.filter(postNum=postnum)
    post = post[0]
    comments = post.comments.all()
    temp = []
    for comment in comments:
        temp.append(comment.contents)
    return render(request, 'show_a_post.html', {"post" : post, "comments" : temp})

def handle_comment(request):
    if request.method == 'POST':
        print (request.POST)
        #postNum = request.POST.get('postNum')
        redirect = "/posts/%s" % request.POST.get('postNum')
        comment = Comment()
        comment.postNum = request.POST.get('postNum')
        comment.post_id = comment.postNum
        comment.commentNum = 1
        comment.writer = "ME"
        comment.contents = request.POST.get('comment')
        pprint(vars(comment))
        comment.save()
        print("successfully saved")
        return HRR(redirect)
    else:
        raise Exception("handle_comment exception", request)
    
