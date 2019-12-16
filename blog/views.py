from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

class HomeListView(ListView):
    model = Post
    paginate_by = 10

class PostDeatilView(DetailView):
    model = Post
    template_name ='blog/post.html'


###############################CRUD
@method_decorator(staff_member_required, name='dispatch')
class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('home')

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('home')

class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse_lazy('update', args=[self.object.slug]) +'?ok'
    


