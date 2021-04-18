from django.contrib import admin
from .models import AnaerobicExercise, AerobicExercise, user

admin.site.register(AnaerobicExercise)
admin.site.register(AerobicExercise)
admin.site.register(user)