from django.shortcuts import render,redirect
from .models import Activity
from .forms import ActivityForm
from .table import activityTable,applicationTable,selfApplicationTable
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from account.models import Accounts
from django.db.models import Q
# Create your views here.
def activity_index(request):
    content = request.GET.get('content','')
    queryset =  Activity.objects.filter(passed=True).order_by('-hold_time')
    if content :
        queryset = queryset.filter(Q(title__icontains=content)|Q(department__icontains=content)|Q(name__icontains=content)|Q(short_descipt__icontains=content))
    
    table= activityTable(queryset)

    return render(request,'activity/index.html',{'table':table,'content':content})


#activity create
@login_required
def activity_create(request):
    form = ActivityForm()
    if not request.META['REQUEST_METHOD'] == 'POST':
        return render(request,'activity/create.html',{'form':form})
    
    actform  = ActivityForm(request.POST)
    print(actform.errors)
    if actform.is_valid():
        activity = actform.save(commit = False)
        # activity.title = actform.cleaned_date.get('title')
        # activity.department = actform.cleaned_data.get('department')
        # activity.short_descipt = actform.cleaned_date.get('short_descipt')
        # activity.expected_number = actform.cleaned_date.get('expected_number')
        # activity.hold_time = actform.cleaned_date.get('hold_time')
        # activity.post = actform.cleaned_date.get('post')
        # activity.deadline = actform.cleaned_date.get('deadline')


        activity.name = request.user.username
        activity.registered_number =0
        pic = request.FILES.get('pic',None)
        if pic:
            print('addpic')
            fSystem = FileSystemStorage()
            newPic = fSystem.save(pic.name,pic)
            newPic_url=fSystem.url(newPic)
            activity.pic = newPic_url
        if request.user.is_superuser:
            activity.passed = True
        activity.save()
        print('save successfully')
        return redirect('activitiy_details',pk=activity.pk)
    else:
        print('form is not valid')
    return redirect('activities')
    
#activity index
def activity_details(request,pk):
    activity =  Activity.objects.get(id=pk)
    return render(request,'activity/details.html',{'activity':activity})

#activity edit
def activity_edit(request,pk):
    activity =  Activity.objects.get(id=pk)
    if not request.META['REQUEST_METHOD'] == 'POST':
        
        form = ActivityForm(instance= activity)
        return render(request,'activity/create.html',{'activity':activity,'form':form,'edit':True})
    else:
        actform  = ActivityForm(request.POST, instance=activity)
        activity = actform.save(commit=False)
        activity.save()
        print('save successfully')
        return redirect('activitiy_details',pk=activity.pk)

#activity delete
def activity_delete(request,pk):
    activity =  Activity.objects.get(pk=pk)
    activity.delete()
    print('delete successfully')
    return redirect('activities')

def activity_register(request):
    if not request.META['REQUEST_METHOD'] == 'POST':
        return redirect('activities')
    pk = request.POST.get('pk',None)
    
    if pk:
        try:
            activity =  Activity.objects.get(pk=pk)
            # print(activity.registered_members.count())
            account = Accounts.objects.get(name=request.user.username)
            activity.registered_members.add(account)
            activity.save()
            
            print('register successfully')
            return redirect('activitiy_details',pk=activity.pk)
        except Exception as e:
            print(e)
    else:
        print("pk error")        
    return redirect('activities')

def activity_calendar(request):
    all_activites = Activity.objects.filter(passed=True)
    

    return render(request,'activity/calendar.html',{'activities':all_activites})

def activity_application(request):
    content = request.GET.get('content','')
    queryset =  Activity.objects.filter(passed=False).order_by('-hold_time')
    if content :
        queryset = queryset.filter(Q(title__icontains=content)|Q(department__icontains=content)|Q(name__icontains=content)|Q(short_descipt__icontains=content))
    
    table= applicationTable(queryset)

    return render(request,'activity/applications.html',{'table':table,'content':content})


def activity_check(request):
    if not request.META['REQUEST_METHOD'] == 'POST':
        return redirect('activities')

    pk = request.POST.get('pk',None)
    if pk:
        passed = request.POST.get('passed')
        try:
           
            activity = Activity.objects.get(pk=pk)
            if passed=='on':
                activity.passed = True
            else:
                activity.passed = False
            comment_user = requset.user.username
            activity.save()
            return redirect('activitiy_details',pk=activity.pk)

        except Exception as e:
            print(e)
            return redirect('activities')

    

def activity_self(request):
    content = request.GET.get('content','')
    queryset =  Activity.objects.filter(name=request.user.username).order_by('-hold_time')
    if content :
        queryset = queryset.filter(Q(title__icontains=content)|Q(department__icontains=content)|Q(name__icontains=content)|Q(short_descipt__icontains=content))
    
    table= selfApplicationTable(queryset)

    return render(request,'activity/applications.html',{'table':table,'content':content})
   


def activity_demo(request):
    return render(request,'activity/demo.html')