from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Superhero

#  Create your views here.
def index(request):
    all_heroes = Superhero.objects.all()
    context = {
        'all_heroes': all_heroes
    }
    return render(request, 'superheroes/index.html', context)

def detail(request, hero_id):
    single_hero = Superhero.objects.get(pk=hero_id)
    context = {
        'single_hero': single_hero
    }
    return render(request, 'superheroes/detail.html', context)

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary = request.POST.get('primary')
        secondary = request.POST.get('secondary')
        catchphrase = request.POST.get('catchphrase')
        new_hero = Superhero(name=name, alter_ego=alter_ego, primary_ability= primary, secondary_ability=secondary, catch_phrase=catchphrase)
        new_hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:    
        return render(request, 'superheroes/create.html') 

def edit(request, hero_id):
    hero_from_db = Superhero.objects.get(pk=hero_id)
    context = {
        'single_hero': hero_from_db
    }
    
    if request.method == "POST":
        name_from_form = request.POST.get('name')
        alter_ego_from_form = request.POST.get('alter_ego')
        primary_from_form = request.POST.get('primary')
        secondary_from_form = request.POST.get('secondary')
        catchphrase_from_form = request.POST.get('catchphrase')
        hero_edit = Superhero(name=name_from_form, alter_ego=alter_ego_from_form, primary_ability= primary_from_form, secondary_ability=secondary_from_form, catch_phrase=catchphrase_from_form)
        hero_edit.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:    
        return render(request, 'superheroes/edit.html') 