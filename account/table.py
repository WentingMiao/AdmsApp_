import django_tables2 as tables
from .models import Accounts
from django.contrib.auth.models import User

class accountsTable(tables.Table):
    delete = tables.TemplateColumn(
        '<form action="/account/members/curd/{{record.pk}}/" method="post">{% csrf_token %}<input type="hidden" name="_method" value="delete"><button data-toggle="tooltip" title="Please note that deletion cannot be undone" type="submit" class="btn btn-danger btn-xs">Delete</button></form>',
        orderable=False,
        verbose_name=''
    )

    edit = tables.TemplateColumn(
        ' <form action="{% url \'members_curd\' record_id=record.pk %} " method="post" >{% csrf_token %}<input type="hidden" name="_method" value="edit"><button  type="submit" class="btn btn-info btn-xs">Detail</button></form>',
        orderable=False,
        verbose_name='Edit'
    )

    img = tables.TemplateColumn(
        # '<p>{{record.pic}}</p>',
        '<img src="{{record.pic}}" class="profile-user-img img-fluid img-circle "  style="height:50px;width:50px" alt="User Image">',
        orderable=False,
        verbose_name=''
    )

    class Meta:
        model = Accounts
        attrs = {"class": "table table-bordered table-hover dataTable"}
        # fields = ("name",  "department", "position","uni","email","phone_number","edit","delete") 
        fields = ("img","name",  "department", "position","uni","edit","delete",) 

class UserTable(tables.Table):
    delete = tables.TemplateColumn(
        ' <form action="/account/users/curd/{{record.pk}}/" method="post">{% csrf_token %}<input type="hidden" name="_method" value="delete"><button data-toggle="tooltip" title="Please note that deletion cannot be undone" type="submit" class="btn btn-danger btn-xs">Delete</button></form>',
        orderable=False,
        verbose_name=''
    )
    class Meta:
        model = User
        attrs = {"class": "table table-bordered table-hover dataTable"}
        fields = ("username","email","is_staff") 
        # fields = '__all__'
        #这里还没有展示 onetoonefield 的
