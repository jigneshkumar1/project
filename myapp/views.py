from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

# def home(request):
#     return render(request, "myapp/index.html")

# def about(request):
#     return render(request,"myapp/aboutpage.html")


# def contect(request):
#     return render(request,"myapp/contactpage.html")

# def profile(request):
#     return render(request,"myapp/profilepage.html")


"""
get() : fetch single record from  model it will return an object

            syntax : Model.objects.get(filedname = value..)
            e.g. User.objects.get(email = email)
"""

def login(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "Chairman":
            cid = Chairman.objects.get(user_id = uid)
            context = {
                "uid" : uid,
                "cid" : cid,
            }
            return render(request,"myapp/index.html",context)
    else:
        if request.POST:
            print("----->>button clicked")
            email = request.POST['email']
            password = request.POST['password']
            print("-----> email",email)
            print("-----> password",password)
            # print("=======>>> uid :: ",uid)
            # print("-------> email",uid.role)
            # print("-------> password",uid.password)
            try:
                uid = User.objects.get(email = email)
                if uid.password == password:
                    if uid.role == "Chairman":
                        cid = Chairman.objects.get(user_id = uid)
                        print("welcome chairman")
                        context = {
                            "uid" : uid,
                            "cid" : cid,
                        }
                        # store email in session
                        request.session['email'] = email
                        return render(request,"myapp/index.html",context)
                    else:
                        print("Welcome member")
                else:
                    e_msg = "invalid password"
                    return render(request,"myapp/login.html",{'e_msg' : e_msg})

            except Exception as e:
                print("Error: ",e)
                e_msg = "invalid email"
                return render(request,"myapp/login.html",{'e_msg' : e_msg})

        else:
            print("-------> only page is refresh")
        return render(request,"myapp/login.html")

def index(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        context = {
            'uid' : uid,
            'cid' : cid
        }
        return render(request,"myapp/index.html",context)
    else:
        return render(request,"myapp/login.html")


def profile(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        context = {
            'uid' : uid,
            'cid' : cid
        }
        return render(request,"myapp/profile.html",context)
    else:
        return render(request,"myapp/login.html")

def logout(request):
    if "email" in request.session:
        del request.session["email"]
        return render(request,"myapp/login.html")
    else:
        return render(request,"myapp/login.html")

def notfound(request):
    print("not found page")
    return render(request,"myapp/page404.html")

def change_password(request):
    if request.POST:
        currentPassword = request.POST['currentpassword']
        newPassword = request.POST['newpassword']

        uid = User.object.get(email = request.session['email'])

        if uid.password == currentPassword:
            uid.password = newPassword
            uid.save() # update
            del request.session['email']
            s_msg = "Successfully password Reset"
            return render (request, "myapp/login.html",{'s_msg' : s_msg})
        else:
            e_msg = "invalid password"
            del request.session['email'] #logout logic
            return render(request,"myapp/login.html",{'e_msg' : e_msg})
    return render(request,"myapp/profile.html")
