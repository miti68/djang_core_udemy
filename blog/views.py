from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from .models import PostModel

def post_model_detail_view(request, id=None):
    obj = get_object_or_404(PostModel, id=id)
    template = 'blog/detail_view.htm'
    context = {
        'object': obj
    }
    return render(request, template, context)

#@login_required(login_url='/login/')
def post_model_list_view(request):
    query_set = PostModel.objects.all() #return query set ~ a list
    template = 'blog/list_view.htm'
    context = {
        'object_list': query_set
    }
    return render(request, template, context)