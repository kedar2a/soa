from django.http import HttpResponse
from django.template import loader

from idols.models import MurtiCategory, Murti


def home_slider(request):
    template = loader.get_template('idols/home-slider.html')
    context = {}
    return HttpResponse(template.render(context, request))


def gallery(request):
    all_murti_category = MurtiCategory.objects.all()
    template = loader.get_template('idols/gallery.html')
    context = {
        'title': 'Gallery',
        'all_murti_category': all_murti_category,
        'url_name': 'murti_category'
    }
    return HttpResponse(template.render(context, request))


def murti_category(request, murti_category_code):


    template = loader.get_template('idols/gallery.html')
    murti_category_obj = MurtiCategory.objects.get(category_code=murti_category_code)
    all_category_murtis = Murti.objects.filter(category_id=murti_category_obj.id)

    context = {
        'all_murti_category': all_category_murtis,
        'url_name': 'murti_detail'
    }
    return HttpResponse(template.render(context, request))


def murti_detail(request, murti_category_code, m_id):


    template = loader.get_template('idols/murti-detail.html')
    murti_obj = Murti.objects.get(id=m_id)

    context = {
        'murti': murti_obj,
    }
    return HttpResponse(template.render(context, request))


def aim(request):
    template = loader.get_template('idols/aim.html')
    context = {
        'title': 'Aim',
    }
    return HttpResponse(template.render(context, request))    


def media(request):
    template = loader.get_template('idols/media.html')
    context = {
        'title': 'Media'
    }
    return HttpResponse(template.render(context, request))


def team(request):
    template = loader.get_template('idols/team.html')
    context = {
        'title': 'Team',
    }
    return HttpResponse(template.render(context, request))


def contact(request):
    template = loader.get_template('idols/contact.html')
    context = {
        'title': 'Contact',
    }
    return HttpResponse(template.render(context, request))

