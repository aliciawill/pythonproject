from django.contrib import admin

# Register your models here.
from shop01.models import Test, Question

admin.site.register(Test)
admin.site.register(Question)