from django.urls import path
from . import views

urlpatterns = [
  path('login/', views.loginUser, name='login'),
  path('logout/', views.logoutUser, name='logout'),
  path('register/', views.registerUser, name='register'),
  path('', views.index, name='list'),
  path('update_task/<str:pk>', views.updateTask, name='update_task' ),
  path('delete/<str:pk>', views.deleteTask, name='delete' ),
]