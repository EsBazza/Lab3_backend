from django.urls import path
from . import views
app_name = "registration" 

urlpatterns = [
       path('api/register/', views.register_user, name='register_user'),
       path('api/users/', views.list_users, name='list_users'),  # new endpoint
       path('api/users/<int:pk>/', views.user_detail, name='user_detail'),
       path('api/students/', views.student_list, name='student_list'),
       path('api/students/<int:pk>/', views.student_detail, name='student_detail'),
       
       path('login/', views.login_view, name='login_html'),
       path('logout/', views.logout_view, name='logout_html'),
       path('users/', views.users_html, name='users_html'),

]