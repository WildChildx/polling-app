from django.contrib import admin
from polls.models import Choice, Questions

admin.site.register(Questions)
admin.site.register(Choice)