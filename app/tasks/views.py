from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import UserGym
from .forms import UserForm


# Create your views here.

def teste(request):
    return HttpResponse('Hello World')

# def login(request):
#    return render(request, 'tasks/login.html')

@login_required
def listUsers(request):

    search = request.GET.get('search')
     
    if search:

        users = UserGym.objects.filter(fullname__icontains=search, user=request.user)
    
    else:
        
        users_list = UserGym.objects.all().order_by('created_at').filter(user=request.user)
        
        paginator = Paginator(users_list, 4)

        page = request.GET.get('page')

        users = paginator.get_page(page)

    return render(request, 'tasks/listUsers.html', {'users': users})    

@login_required
def userView(request, id):
    user = get_object_or_404(UserGym, pk=id)
    return render(request, 'tasks/user.html', {'user': user})

@login_required
def addUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user
            user.save()
            return redirect('../')
    
    else:                  
        form = UserForm()
        return render(request, 'tasks/addUser.html', {'form': form})

@login_required
def editUser(request, id):
    user = get_object_or_404(UserGym, pk=id)
    form = UserForm(instance=user)

    if (request.method == 'POST'):
        form = UserForm(request.POST, instance=user)
        
        if(form.is_valid()):
            user.save()
            return  redirect('../')
        else:
            return render(request, 'tasks/editUser.html', {'form':form, 'user': user}) 

    else:
        return render(request, 'tasks/editUser.html', {'form':form, 'user': user})    

@login_required
def deleteUser(request, id):
    user = get_object_or_404(UserGym, pk=id)
    user.delete()

    messages.info(request, 'Usuário deletado com sucesso.')

    return  redirect('../')

def testeParam(request, name):
    return render(request, 'tasks/testeParm.html', {'name': name})
