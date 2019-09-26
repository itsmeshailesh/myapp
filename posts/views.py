from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.

def post_create(request):
    return HttpResponse("<h1>Create</h1>")
def post_detail(request):
    return HttpResponse("<h1>detail</h1>")
def post_list(request):
	context={}
	return render(request,'index.html',context)
def post_update(request):
    return HttpResponse("<h1>update</h1>")
def post_delete(request):
    return HttpResponse("<h1>delete</h1>")