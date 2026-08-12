from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'members': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, member_id):
    try:
        member = Member.objects.get(id=member_id)
    except Member.DoesNotExist:
        return HttpResponse("Member not found", status=404)

    template = loader.get_template('details.html')
    context = {
        'member': member,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render({}, request))

