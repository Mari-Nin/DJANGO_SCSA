from django.urls import path
from . import views
app_name = 'templates_app'

urlpatterns = [
    path('', views.home,name = 'saxli'),
    path('home/', views.home,name = 'saxli'),
    path('about/', views.about,name = 'about'),
    path('welcome_page/', views.welcome_page,name = 'welcome_page'),
    path('post_detail/<int:post_id>/', views.post_detail,name = 'post_detail'),
    path('api_view/', views.api_view,name = 'API'),
    path('protected/', views.protected_view,name = 'protected_page'),
    path('posts/', views.posts,name = 'posts'),
    path('employee/', views.employee, name='employee'),
    path('edit_employee/<int:emp_id>/', views.edit_employee, name='edit_employee'),
    path('delete_employee/<int:emp_id>/', views.delete_employee, name='delete_employee'),
    path('contact/edit/<int:cont_id>/', views.edit_contact, name='edit_contact'),
    path('contact/delete/<int:cont_id>/', views.delete_contact, name='delete_contact'),
    path('contact/', views.contact, name='contact'),
    path('rates/', views.rates, name='rates'),
    path('edit_rate/<int:rate_id>/', views.edit_rate, name='edit_rate'),
    path('delete_rate/<int:rate_id>/', views.delete_rate, name='delete_rate'),
    

]


