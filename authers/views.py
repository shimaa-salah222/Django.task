from django.shortcuts import render ,reverse , redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from authers.form import Autherform
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.

def index(request):
    return HttpResponse("<h1 style='color:green'> authers</h1>")

def home(request):
    return HttpResponse("<h1 style='color:green; text-align:center'>all authers</h1>")



auther=[
    {'id':1, 'name':'ali', 'birthdate':'22-10-2002' , 'created_at':'2-2-2022', 'updated_at':'2-2-2022','image':'imgd.jpg'},
    {'id':2, 'name':'ahmed', 'birthdate':'22-10-2002' , 'created_at':'2-2-2022', 'updated_at':'22-2-2020','image':'imgf.jpg'},
    {'id':3, 'name':'mona', 'birthdate':'22-10-2002', 'created_at':'2-2-2022', 'updated_at':'2-10-2010' ,'image':'imgg.jpg'},
    {'id':4, 'name':'menna', 'birthdate':'22-10-2002' , 'created_at':'2-2-2022', 'updated_at':'2-2-2023','image':'imgr.jpg'},
    {'id':5, 'name':'mohamed', 'birthdate':'22-10-2002' ,'created_at':'2-2-2022', 'updated_at':'2-4-2022', 'image':'imgd.jpg'},
    {'id':6, 'name':'salah', 'birthdate':'22-10-2002' , 'created_at':'2-2-2022', 'updated_at':'2-5-2021','image':'imgf.jpg'},
    {'id':7, 'name':'sama', 'birthdate':'22-10-2002' , 'created_at':'2-2-2022', 'updated_at':'2-2-2019','image':'imgg.jpg'},
    {'id':8, 'name':'walaa', 'birthdate':'22-10-2002' , 'created_at':'2-2-2022', 'updated_at':'10-2-2022','image':'imgr.jpg'},

]
def all_authers(request):
    return HttpResponse(auther)


def find_auther(request, id):
    selected_auther = next((auther for auther in auther if auther['id'] == int(id)), None)
    if selected_auther:
        return render(request, 'authers/s_auther.html', context={'auther': selected_auther})
    else:
        return HttpResponse("<h3 style='color:red; '>error: auther is not found!</h3>")
    
def deleted(request, id):
    try:
        selected_auther = next((auther for auther in auther if auther['id'] == int(id)), None)
        if selected_auther:
            auther.remove(selected_auther)
    except ValueError:
        pass

    url = reverse('home')
    return HttpResponseRedirect(url)
    

def A_list(request):

    return render(request,'authers/profile.html',
             context={'authers':auther}) 




from authers.models import Auther

def indexx(request):
   authers=Auther.objects.all()
   print(authers)
   return render(request, template_name ='authers/ind.html' ,
                 context={'authers':authers})



def show(request,id):
    authers=Auther.objects.get(id=id)
    return render(request, template_name ='authers/ashow.html' ,
                 context={'auther':authers})










class AtherListView(ListView):
    model = Auther
    template_name = 'authers/aulist.html'
    def get_queryset(self):
        return Auther.objects.all()




class AtherCreateView(CreateView):
    model = Auther
    form_class = Autherform
    template_name = 'authers/createA.html'
    success_url = '/authers/'


class AutherEdit(UpdateView):
    model = Auther
    form_class = Autherform
    template_name = 'authers/edita.html'
    success_url = '/authers/'



class AtherDeleteView(DeleteView):
    template_name = 'authers/delete.html'
    model = Auther
    success_url = '/authers/'
    def get_object(self, queryset=None):
        return get_object_or_404(Auther, pk=self.kwargs.get("pk"))



class AtherDetailView(DetailView):
    model = Auther
    template_name = 'authers/details.html'
