from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Superhero

# CRUD: Create Read Update Delete
# READ: List view, Detail View

def hero_list(request):
    all_heroes = Superhero.objects.all()
    context = {'all_heroes': all_heroes}
    return render(request, 'superheroes/hero_list.html', context)


def hero_detail(request, hero_id):
    hero = Superhero.objects.get(id=hero_id)
    context = {'hero': hero}
    return render(request, 'superheroes/hero_detail.html', context)


def hero_create(request):
 


    if request.method == "POST":
        name = request.POST.get('name')
        image = request.FILES.get('image')
        alter_ego = request.POST.get('alter_ego')
        primary_ability = request.POST.get('primary_ability')
        secondary_ability = request.POST.get('secondary_ability')
        catch_phrase = request.POST.get('catch_phrase')
        new_hero = Superhero(
            name=name,
            image=image, 
            alter_ego=alter_ego, 
            primary_ability=primary_ability, 
            secondary_ability=secondary_ability, 
            catch_phrase=catch_phrase)
        new_hero.save()
        return redirect('superheroes:hero_list')
    return render(request, 'superheroes/hero_create.html') 


def hero_edit(request, hero_id):
    hero = Superhero.objects.get(id=hero_id)

    print(
    f'GET Data: {request.GET}',
    f'POST Data: {request.POST}', 
    f'FILES Data: {request.FILES}',
    sep='\n')

    if request.method == "POST":
        hero.name = request.POST.get('name')
        image = request.FILES.get('image')
        hero.image = image if image else hero.image
        hero.alter_ego = request.POST.get('alter_ego')
        hero.primary_ability = request.POST.get('primary_ability')
        hero.secondary_ability = request.POST.get('secondary_ability')
        hero.catch_phrase = request.POST.get('catch_phrase')
        hero.save()
        return redirect('superheroes:hero_list')

    context = {'hero': hero}
    return render(request, 'superheroes/hero_edit.html', context) 


def hero_delete(request, hero_id):
    hero = Superhero.objects.get(id=hero_id)
    hero.delete()
    return redirect('superheroes:hero_list')