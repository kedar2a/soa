from django.http import HttpResponse
from django.template import loader


def home_slider(request):
    template = loader.get_template('idols/home-slider.html')
    context = {
        'test': 'test',
    }
    return HttpResponse(template.render(context, request))


def gallery(request):

    from idols.models import MurtiCategory

    all_murti_category = MurtiCategory.objects.all()
    template = loader.get_template('idols/gallery.html')
    context = {
        'all_murti_category': all_murti_category,
        'url_name': 'murti_category'
    }
    return HttpResponse(template.render(context, request))


def murti_category(request, murti_category_code):

    from idols.models import MurtiCategory, Murti

    template = loader.get_template('idols/gallery.html')
    murti_category_obj = MurtiCategory.objects.get(category_code=murti_category_code)
    all_category_murtis = Murti.objects.filter(category_id=murti_category_obj.id)

    context = {
        'all_murti_category': all_category_murtis,
        'url_name': 'murti_detail'
    }
    return HttpResponse(template.render(context, request))


def murti_detail(request, murti_category_code, m_id):

    from idols.models import Murti

    template = loader.get_template('idols/murti-detail.html')
    murti_obj = Murti.objects.get(id=m_id)

    context = {
        'murti': murti_obj,
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

