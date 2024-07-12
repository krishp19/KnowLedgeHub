from django.shortcuts import render, get_object_or_404
from .models import Post,Comment,Blogs
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# Create your views here.

def LikeView(request,pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)])) 


class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetailViews(DetailView):
    model = Post
    template_name = 'article_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailViews, self).get_context_data()
        
        stuff = get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
    
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context
    

class AddpostView(CreateView):
    model=Post
    # form_class = PostForm
    template_name = 'add.html'
    fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update.html'
    fields = ['title' , 'body' ]

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

class AddcommentView(CreateView):
    model= Comment
    template_name = 'comment.html'
    fields = '__all__'

class BlogView(ListView):
    model = Blogs
    template_name = 'blog.html'

class BlogDetailViews(DetailView):
    model = Post
    template_name = 'blog_detail.html'