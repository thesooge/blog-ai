from django.urls import reverse, reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .models import Post , Comment
from .forms import CommentForm
# Create your views here.

class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 3


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.filter(active=True)
        context['comment_form'] = CommentForm()
        return context


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'slug', 'body']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'slug', 'body']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    
class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')


class PostComments(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        # Get the related post by primary key (from the URL)
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        
        # Assign the post to the comment
        comment = form.save(commit=False)
        comment.post = post

        # Assign the logged-in user as the author
        comment.author = self.request.user

        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'slug': self.object.post.slug})    
    
    
    
    
    
    
    
    
    
    