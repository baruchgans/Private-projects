from django.core.cache import cache
from django.core.paginator import PageNotAnInteger, EmptyPage
from django.core.paginator import Paginator
from django.shortcuts import render

from . import db


def pokedex(request, page_number):
    page_size = int(request.GET.get('page_size', '10'))
    sort_direction = request.GET.get('sort_direction', 'asc')
    filter_term = request.GET.get('filter_term', '')

    # Try to get the pokemons from cache
    cache_key = f"pokemons_{page_size}_{sort_direction}_{filter_term}"
    pokemons = cache.get(cache_key)

    # If the pokemons are not in cache, get them from the database
    if pokemons is None:
        # Get all pokemons from the DB
        pokemons = db.get()

        # Filter the pokemons based on the filter term
        if filter_term:
            pokemons = [pokemon for pokemon in pokemons if filter_term in pokemon['type_one'].lower()]

        if sort_direction == 'desc':
            pokemons = sorted(pokemons, key=lambda x: x['number'], reverse=True)
        else:
            pokemons = sorted(pokemons, key=lambda x: x['number'])

        # Store the pokemons in cache for 5 minutes
        cache.set(cache_key, pokemons, 300)

    # Create a paginator object with the selected page size
    paginator = Paginator(pokemons, page_size)

    try:
        # Get the current page of pokemons
        page_pokemons = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page_pokemons = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page_pokemons = paginator.page(paginator.num_pages)

    return render(request, 'pokedex.html',
                  {'pokemons': page_pokemons, 'page_size': page_size, 'filter_term': filter_term,
                   'sort_direction': sort_direction})
