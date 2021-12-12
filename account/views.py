from django.shortcuts import render
# from account.serializer import AccountsSerializer
from rest_framework import viewsets
from account.models import *
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .table import *
from django.db.models import Q


def account_login(request):
    if not request.method == 'POST':
        return render(request, "account/login.html")
    err = {}
    username = request.POST.get('username', '')
    if username == '':
        err['username'] = "username can not be null"
    password = request.POST.get('password', '')
    if password == '':
        err['password'] = "password can not be null"
    print(username)
    print(password)
    if len(err) == 0:
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            err['password'] = "username or password is wrong!"
    print(err)
    return render(request, "account/login.html", {"error": err})


@login_required
def account_logout(request):
    print(request.user.username)
    logout(request)
    print("logout")
    return redirect("/account/login/")


def account_register(request):
    if not request.META['REQUEST_METHOD'] == 'POST':
        return render(request, "account/register.html")
    try:
        if not Department.objects.all():
            Department.objects.create(
                name="Default",
                introduction="System Set Default"
            ).save()
        email = request.POST.get('email', '')
        username = request.POST.get('username', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        print('%s\t %s \t %s \t %s ' % (email, username, password1, password2))
        err = []
        if not email or not username or not password1 or not password2:
            err.append("Input infomation can not be null")
            return render(request, "account/register.html", {"error": err})


        if password1 != password2:
            err.append("Two passward isn't match")
            return render(request, "account/register.html", {"error": err})

        user = User()
        user.username = username
        user.email = email
        user.set_password(password1)

        # newAccount = Account.objects.create(user=instance,name=instance.username,email=instance.email)

        try:
            user.save()
        except Exception as err:
            print('User register error \t %s' % (err))
        else:

            newUser = authenticate(username=username, password=password1)
            if newUser is not None:
                login(request, newUser)
                print("%s login successfully!" % (username))
                return redirect("/")
    except Exception as e:
        print(e)

    print("%s login failed!" % (user.username))
    return render(request, "account/register.html")


@login_required
def members_management(request):
    from .forms import AccountsForm
    content = request.GET.get('content', '')
    queryset = Accounts.objects.all()

    if content:
        queryset = queryset.filter(
            Q(name__icontains=content) | Q(department__icontains=content) | Q(position__icontains=content) | Q(
                uni__icontains=content))

    table = accountsTable(queryset)
    form = AccountsForm()
    return render(request, "account/members.html", {'table': table, 'form': form, 'content': content})


def member_add(request):
    from .forms import AccountsForm
    print('hi')
    if not request.META['REQUEST_METHOD'] == 'POST':
        print('request error')
        return redirect('/account/members/')

    new_member = AccountsForm(request.POST)
    new_member.save(commit=False)
    print(new_member.is_valid())
    print('save')
    return redirect('/account/members/')


def member_curd(request, record_id):
    if not request.META['REQUEST_METHOD'] == 'POST':
        print('request error')
        return redirect('/account/members/')
    try:
        user = User.objects.get(id=record_id)

    except:
        print('error')
        return redirect('/account/members/')
    method = request.POST.get('_method', '').lower()

    if method == 'edit':
        try:
            account = Accounts.objects.get(user=user)
            return render(request, "dashboard/user_profile.html", {'account': account})
        except:
            print('can not find account')

    if method == 'delete':
        user.delete()
        print('delete successfully')

    return redirect('/account/members/')


def users_index(request):
    from .forms import UserForm
    queryset = User.objects.all()
    content = request.GET.get('content', '')
    if content:
        queryset = queryset.filter(Q(username__icontains=content) | Q(email__icontains=content))

    table = UserTable(queryset)
    form = UserForm()
    return render(request, "account/users.html", {'table': table, 'form': form, 'content': content})


@login_required
def users_add(request):
    from .forms import UserForm
    if not request.META['REQUEST_METHOD'] == 'POST':
        print('request error')
        return redirect('/account/users/')

    userForm = UserForm(request.POST)
    if userForm.is_valid():
        user = userForm.save()
        user.refresh_from_db()
        user.username = userForm.cleaned_data.get('username')
        user.email = userForm.cleaned_data.get('email')
        user.set_password(userForm.cleaned_data['password'])
        user.save()

    return redirect('/account/users/')


@login_required
def users_curd(request, record_id):
    if not request.META['REQUEST_METHOD'] == 'POST':
        print('request error')
        return redirect('/account/users/')
    try:
        user = User.objects.get(id=record_id)

    except:
        print('error')
        return redirect('/account/members/')
    method = request.POST.get('_method', '').lower()
    if method == 'delete':
        user.delete()
        print('delete successfully')
    return redirect('/account/users/')
