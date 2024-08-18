from django.shortcuts import render ,reverse , redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from bookstore.models import All_books
from authers.models import Auther

# Create your views here.

def index(request):
    return HttpResponse("<h1 style='color:green'> Book store</h1>")

def home(request):
    return HttpResponse("<h1 style='color:green; text-align:center'>all books</h1>")

def contactus(request):
    return HttpResponse("<h1 style='color:green; text-align:center'>Contact Us</h1>")

def aboutUs(request):
    return HttpResponse("<h1 style='color:red; text-align:center'>About Us</h1>")


books=[
    {'id':1, 'name':'book1', 'num_of_pages':100 , 'cover':'img1.jpg', 'auther':'aaa','price':120},
    {'id':2, 'name':'book2', 'num_of_pages':220 , 'cover':'img2.jpg', 'auther':'ddd','price':130},
    {'id':3, 'name':'book3', 'num_of_pages':230 , 'cover':'img3.jpg', 'auther':'rrr','price':125},
    {'id':4, 'name':'book4', 'num_of_pages':240 , 'cover':'img4.jpg', 'auther':'ccc','price':150},
    {'id':5, 'name':'book5', 'num_of_pages':300 , 'cover':'img5.jpg', 'auther':'ttt','price':160},
    {'id':6, 'name':'book6', 'num_of_pages':270 , 'cover':'img1.jpg', 'auther':'vvv','price':120},
    {'id':7, 'name':'book7', 'num_of_pages':320 , 'cover':'img2.jpg', 'auther':'uuu','price':200},
    {'id':8, 'name':'book8', 'num_of_pages':400 , 'cover':'img3.jpg', 'auther':'qqq','price':220},
    {'id':9, 'name':'book9', 'num_of_pages':310 , 'cover':'img4.jpg', 'auther':'mmm','price':230},
    {'id':10,'name':'book10', 'num_of_pages':430 , 'cover':'img5.jpg', 'auther':'sss','price':500},

]
def all_books(request):
    return HttpResponse(books)


def find_book(request, id):
    selected_book = next((book for book in books if book['id'] == int(id)), None)
    if selected_book:
        return render(request, 'bookstore/s_book.html', context={'book': selected_book})
    else:
        return HttpResponse("<h3 style='color:red; '>error: Book is not found!</h3>")
    
    
def deleted(request, id):
    try:
        selected_book = next((book for book in books if book['id'] == int(id)), None)
        if selected_book:
            books.remove(selected_book)
    except ValueError:
        pass

    url = reverse('home')
    return HttpResponseRedirect(url)
    

def b_list(request):

    return render(request,'bookstore/data.html',
             context={'books':books})

""" def book5(request):
  selected_book = next((book for book in books if book['id'] == 5), None)
  print(selected_book)
  return render(request, 'books/book5.html', context={'book5': selected_book}) """






def indexx(request):
   books=All_books.objects.all()
   print(books)
   return render(request, template_name ='bookstore/index.html' ,
                 context={'books':books})



def show(request,id):
    books=All_books.objects.get(id=id)
    return render(request, template_name ='bookstore/show.html' ,
                 context={'book':books})


def delete(request,id):
    books=All_books.objects.get(id=id)
    books.delete()

    url = reverse('books.indexx')
    return redirect(url)  


def create(request):
    print(f"request here {request}")
    authers=Auther.objects.all()
    if request.method == 'POST':
        
        print(request.POST)
        print(f"name= {request.POST['name']}")
        print(request.FILES)

        book=All_books()
        book.name =request.POST['name']
        auther= Auther.objects.filter(id=request.POST['auther']).first()
        if(auther):
            book.auther=auther

        book.auther = Auther.objects.get(id=request.POST['auther'])
        

        book.num_of_pages =request.POST['num_of_pages']
        book.price =request.POST['price']
        book.cover =request.FILES['cover']
        book.save()
        url = reverse('books.indexx')
        return redirect(url)  

    return render(request, template_name ='bookstore/create.html',
                  context={'authers':authers})


def edit(request,id):
     books= get_object_or_404(All_books,id=id)
     auther=Auther.objects.all()
     if request.method == 'POST':
         books.name =request.POST['name']
         books.num_of_pages =request.POST['num_of_pages']
         books.price =request.POST['price']
         if 'auther' in request.POST:
             auther= Auther.objects.filter(id=request.POST['auther']).first()
             if(auther):
               books.auther=auther

         books.cover =request.FILES['cover']
         books.save() 
         url = reverse('books.indexx')
         return redirect(url)
     
     return render(request, template_name='bookstore/edit.html',
                  context={'authers':auther, 'books': books})

   