
from django.shortcuts import render, redirect,HttpResponse
from .models import Organizer,Athlete
from django.db.models import Q

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


import smtplib as s
from django.core.mail import send_mail
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Create your views here.

@login_required
def index(request):
    return render(request, 'index.html')

def all_event(request):
    orgs = Organizer.objects.all()
    context = {
        'orgs': orgs
    }
    print(context)
    return render(request, 'view_all_event.html', context)


def add_event(request):
    if request.method == 'POST':
        # Fetching user email from session
        # user_email = request.session.get('user_email')

        org_name = request.POST['org_name']
        event_name = request.POST['event_name']
        event_date = request.POST['event_date']
        event_fee = int(request.POST['event_fee'])
        sports_name = request.POST['sports_name']
        age = int(request.POST['age'])
        phone_number = int(request.POST['phone_number'])
        event_location = request.POST['event_location']
        new_org = Organizer(org_name=org_name, event_name=event_name, event_date=event_date, event_fee=event_fee, sports_name=sports_name,
                           age=age, phone_number=phone_number, event_location=event_location)
        new_org.save()

        # send email logic
        try:
            ob = s.SMTP("smtp.gmail.com", 587)
            ob.starttls()
            ob.login("iraj8204@gmail.com", "ajgsrgkyxqstqvmg")
            subject = "New Sports Event Organized!"
            body = "Dear Athlete, we're excited to announce a new sports event has been organized. Stay tuned for more details! \nFor more information, please visit: http://127.0.0.1:8000/all_event"
            message = "Subject:{}\n\n{}".format(subject, body)



            listofAddress = ["sajanaprajapati2810@gmail.com", "luckysharma123deepj@gmail.com"]
            ob.sendmail("SportsSync@gmail.com", listofAddress, message)
            print(listofAddress)


            # # Sending email to the user who signed up
            # ob.sendmail(subject, body, 'iraj8204@gmail.com', [user_email],message)
            # sender_email = "SportsSync@gmail.com"
            # sender_password = "guzvnazcmjzcwwhx"
            # subject = "Welcome to SportsSync!"
            # body = "Dear User, thank you for signing up with SportsSync! Get ready to receive updates on exciting sports events."
            #
            # send_mail(subject, body,sender_email, [user_email])
            # print("Welcome email sent successfully to user:", user_email)



            # print(user_email)
            print("send successfully!...")

            ob.quit()
        except Exception as e:
            return HttpResponse(f"An Exception Occurred! Event has been added but email could not be sent. Error: {str(e)}")


        return redirect('index')
    elif request.method == 'GET':
        return render(request, 'add_event.html')
    else:
        return HttpResponse("An Exception Occurred! Event Has Not Been Added")


def remove_event(request,org_id = 0):
    if org_id:
        try:
            emp_to_be_removed = Organizer.objects.get(id=org_id)
            emp_to_be_removed.delete()
            return  redirect('index')
            # return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("Please Enter A Valid EMP ID")
    orgs = Organizer.objects.all()
    context = {
        'orgs': orgs
    }

    return render(request, 'remove_event.html',context)

def filter_event(request):
    if request.method == 'POST':
        org_name = request.POST['org_name']
        sports = request.POST['sports']
        age = request.POST['age']
        orgs = Organizer.objects.all()
        if org_name:
            orgs = orgs.filter(Q(org_name__icontains=org_name) | Q(org_name__icontains=org_name))
        if sports:
            orgs = orgs.filter(sports_name__icontains=sports)
        if age:
            orgs = orgs.filter(age=age)

        context = {
            'orgs': orgs
        }
        return render(request, 'view_all_event.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_event.html')
    else:
        return HttpResponse('An Exception Occurred')


def HomePage(request):
    return render(request, 'home.html')


def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:

            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()

            # Store email in session
            # request.session['user_email'] = email

            # print(email)
            return redirect('login')

    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')