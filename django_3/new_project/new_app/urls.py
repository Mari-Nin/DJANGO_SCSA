from django.urls import path
from .views import hello_view,about_view,item_detail_view

urlpatterns=[
    path('hello/',hello_view,name='hello'),
    path('about/',about_view,name='about'),
    path('item/<int:item_id>/',item_detail_view,name='item_detail'),
]