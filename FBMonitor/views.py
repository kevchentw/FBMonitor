from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime, timedelta
NOW = datetime.now()
WEEK = timedelta(days=7)
TODAY = datetime.strftime(NOW,"%Y/%m/%d")
LAST_WEEK = datetime.strftime(NOW-WEEK,"%Y/%m/%d")

def monitor(request):
    if request.method == "GET":
        d = {}
        f = {}
        f['order'] = request.GET.get('order', "time")
        f['total'] = request.GET.get('total', 10)
        f['likes'] = request.GET.get('likes', 0)
        f['comments'] = request.GET.get('comments', 0)
        f['shares'] = request.GET.get('shares', 0)
        f['until_datetime'] = request.GET.get('until_datetime', TODAY)
        f['since_datetime'] = request.GET.get('since_datetime', LAST_WEEK)
        d['filter'] = f
        return render(request, "monitor.html", d)
