from django.shortcuts import render
from .models import Portfolio
from django.views.generic import ListView


class PortfolioListView(ListView):
    model = Portfolio
    template_name = 'portfolio/portfolio.html'
    context_object_name = 'portfolio'
    paginate_by = 10