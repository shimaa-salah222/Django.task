from django.urls import path
from . import views
from authers.views import  AtherListView, AtherDetailView, AtherCreateView, AutherEdit, AtherDeleteView


urlpatterns=[
    path('authers',views.index, name='index'),
    path('home',views.A_list, name='home'),
    path('allauthers',views.all_authers, name='all_authers'),
    path('home/<int:id>',views.find_auther,name='auther.list'),
    path('deleted/<int:id>',views.deleted,name='auther.deleted'),
    path('',views.indexx,name='auther.indexx'),
    path('index/<int:id>',views.show,name='auther.show'),

    path('authers/', AtherListView.as_view(),name='listAuther'),
    path('create', AtherCreateView.as_view(),name='createAuther'), 
    path('<int:pk>/edit', AutherEdit.as_view(),name='editAuther'), 
    path('delete/<int:pk>', AtherDeleteView.as_view(),name='deleteAuther'), 
    path('<int:pk>/details', AtherDetailView.as_view(),name='detailsAuther'), 
]