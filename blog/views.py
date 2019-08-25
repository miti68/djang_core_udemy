from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import PostModel
from .forms import PostModelForm
from django.contrib import messages

def post_model_create_view(request):
    form = PostModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "Created a new blog post!")
        return HttpResponseRedirect("/blog/{num}".format(num=obj.id))
    context = {
        "form": form
    }
    template = 'blog/create_view.htm'
    return render(request, template, context)

def post_model_update_view(request, id=None):
    obj = get_object_or_404(PostModel, id=id)
    form = PostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "Updated blog post!")
        return HttpResponseRedirect("/blog/{num}".format(num=obj.id))
    context = {
        "object": obj,
        "form": form
    }
    template = 'blog/update_view.htm'
    return render(request, template, context)

def post_model_detail_view(request, id=None):
    obj = get_object_or_404(PostModel, id=id)
    template = 'blog/detail_view.htm'
    context = {
        'object': obj
    }
    return render(request, template, context)

def post_model_delete_view(request, id=None):
    obj = get_object_or_404(PostModel, id=id)
    if request.method == "POST":
        obj.delete()
        messages.success(request, "Delete post success")
        return HttpResponseRedirect("/blog/")
    template = 'blog/delete_view.htm'
    context = {
        'object': obj
    }
    return render(request, template, context)

#@login_required(login_url='/login/')
def post_model_list_view(request):
    query = request.GET.get("q",None)
    query_set = PostModel.objects.all() #return query set ~ a list
    if query is not None:
        query_set = query_set.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(slug__icontains=query) 
            )
    template = 'blog/list_view.htm'
    context = {
        'object_list': query_set
    }
    return render(request, template, context)

def post_model_robust_view(request, id=None):
    obj = None
    context = {}
    success_message = 'A new post was created'

    if id is None:
        template = 'blog/create_view/htm'
    else:
        obj = get_object_or_404(PostModel, id=id)
        success_message = 'Get Post'
        context["object"] = obj
        template = 'blog/detail_view/htm'
        if "edit" in request.get_full_path():
            template = 'blog/edit_view.htm'
        if "delete" in request.get_full_path():
            template = "blog/delete_view.htm"
            if request.method == "POST":
                obj.delete()
                messages.success(request, "Post deleted")
                return HttpResponseRedirect("/blog/") 

    form = PostModelForm(request.POST or None, instance=obj)
    context["form"] = form
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request,success_message)
        if obj is not None:
            return HttpResponseRedirect("/blog/{num}".format(num=obj.id))
        context["form"] = PostModelForm()

    return render(request, template, context)