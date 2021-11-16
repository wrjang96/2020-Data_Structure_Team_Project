from django.urls import path
from recommends import views


urlpatterns = [path("rest/", views.show_restaurant, name="rest")]
