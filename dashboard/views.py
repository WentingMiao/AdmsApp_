from django.shortcuts import render,redirect
from account.models import Accounts
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from .table import profile_table
from django.db.models import Q
@login_required
def index(request):
    
    # account = Accounts.objects.get(name=request.user.username)

    print(request.user)
    # return render(request, 'base/index.html',{'account':account})
    return render(request, 'dashboard/index.html')


        
@login_required
def profile_index(request,id):

    if request.user:
        user = Accounts.objects.get(user_id= id)
        
        print(user.name)
        print(user.pic)
    return render(request, 'dashboard/user_profile.html',{'account':user})

@login_required
def profile_update(request,id):
    if not request.method == 'POST':
        return render(request, "account/login.html")
    msg=''

    try:

        # user = Accounts.objects.filter(name=request.user.username)[0]
        user = Accounts.objects.get(user_id= id)
        pic = request.FILES.get('pic',None)
        email = request.POST.get('email',None)
        name = request.POST.get('name',None)
        department = request.POST.get('department',None)
        position = request.POST.get('position',None)
        uni = request.POST.get('uni',None)
        if pic:
            print('changepic')
            fSystem = FileSystemStorage()
            newPic = fSystem.save(pic.name,pic)
            newPic_url=fSystem.url(newPic)
            user.pic = newPic_url

        if email:
            user.email=email
        if name:
            user.name=name
        if department:
            user.department = department
        if position:
            user.position = position
        if uni:
            user.uni = uni
        user.save()
        
        return redirect('/dashboard/profile/'+str(user.user_id)+'/')
        # return render(request, 'dashboard/user_profile.html',{'account':user})
    except Accounts.DoesNotExist:
        msg="Couldn't find the account"
        return redirect('/account/login/')
    
        
def document_profile(request):
    content = request.GET.get('content','')
    
    queryset =  Accounts.objects.exclude(profile__isnull=True).exclude(profile__exact='')
    if content :
        queryset = queryset.filter(Q(name__icontains=content)|Q(department__icontains=content))
    
    table= profile_table(queryset)

    return render(request,'document/profile.html',{'table':table,'content':content}) 
    
    

def profile_upload(request):
    if not request.method == 'POST':
        print('request error')
        return redirect('document_profile')

    profile = request.FILES.get('profileUpload','')
    try:
        account = Accounts.objects.get(name=request.user.username)
        account.profile = profile
        account.save()
        print('save successsfully')
    except Exception as e:
        print(e)



    return redirect('document_profile')