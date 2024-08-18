from django.urls import path
from . import views
from bookstore.views import home, contactus,aboutUs

urlpatterns=[
    path('bookstore',views.index, name='index'),
    path('home',views.b_list, name='home'),
    path('contactus',views.contactus, name='contact'),
    path('about',views.aboutUs, name='about'),
    path('home/<int:id>',views.find_book,name='home.list'),
    path('deleted/<int:id>',views.deleted,name='bookstore.deleted'),
    path('allbooks',views.all_books,name='allbooks'),
    path('index',views.indexx,name='books.indexx'),
    path('index/<int:id>',views.show,name='books.show'),
    path('delete/<int:id>',views.delete,name='books.delete'), 
    path('create',views.create,name='books.create'), 
    path('<int:id>/edit',views.edit,name='books.edit'), 

]