from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Book
from .forms import PostForm

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    books = Book.objects.all()
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
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})