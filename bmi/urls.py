from django.urls import path ,include
from bmi import views

urlpatterns = [
	path('UserList/',views.UserList.as_view(),name='UserList'),
 
]