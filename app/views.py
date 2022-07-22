# from importlib.resources import path
import email
from django.shortcuts import render
# from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
# from django.contrib import messages
# from django.core.paginator import Paginator
# from django.db.models import Q
# from django.contrib.auth.decorators import login_required

from .forms import AccountAddForm
# from .models import Message,Friend,Group,Good
# from .forms import GroupCheckForm,GroupSelectForm,FriendsForm,CreateGroupForm, PostForm


# TOPページのビュー関数
def index(request):
    return render(request, "app/index.html")

# loginページのビュー関数
def login(request):
    return render(request, "app/login.html")

# ユーザー登録ページのビュー関数
def user_register(request):
    if request.method == "GET":
        form = AccountAddForm
    elif request.method == "POST":
        form = AccountAddForm(request.POST)
        if form.is_valid():
            User().objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )
            return HttpResponse("アカウント登録が完了しました。")
    context = {
        'form': form
    }
    return render(request, "app/user-register.html")


# @login_required(login_url='/admin/login/')
