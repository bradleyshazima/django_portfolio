from django.contrib import admin

# Register your models here.

from .models import About, Contact, Contact_Message

admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Contact_Message)


