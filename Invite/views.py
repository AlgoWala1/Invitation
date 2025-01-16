from django.shortcuts import render
from .models import Attending
from .models import Events
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

def Activities(request):
    if request.method == "POST":
        data = request.POST
        activity = data.get("identity")
        team_name = data.get("team_name")
        leader_name = data.get("leader_name")
        phone = data.get("phone")

        print(activity , team_name , leader_name, phone)
        if Events.objects.filter(team_name = team_name) or Events.objects.filter(phone = phone):
            pass
        else:
            Events.objects.create(
                team_name = team_name,
                leader_name = leader_name,
                phone = phone,
                activity = activity
            )

    
    return render(request,"Activities.html")