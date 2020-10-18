from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from .models import Announce
from users.models import Engineers,Entrepreneur,Researchers,Academician,Doctors
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from PIL import Image

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted','document']
    paginate_by = 5
    def get_queryset(self):
      queryset = super(PostListView, self).get_queryset()
      return queryset.filter(moderation=True)


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView,FileSystemStorage):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/home'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
        
class PostCreateView(LoginRequiredMixin, CreateView,FileSystemStorage):
    model = Post
    fields = ['title', 'content','document']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AnnounceCreateView(LoginRequiredMixin, CreateView):
    model = Announce
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AnnounceListView(ListView):
    model = Announce
    template_name = 'blog/AnnounceListView.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'Announce'
    ordering = ['-date_posted']
    paginate_by = 5
    
    def get_queryset(self):
      queryset = super(AnnounceListView, self).get_queryset()
      return queryset.filter(moderation=True)


def home(request):
    return render(request, 'blog/home.html')

class EngineersListView(ListView):
    model = Engineers
    template_name = 'blog/about.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'Engineers'
    
    paginate_by = 5

class EntrepreneurListView(ListView):
    model = Entrepreneur
    template_name = 'blog/about1.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'Entrepreneur'
    
    paginate_by = 5

class AcademicianListView(ListView):
    model = Academician
    template_name = 'blog/about2.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'Academician'
    
    paginate_by = 5

class ResearchersListView(ListView):
    model = Researchers
    template_name = 'blog/about3.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'Researchers'
    
    paginate_by = 5

class DoctorsListView(ListView):
    model = Doctors
    template_name = 'blog/about4.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'Doctors'
    
    paginate_by = 5

def home1(request):
    return render(request, 'blog/home1.html')

def groups(request):
    return render(request, 'groups/group_list.html')

def profiles(request):
    return render(request,'blog/profiles.html',{'title':'profiles'})    


