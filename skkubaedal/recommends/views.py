from django.shortcuts import render
import restaurant


# Create your views here.
def show_restaurant(request):
    render(request, "./templates/restaurant.html", {"rest_list": Flist})
