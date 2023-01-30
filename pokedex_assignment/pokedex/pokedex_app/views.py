from django.core.paginator import Paginator
from django.shortcuts import render

from . import db


def pokedex(request, page_number):
    page_size = request.GET.get('page_size', '10')
    # Get all pokemons from the DB
    pokemons = db.get()

    # Create a paginator object with a page size of 10
    paginator = Paginator(pokemons, page_size)

    # Get the current page of pokemons
    page_pokemons = paginator.get_page(page_number)

    # Render the pokedex template with the current page of pokemons
    return render(request, 'pokedex.html', {'pokemons': page_pokemons, 'page_size': page_size})

