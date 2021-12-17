from django.contrib import admin
from .models import Users, Subscriber, PublisherData

# Register your models here.

admin.site.register(Users)
admin.site.register(Subscriber)
admin.site.register(PublisherData)
