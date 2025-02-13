
from django.contrib import admin
from TestApp.models import Contact
from TestApp.models import About_us
from TestApp.models import Course

# Register your models here.
# class ContactAdmin(admin.ModelAdmin):
#     clist=['name','email','message']
admin.site.register(Contact)
admin.site.register(About_us)
admin.site.register(Course)
