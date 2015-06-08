from django.shortcuts import render
from FBMonitor.myfacebook import Facebook

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
