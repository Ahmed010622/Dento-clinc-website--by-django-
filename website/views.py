from tokenize import Name
from django.shortcuts import render
from django.core.mail import send_mail


def home (request):
    return render (request , "home.html" , {})


def contact (request):
    if request.method=="POST":
        Name=request.POST["name"]
        Email=request.POST["email"]
        Subject=request.POST["subject"]
        message=request.POST["message"]
        #send an email
        send_mail(
            Subject,
            message,
            Email,#from email
            ['ahmedredadeabes@gmail.com'],#to email

        )

        return render (request , "contact.html" , {"name":Name})

    else:


        return render (request , "contact.html" , {})
def price (request):
    return render (request , "price.html" , {})

def service (request):
    return render (request , "service.html" , {})

def appointment (request):
    if request.method=="POST":
        your_name=request.POST["your-name"]
        your_email=request.POST["your-email"]
        appointment_date=request.POST["appointment-date"]
        appointment_time=request.POST["appointment-time"]

        appointment="Name:"+ your_name + "Email:"+ your_email +"Appointment_date:"+appointment_date +"Appointment_time:"+appointment_time
        send_mail(
            'appointment request',
             appointment,
             your_email,
            ['ahmedredadeabes@gmail.com'],#to email

             )
       
        return render (request , "appointment.html" , 
        {"your_name":your_name,
        "your_email":your_email,
        "appointment_date":appointment_date,
        "appointment_time":appointment_time,

        })

    else:
        return render (request , "appointment.html" , {})

def about (request):
    return render (request , "about.html" , {})