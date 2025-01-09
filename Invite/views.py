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
    attend = Attending.objects.all()
    return render(request,'Display.html',context={'attending_list':attend})
