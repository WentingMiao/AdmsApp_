import django_tables2 as tables
from account.models import Accounts


class profile_table(tables.Table):
    class Meta:
        model = Accounts
        attrs = {"class": "table table-bordered table-hover dataTable"}
        fields = ("name", "department", "uni",'profile') 

