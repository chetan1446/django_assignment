from django.contrib import admin
from .models import Mammals,Fish,Bird
# Register your models here.
admin.site.register(Mammals)
admin.site.register(Fish)
admin.site.register(Bird)