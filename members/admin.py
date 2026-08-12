from django.contrib import admin
from .models import Member

#controls how the model is displayed in the admin interface
class MemberAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'joined_date')
    
admin.site.register(Member, MemberAdmin)