from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# name = ''
# Create your views here.
def home(request):
    return render(request, 'authentication/home.html')


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            name = user.first_name
            return render(request, 'profilec/index.html', {'name': name})


        else:
            messages.error(request, "Wrong Credentials")
            return redirect('signin')



    return render(request, 'authentication/signin.html')





def signup(request):
    if request.method == "POST":

        username = request.POST['username']
        name = request.POST['name']
        password = request.POST['password']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist!")
            return redirect('/signup')
        
        
        if len(username)>10:
            messages.error(request, "Username less than 10 characters please")
            return redirect('/signup')


        if not username.isalnum():
            messages.error(request, "Username should be Alpha Numeric")
            return redirect('/signup')



        myuser = User.objects.create_user(username,' ',password)
        myuser.first_name = name
        myuser.save()

        messages.success(request, "Your account created successfully")

        return redirect('signin')

    return render(request, 'authentication/signup.html')




def signout(request):
    logout(request)
    messages.success(request, 'logout sucess')
    return redirect('home')