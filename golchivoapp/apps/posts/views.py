from urllib.parse import quote_plus

from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, Http404
from .models import Post
from .forms import PostForm
# Create your views here.


def post_list(request):
    queryset_list = Post.objects.all().order_by("-timestamp")
    paginator = Paginator(queryset_list, 4)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "post":queryset,
        "template_title":"post list"
    }
    return render(request,'posts/post_list.html',context)


def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'template_title':'Crear nueva noticia',
        'form':form,
        'btn_name':'Crear post'
    }
    return render(request,"posts/post_form.html",context)


def post_detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    share_string = quote_plus(instance.content)
    context = {
        "template_title":"Post detail",
        "instance":instance,
        "share_string":share_string
    }
    return render(request,"posts/post_detail.html",context)


def post_update(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "template_title": "Editar noticia",
        "form": form,
        'btn_name':'Editar post'
    }
    return render(request,"posts/post_form.html",context)


def post_delete(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    return redirect("posts:list")