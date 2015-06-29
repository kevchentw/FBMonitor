from django.shortcuts import render, redirect
from FBMonitor.myfacebook import Facebook
from FBData.models import FBData
from django.http import HttpResponse

def post_view(request):
    if request.method == "GET":
        return render(request, "post.html")

def monitor(request):
    if request.method == "GET":
        d = {}
        page = request.GET.get('page', '209251989898')
        limit = request.GET.get('limit', '5')
        f = Facebook()
        d['feed'] = f.get_feed_id(f.get_feed(page, limit))
        d['feed_data'] = f.get_feed(page, limit)
        return render(request, "monitor.html", d)

def monitor_all(request):
    if request.method == "GET":
        order = request.GET.get('order', "time")
        total = request.GET.get('total', 10)
        likes = request.GET.get('likes', 0)
        comments = request.GET.get('comments', 0)
        shares = request.GET.get('shares', 0)
        if not total:
            total = 0
        if not likes:
            likes = 0
        if not comments:
            comments = 0
        if not shares:
            shares = 0
        try:
            total = int(total)
            likes = int(likes)
            comments = int(comments)
        except:
            total = 0
            likes = 0
            comments = 0
        form = {"order": order, "total": total, "likes": likes, "comments": comments, "shares": shares}
        d = {}
        feed = FBData.objects.filter(likes__gte=likes, comments__gte=comments, shares__gte=shares).order_by("-"+order)[:total]
        # feed = feed.extra(order_by=[order])
        d['feed'] = feed
        d['form'] = form
        return render(request, "monito_all.html", d)


def update(request):
    if request.method == "GET":
        f = Facebook()
        f.get_all_summary()	
        return redirect("/monitor_all/")
