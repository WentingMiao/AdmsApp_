from django.contrib import admin
from .models import Accounts, Department, Position, University

# Register your models here.
admin.site.register(Accounts)

admin.site.register(Department)
admin.site.register(Position)
admin.site.register(University)
