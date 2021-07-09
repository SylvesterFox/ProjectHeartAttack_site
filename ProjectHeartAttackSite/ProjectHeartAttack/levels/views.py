from django.shortcuts import render
from django.http import HttpResponse

from .models import Levels

def index(request):
    levels_list = Levels.objects.all()
    _context = {
        'levels': levels_list, 
        'title': 'ProjectHeartAttack' 
        }
    return render(request, template_name="levels/index.html", context=_context)

def get_level(request, levels_id):
    level = Levels.objects.get(pk=levels_id)
    _context = {
        'levels': level, 
        'title': f'Level Info|{level.name_level}' 
        }
    return render(request, template_name='levels/lavelinfo.html', context=_context)