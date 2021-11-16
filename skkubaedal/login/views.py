from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import UserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template import RequestContext
from .models import Post


# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect("/")
        else:
            return HttpResponse("Duplicate membership information.")
    else:
        form = UserForm()
        return render(request, "adduser.html", {"form": form})


def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/index")
        else:
            return HttpResponse("Login failed. Try again.")
    else:
        form = LoginForm()
        return render(request, "login.html", {"form": form})


def firstpage(request):
    return render(request, "firstpage.html")


def index(request):
    return render(request, "index.html")


def map(request):
    return render(request, "map.html")


def shop_list(request):
    lists = Post.objects.all()
    return render(request, "shoplist.html", {"lists": lists})


def shopdetail(request, pk):
    lists = get_object_or_404(Post, pk=pk)
    return render(request, "shopdetail.html", {"lists": lists})


def recommendmain(request):
    return render(request, "recommendmain.html")


def back(request):
    return redirect("/index")


def Kor1(request):
    return render(request, "Kor1.html")


def Jap_1(request):
    return render(request, "Jap_1.html")


def Kor_criteria(request):
    return render(request, "Kor_criteria.html")


def Kor_review(request):
    lists = Post.objects.filter(foodtype="한식").order_by("-score")
    return render(request, "Kor_review.html", {"lists": lists})


def Kor_distance(request):
    return render(request, "Kor_distance.html")


def Kor_distance_sidedoor(request):
    lists = Post.objects.filter(foodtype="한식", location="쪽문")
    return render(request, "Kor_distance_sidedoor.html", {"lists": lists})


def Kor_distance_maingate(request):
    lists = Post.objects.filter(foodtype="한식", location="정문 || 철문")
    return render(request, "Kor_distance_maingate.html", {"lists": lists})


def Jap_criteria(request):
    return render(request, "Jap_criteria.html")


def Jap_distance(request):
    return render(request, "Jap_distance.html")


def Jap_review(request):
    lists = Post.objects.filter(foodtype="일식").order_by("-score")
    return render(request, "Jap_review.html", {"lists": lists})


def Jap_distance_sidedoor(request):
    lists = Post.objects.filter(foodtype="일식", location="쪽문")
    return render(request, "Jap_distance_sidedoor.html", {"lists": lists})


def Jap_distance_maingate(request):
    lists = Post.objects.filter(foodtype="일식", location="정문 || 철문")
    return render(request, "Jap_distance_maingate.html", {"lists": lists})


def Chi_1(request):
    return render(request, "Chi_1.html")


def Chi_criteria(request):
    return render(request, "Chi_criteria.html")


def Wes_1(request):
    return render(request, "Wes_1.html")


def Chi_distance(request):
    return render(request, "Chi_distance.html")


def Chi_review(request):
    lists = Post.objects.filter(foodtype="중식").order_by("-score")
    return render(request, "Chi_review.html", {"lists": lists})


def Chi_distance_sidedoor(request):
    lists = Post.objects.filter(foodtype="중식", location="쪽문")
    return render(request, "Chi_distance_sidedoor.html", {"lists": lists})


def Chi_distance_maingate(request):
    lists = Post.objects.filter(foodtype="중식", location="정문 || 철문")
    return render(request, "Chi_distance_maingate.html", {"lists": lists})


def Wes_criteria(request):
    return render(request, "Wes_criteria.html")


def Flour_1(request):
    return render(request, "Flour_1.html")


def Wes_distance(request):
    return render(request, "Wes_distance.html")


def Wes_review(request):
    lists = Post.objects.filter(foodtype="양식").order_by("-score")
    return render(request, "Wes_review.html", {"lists": lists})


def Wes_distance_sidedoor(request):
    lists = Post.objects.filter(foodtype="양식", location="쪽문")
    return render(request, "Wes_distance_sidedoor.html", {"lists": lists})


def Wes_distance_maingate(request):
    lists = Post.objects.filter(foodtype="양식", location="정문 || 철문")
    return render(request, "Wes_distance_maingate.html", {"lists": lists})


def redirect1(request):
    return redirect("/index/recommendmain")


def Flour_criteria(request):
    return render(request, "Flour_criteria.html")


def Flour_distance(request):
    return render(request, "Flour_distance.html")


def Flour_review(request):
    lists = Post.objects.filter(foodtype="분식").order_by("-score")
    return render(request, "Flour_review.html", {"lists": lists})


def Flour_distance_sidedoor(request):
    lists = Post.objects.filter(foodtype="분식", location="쪽문")
    return render(request, "Flour_distance_sidedoor.html", {"lists": lists})


def Flour_distance_maingate(request):
    lists = Post.objects.filter(foodtype="분식", location="정문 || 철문")
    return render(request, "Flour_distance_maingate.html", {"lists": lists})
