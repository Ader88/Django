from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Author, Post
from .forms import PostForm, AuthorForm
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def posts_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)  # 5 postów na stronie
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    form = PostForm()
    if request.method == "POST":
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Dodano nowy Post!"
            )
            return redirect('posts_list')

    return render(request, 'posts_list.html', {'page_obj': page_obj, 'form': form})

def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_details.html', {'post': post})

def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'authors_list.html', {'authors': authors})

def author_details(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'author_details.html', {'author': author})

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts_list')
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authors_list')
    else:
        form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})