from django.urls import path
from login import views

urlpatterns = [
    path("join/", views.signup, name="join"),
    path("login/", views.signin, name="login"),
    path("", views.firstpage, name="firstpage"),
    path("index/", views.index, name="index"),
    path("index/map", views.map, name="map"),
    path("index/back", views.back, name="back"),

    path("index/shoplist/", views.shop_list, name="shoplist"),
    path("index/shoplist/<int:pk>/", views.shopdetail, name="shopdetail"),
    path("index/recommendmain/", views.recommendmain, name="recommendmain"),
    path("index/recommendmain/index", views.back, name="back"),
    path("index/recommendmain/Kor1/", views.Kor1, name="Kor1"),
    path("index/recommendmain/Kor1/Jap_1", views.Jap_1, name="Jap_1"),
    path(
        "index/recommendmain/Kor1/Kor_criteria", views.Kor_criteria, name="Kor_criteira"
    ),
    path(
        "index/recommendmain/Kor1/Kor_distance", views.Kor_distance, name="Kor_distance"
    ),
    path("index/recommendmain/Kor1/Kor_review", views.Kor_review, name="Kor_review"),
    path(
        "index/recommendmain/Kor1/Kor_distance_sidedoor",
        views.Kor_distance_sidedoor,
        name="Kor_distance_sidedoor",
    ),
    path(
        "index/recommendmain/Kor1/Kor_distance_maingate",
        views.Kor_distance_maingate,
        name="Kor_distance_maingate",
    ),
    path(
        "index/recommendmain/Kor1/Jap_criteria", views.Jap_criteria, name="Jap_criteria"
    ),
    path(
        "index/recommendmain/Kor1/Jap_distance", views.Jap_distance, name="Jap_distance"
    ),
    path("index/recommendmain/Kor1/Jap_review", views.Jap_review, name="Jap_review"),
    path(
        "index/recommendmain/Kor1/Jap_distance_sidedoor",
        views.Jap_distance_sidedoor,
        name="Jap_distance_sidedoor",
    ),
    path(
        "index/recommendmain/Kor1/Jap_distance_maingate",
        views.Jap_distance_maingate,
        name="Jap_distance_maingate",
    ),
    path("index/recommendmain/Kor1/Chi_1", views.Chi_1, name="Chi_1"),
    path(
        "index/recommendmain/Kor1/Chi_criteria", views.Chi_criteria, name="Chi_criteria"
    ),
    path("index/recommendmain/Kor1/Wes_1", views.Wes_1, name="Wes_1"),
    path(
        "index/recommendmain/Kor1/Chi_distance", views.Chi_distance, name="Chi_distance"
    ),
    path("index/recommendmain/Kor1/Chi_review", views.Chi_review, name="Chi_review"),
    path(
        "index/recommendmain/Kor1/Chi_distance_sidedoor",
        views.Chi_distance_sidedoor,
        name="Chi_distance_sidedoor",
    ),
    path(
        "index/recommendmain/Kor1/Chi_distance_maingate",
        views.Chi_distance_maingate,
        name="Chi_distance_maingate",
    ),
    path(
        "index/recommendmain/Kor1/Wes_criteria", views.Wes_criteria, name="Wes_criteria"
    ),
    path("index/recommendmain/Kor1/Flour_1", views.Flour_1, name="Flour_1"),
    path(
        "index/recommendmain/Kor1/Wes_distance", views.Wes_distance, name="Wes_distance"
    ),
    path("index/recommendmain/Kor1/Wes_review", views.Wes_review, name="Wes_review"),
    path(
        "index/recommendmain/Kor1/Wes_distance_sidedoor",
        views.Wes_distance_sidedoor,
        name="Wes_distance_sidedoor",
    ),
    path(
        "index/recommendmain/Kor1/Wes_distance_maingate",
        views.Wes_distance_maingate,
        name="Wes_distance_maingate",
    ),
    path("index/recommendmain/Kor1/redirect1", views.redirect1, name="redirect1"),
    path(
        "index/recommendmain/Kor1/Flour_criteria",
        views.Flour_criteria,
        name="Flour_criteria",
    ),
    path(
        "index/recommendmain/Kor1/Flour_distance",
        views.Flour_distance,
        name="Flour_distance",
    ),
    path(
        "index/recommendmain/Kor1/Flour_review", views.Flour_review, name="Flour_review"
    ),
    path("index/recommendmain/Kor1/redirect1", views.redirect1, name="redirect1"),
    path(
        "index/recommendmain/Kor1/Flour_distance_sidedoor",
        views.Flour_distance_sidedoor,
        name="Flour_distance_sidedoor",
    ),
    path(
        "index/recommendmain/Kor1/Flour_distance_maingate",
        views.Flour_distance_maingate,
        name="Flour_distance_maingate",
    ),
    path("index/recommendmain/Kor1/back", views.back, name="back"),
]
