from django.urls import path 
from .import views 
from .views import PostList
urlpatterns=[

    path('home/',views.home,name='home'),
    path('',views.add_post,name='add_post'),
    path('api/vari/',PostList.as_view(),name='post-list'),
]