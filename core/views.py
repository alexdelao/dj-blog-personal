from django.shortcuts import render
from django.views.generic.base import TemplateView

class AboutTemplateView(TemplateView):
    template_name = 'core/about.html'

# Create your views here.
# def about(request):
#     return render(request, 'core/about.html')