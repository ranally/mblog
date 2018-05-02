# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=('title','slug','pub_date')


admin.site.register(Post,PostAdmin)
