from django.shortcuts import render
from .models import Post
from django.views import generic

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-updated_on')
    template_name = 'post_list.html'
    
class DetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

# def blog(request):
    
#     return render(request, 'blog.html')
