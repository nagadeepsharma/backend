from api.views import projects
from django.contrib import admin
from .models import Blogs, Projects,Tag
# Register your models here.
admin.site.register(Projects)
admin.site.register(Tag)
admin.site.register(Blogs)
