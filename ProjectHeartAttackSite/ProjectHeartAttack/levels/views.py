from django.core import paginator
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

from .models import Levels

def index(request):
    levels_list = Levels.objects.all()
    paginator = Paginator(levels_list, 25) # levels_list <- пердеём список уровней из базы, num - сколоко уровней будет занимать одна страница, default max 25.

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''


    _context = {
        'levels': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url,
        'title': 'ProjectHeartAttack',
        }
    return render(request, template_name="levels/index.html", context=_context)

def get_level(request, levels_id):
    level = Levels.objects.get(pk=levels_id)
    _context = {
        'levels': level, 
        'title': f'Level Info|{level.name_level}' 
        }
    return render(request, template_name='levels/lavelinfo.html', context=_context)

def toplevels(request):
    order_levels_rating = Levels.objects.all().order_by('-rating')
    paginator = Paginator(order_levels_rating, 25) 

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    _context_toplevels = {
        'levels': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url,
        'title': 'ProjectHeartAttack| Top Levels',
    }

    return render(request, template_name='levels/index.html', context=_context_toplevels)
