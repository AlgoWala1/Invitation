from django.shortcuts import render
from .models import Attending
def HomePage(request):
    if request.method == "POST":
        data = request.POST
        name = data.get("Name")
        email = data.get("email")

        Attending.objects.create(
            name = name,
            email = email
        )
        
    return render(request,'invite.html')

def Display(request):
    Attending.objects.filter(name__icontains='Mohin').delete()
    Attending.objects.filter(email__icontains='mohin').delete()
    attend = Attending.objects.all()
    return render(request,'Display.html',context={'attending_list':attend})
