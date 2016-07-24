from django.http import HttpResponse
from django.template import loader


def home_slider(request):
    template = loader.get_template('idols/home-slider.html')
    context = {
        'test': 'test',
    }
    return HttpResponse(template.render(context, request))


def gallery(request):
    template = loader.get_template('idols/gallery.html')
    context = {
        'test': 'test',
    }
    return HttpResponse(template.render(context, request))


def aim(request):
    template = loader.get_template('idols/aim.html')
    context = {
        'test': 'test',
    }
    return HttpResponse(template.render(context, request))    


def media(request):
    template = loader.get_template('idols/media.html')
    context = {
        'test': 'test',
    }
    return HttpResponse(template.render(context, request))


def team(request):
    template = loader.get_template('idols/team.html')
    context = {
        'test': 'test',
    }
    return HttpResponse(template.render(context, request))


def contact(request):
    template = loader.get_template('idols/contact.html')
    context = {
        'test': 'test',
    }
    return HttpResponse(template.render(context, request))