import django_tables2 as tables
from account.models import Accounts, ImgFiles


class profile_table(tables.Table):
    class Meta:
        model = Accounts
        attrs = {"class": "table table-bordered table-hover dataTable"}
        fields = ("name", "department", "uni", 'profile')


class gallery_table(tables.Table):
    pic = tables.TemplateColumn(
        '<a href="/media/{{record.pic}}" target="_blank"><img src="/media/{{record.pic}}" class="profile-user-img img-fluid img-circle "  style="height:50px;width:50px" alt="User Image"><a/>',
        orderable=False,
        verbose_name='pic'
    )

    class Meta:
        model = ImgFiles
        attrs = {"class": "table table-bordered table-hover dataTable"}
        fields = ('account', "account.department", "account.uni", 'pic',)
