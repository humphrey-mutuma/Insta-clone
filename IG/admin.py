from django.contrib import admin
from .models import Profile,Posts,Following,Comments

# Register your models here.
admin.site.register(Profile)
admin.site.register(Posts)
admin.site.register(Following)
admin.site.register(Comments)
