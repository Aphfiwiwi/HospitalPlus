from django.shortcuts import render,redirect
from hospitalapp.models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def service(request):
    return render(request, 'service-details.html')

def starter(request):
    return render(request, 'starter-page.html')

def about(request):
    return render(request, 'about.html')

def serve(request):
    return render(request, 'services.html')

def departments(request):
    return render(request, 'departments.html')

def doctors(request):
    return render(request, 'doctors.html')

def appoint(request):
    if request.method == "POST":
        myappointment = appointment(
            name = request.POST["name"],
            email = request.POST["email"],
            phone = request.POST["phone"],
            date = request.POST["date"],
            department = request.POST["department"],
            doctor = request.POST["doctor"],
            message = request.POST["message"],
        )
        myappointment.save()
        return redirect("/appointment/")
    else :
        return render(request, 'form.html')


def contact(request):
    #to store values for forms
    if request.method == "POST":
        mycontact = contactinfo(
            name = request.POST["name"],
            email = request.POST["email"],
            subject = request.POST["subject"],
            message = request.POST["message"],
        )
        mycontact.save()
        return redirect("/show/")
    else :
        return render(request, 'contact.html')

def show(request):
    #to fetch info stored in models and display them
    all = appointment.objects.all() #appointment is the name of the model
    return render(request, 'show.html', {'all': all})

def delete(request,id):
    deleteappointment = appointment.objects.get(id=id) #name of model
    deleteappointment.delete()
    return redirect("/show/")