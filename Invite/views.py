from django.shortcuts import render
from .models import Attending
def HomePage(request):
    if request.method == "POST":
        data = request.POST
        name = data.get("Name")
        email = data.get("email")
        phone = data.get("Phone_Number")
        if Attending.objects.filter(email = email).count() or Attending.objects.filter(phoneNumber = phone):
            pass
        else:
            Attending.objects.create(
                name = name,
                email = email,
                phoneNumber = phone
            )
        
    return render(request,'invite.html')

def Display(request):
    Attending.objects.filter(name__icontains='Mohin').delete()
    Attending.objects.filter(email__icontains='mohin').delete()
    
    attend = Attending.objects.all()
    return render(request,'Display.html',context={'attending_list':attend})
