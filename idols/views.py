from django.http import HttpResponse
from django.template import loader

from idols.models import MurtiCategory, Murti
from SOA_Project.settings import MURTI_YEAR
from django.views.decorators.cache import cache_page

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer
# from .serializers import GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer


def home_slider(request):
    template = loader.get_template('idols/home-slider.html')
    context = {
        'title': 'Home',
    }
    return HttpResponse(template.render(context, request))


def feature(request):
    template = loader.get_template('idols/feature.html')
    context = {
        'title': 'Feature',
    }
    return HttpResponse(template.render(context, request))    

@cache_page(60 * 60 * 12)
def gallery(request):
    all_murti_category = MurtiCategory.objects.all().order_by('murti_category_name')
    template = loader.get_template('idols/gallery.html')
    context = {
        'title': 'Gallery',
        'all_murti_category': all_murti_category,
        'url_name': 'murti_category'
    }
    return HttpResponse(template.render(context, request))


@cache_page(60 * 60 * 12)
def murti_category(request, murti_category_code):

    template = loader.get_template('idols/gallery.html')
    murti_category_obj = MurtiCategory.objects.get(category_code=murti_category_code)
    all_category_murtis = Murti.objects.filter(category_id=murti_category_obj.id, year=MURTI_YEAR)

    context = {
        'title': 'Gallery',
        'all_murti_category': all_category_murtis,
        'url_name': 'murti_detail'
    }
    return HttpResponse(template.render(context, request))


def murti_detail(request, murti_category_code, m_id):
    template = loader.get_template('idols/murti-detail.html')
    murti_obj = Murti.objects.get(id=m_id)

    context = {
        'title': 'Gallery',
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

