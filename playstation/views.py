from re import template
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import prem 
from django.urls import reverse
def msg(request):
    Prem = prem.objects.all().values()
    template = loader.get_template("myfirst.html")
    context = {
        'prem':Prem,
    }
    return HttpResponse(template.render(context,request))

def add(request):
    template = loader.get_template("add.html")
    return HttpResponse(template.render({},request))

def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  member = prem(firstname=x, lastname=y)
  member.save()
  return HttpResponseRedirect(reverse('msg'))

def delete(request,id):
    member = prem.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('msg'))

def update(request, id):
  Prem = prem.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'prem': Prem,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  member = prem.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  member.save()
  return HttpResponseRedirect(reverse('msg'))

def testing(request):
    Prem = prem.objects.all().values()
    template = loader.get_template('template.html')
    context = {
    'prem': Prem,
  }
    return HttpResponse(template.render(context, request))

  