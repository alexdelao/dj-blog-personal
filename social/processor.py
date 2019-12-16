from .models import Link
import datetime

def ctx_dict(request):
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx

def ctx_year(request):
    dt = datetime.datetime.now()
    return {'year':dt.year}