from django.contrib import admin
from .models import Group, UserGroup, Instances, Blogpost

admin.site.register(Group)
admin.site.register(UserGroup)
admin.site.register(Instances)
admin.site.register(Blogpost)
