from django.urls import path
from . import views 

app_name = 'DragonLifts'
urlpatterns = [
  path('1/', views.workoutBuilder, name='default'),
  path('1/addAna', views.addAnaExcercise),
]