from django.contrib import admin
from .models import Post
from .models import Announce
from django.contrib.admin import AdminSite
from .models import moderation
class PostAdmin(admin.ModelAdmin):
    list_display = ('title',  'moderation')
  

admin.site.register(Post, PostAdmin)
admin.site.register(Announce)
admin.site.site_header='Scientract Administrator'
index_title = "Welcome Scientract Administrator Portal"
admin.site.register(moderation)

class ModAdminSite(AdminSite):
    site_header = "Moderation"
    site_title = "Moderation"
    index_title = "Welcome Moderation Portal"
   
   


Mod_admin_site = ModAdminSite(name='Mod_admin')


Mod_admin_site.register(Post)
Mod_admin_site.register(moderation)


