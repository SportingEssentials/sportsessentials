from django.shortcuts import render
from .models import BasketballEssential, SoccerEssential


def home(request):
    basketball_essentials = BasketballEssential.objects.all()
    soccer_essentials = SoccerEssential.objects.all()
    
    # Calculate the number of stars for each basketball essential
    for essential in basketball_essentials:
        num_full_stars = int(essential.stars)
        num_half_stars = round((essential.stars - num_full_stars) * 2)
        essential.num_stars = '★' * num_full_stars + '½' * num_half_stars + '☆' * (5 - num_full_stars - num_half_stars)
    
    context = {
        'basketball_essentials': basketball_essentials,
        'soccer_essentials': soccer_essentials,
    }
    return render(request, 'home.html', context)

