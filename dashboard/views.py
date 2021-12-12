from django.shortcuts import render, redirect
from account.models import Accounts, Department, ImgFiles, Position, University
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

from activity.models import Activity
from .table import profile_table, gallery_table
from django.db.models import Q


@login_required
def index(request):
    imglist = []
    for k, item in enumerate(ImgFiles.objects.order_by('-deadline')[:3]):
        imglist.append({
            "id": k + 1,
            "imgurl": item.pic
        })
    queryset = Activity.objects.filter(passed=True).order_by('-hold_time')[:3]
    return render(request, 'dashboard/index.html', {"Activity": queryset, "imglist": imglist})


@login_required
def profile_index(request, id):
    if request.user:
        user = Accounts.objects.get(user_id=id)
        departments = Department.objects.all()
        positions = Position.objects.all()
        universitys = University.objects.all()
    return render(request, 'dashboard/user_profile.html',
                  {'account': user, 'departments': departments, 'positions': positions, 'universitys': universitys})


@login_required
def profile_update(request, id):
    if not request.method == 'POST':
        return render(request, "account/login.html")
    msg = ''

    try:

        # user = Accounts.objects.filter(name=request.user.username)[0]
        user = Accounts.objects.get(user_id=id)
        pic = request.FILES.get('pic', None)
        email = request.POST.get('email', None)
        name = request.POST.get('name', None)
        departmentid = request.POST.get('department', "1")
        department = Department.objects.filter(id=departmentid).first()
        positionid = request.POST.get('position', None)
        position = Position.objects.filter(id=positionid).first()
        uniid = request.POST.get('uni', None)
        uni = University.objects.filter(id=uniid).first()
        if pic:
            print('changepic')
            fSystem = FileSystemStorage()
            newPic = fSystem.save(pic.name, pic)
            newPic_url = fSystem.url(newPic)
            user.pic = newPic_url

        if email:
            user.email = email
        if name:
            user.name = name
        if department:
            user.department = department
        if position:
            user.position = position
        if uni:
            user.uni = uni
        user.save()
        Activity.objects.filter(name=Accounts.objects.filter(name=request.user.username).first()).update(
            department=department)

        return redirect('/dashboard/profile/' + str(user.user_id) + '/')
        # return render(request, 'dashboard/user_profile.html',{'account':user})
    except Accounts.DoesNotExist:
        msg = "Couldn't find the account"
        return redirect('/account/login/')


def document_profile(request):
    content = request.GET.get('content', '')

    queryset = Accounts.objects.exclude(profile__isnull=True).exclude(profile__exact='')
    if content:
        queryset = queryset.filter(Q(name__icontains=content) | Q(department__icontains=content))

    table = profile_table(queryset)

    return render(request, 'document/profile.html', {'table': table, 'content': content})


def document_gallery(request):
    department = request.GET.get('department', '')
    departments = Department.objects.all()
    queryset = ImgFiles.objects.all()
    if department:
        queryset = queryset.filter(account__department_id=department)

    table = gallery_table(queryset)

    return render(request, 'document/imgfile.html', {'table': table, "queryset": queryset, 'departments': departments})


def profile_upload(request):
    if not request.method == 'POST':
        print('request error')
        return redirect('document_profile')

    profile = request.FILES.get('profileUpload', '')
    if profile:
        try:
            account = Accounts.objects.get(name=request.user.username)
            account.profile = profile
            account.save()
            print('save successsfully')
        except Exception as e:
            print(e)

    return redirect('document_profile')


def imgfile_upload(request):
    if not request.method == 'POST':
        print('request error')
        return redirect('document_gallery')

    profile = request.FILES.get('profileUpload', '')
    if profile:
        try:
            account = Accounts.objects.get(name=request.user.username)
            ImgFiles.objects.create(
                account=account,
                pic=profile
            ).save()
            print('save successsfully')
        except Exception as e:
            print(e)

    return redirect('document_gallery')
