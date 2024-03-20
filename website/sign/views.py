from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Sign
from .forms import PetForm
# Create your views here.

def index(request):
    return render(request, 'sign/index.html')
    
def show(request):
    pets = Sign.objects.all()
    return render(request, 'sign/pet.html', {"boi": pets})
    
def update(request, pet_id):
    pet = Sign.objects.get(pk=pet_id)
    return render(request, 'sign/update.html', {'pet': pet})
    
    
    
    
def addpet(request):
    submitted = False
    if request.method == "POST":
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/sign/addpet?submitted=True')
    else:
        form = PetForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'sign/addpet.html', {'form': form, 'submitted': submitted})

