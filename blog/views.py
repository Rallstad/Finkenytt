from django.views import generic
from .models import Post, About, Contact, Finches


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


class About(generic.ListView):
    model = About
    template_name = 'about.html'


class Contact(generic.ListView):
    model = Contact
    template_name = 'contact.html'


class Finches(generic.ListView):
    model = Finches
    template_name = 'finches.html'
