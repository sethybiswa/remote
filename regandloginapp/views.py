from django.shortcuts import render,redirect
from regandloginapp.models import RegistrationData
from regandloginapp.forms import RegistrationForm
from django.http.response import HttpResponse
from regandloginapp.forms import LoginForm

# Create your views here.
def index(request):
    return render(request,'indexfile.html')

def registrationview(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            username = form.cleaned_data.get("username")
            password = request.POST.get("password")
            mobile = request.POST.get("mobile")
            email = request.POST.get("email")
            gender = form.cleaned_data.get("gender")
            date_of_birth = form.cleaned_data.get("date_of_birth")

            data = RegistrationData(
                first_name = first_name,
                last_name = last_name,
                username=username,
                password=password,
                mobile=mobile,
                email=email,
                gender=gender,
                date_of_birth=date_of_birth
            )
            data.save()
            form = LoginForm()
            return render(request,'login.html',{'form':form})
        else:
            return HttpResponse('User Missing Values')
    else:
        form = RegistrationForm()
        return render(request,'registrationfile.html',{'form':form})



def loginview(request):
    if request.method == "POST":
        lform = LoginForm(request.POST)
        if lform.is_valid():
            username = request.POST.get('user_name'),
            password = request.POST.get('password')
            # lform = RegistrationData.objects.all()
            username = RegistrationData.objects.filter(username=username,password=password)
            # password = RegistrationData.objects.filter(password=password)
            if username:
                if password:
                    return HttpResponse("Success")
                else:
                    return HttpResponse("Enter Correct Password")
            else:
                return HttpResponse("Enter Correct Details")
        else:
            return HttpResponse("User Missing Data")
    else:
        lform = LoginForm()
        return render(request,'login.html',{"lform":lform})


