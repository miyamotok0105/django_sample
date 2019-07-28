from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
#modelとviewを密結合にしないで、リポジトリを経由する。
from .models import PostData, BookData
from blog.domain.entities.post import Post
from blog.domain.repositories.post_repository import PostRepository

from .forms import PostForm

def post_list(request):
    post = PostRepository()
    posts = post.all()
    books = BookData.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts, 'books': books})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            post.author = ""
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(PostData, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})