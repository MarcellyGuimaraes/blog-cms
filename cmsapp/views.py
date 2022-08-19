from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.utils.text import slugify
from django.contrib import messages

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'cmsapp/index.html', context)

def detail(request, slug):
    post = Post.objects.get(slug=slug)
    posts = Post.objects.exclude(post_id__exact=post.post_id)[:5]
    context = {'post': post, 'posts': posts}
    return render(request, 'cmsapp/detail.html', context)

def createPost(request):
    perfil = request.user.userprofile
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid:
            post = form.save(commit=False)
            post.slug = slugify(post.titulo)
            post.escritor = perfil
            post.save()
            messages.info(request, 'Artigo criado com sucesso')
            return redirect('create')
        else:
            messages.error(request, 'Artigo não foi criado :(')
    context = {'form': form}
    return render(request, 'cmsapp/create.html', context)

def updatePost(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.info(request, 'Artigo atualizado com sucesso')
            return redirect('detail', slug=post.slug)
    context = {'form': form}
    return render(request, 'cmsapp/create.html', context)

def deletePost(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)
    if request.method == 'POST':
        post.delete()
        messages.info(request, 'Artigo deletado com sucesso')
        return redirect('create')
    context = {'form': form}
    return render(request, 'cmsapp/delete.html', context)