from django.shortcuts import render, redirect
from .forms import User_Form_Signup, User_Form_Login,Form_Add
from .models import User,Thkr
import uuid
from django.urls import reverse
from django.utils.safestring import mark_safe
import json

def Token(request):
    try:
        token = request.COOKIES.get('auth_token')
        if token:
            user_auth = User.objects.get(auth_token=token)
            return user_auth
    except user_auth.DoesNotExist:
        pass
    return None

def jsons():
    path = "main/jsons/"
    with open(path + "name.json", 'r', encoding='utf-8-sig') as file:
        dic = json.loads(file.read())
        lis = []
        nl = []
        for i in range(dic[-1]["ID"]):
            lis.append(dic[i]["TITLE"]) #names
            nl.append(i+1)
            with open(path+"athkar/"+str(i+1)+".json","r", encoding='utf-8-sig') as f:
                adic = json.loads(f.read())
                an = adic[dic[i]["TITLE"]]
        return lis,nl

def signup(re):
    try:
        user = Token(re)
        if user is None:
            form = User_Form_Signup()

            if re.method == "POST":
                form = User_Form_Signup(re.POST)

                if form.is_valid():
                    cd = form.cleaned_data

                    new_user = User(
                        username=cd['username'],
                        password=cd['password'],
                        first_name=cd['first_name'],
                        last_name=cd['last_name'],
                        email=cd["email"],
                        gender=cd["gender"],
                    )
                    new_user.save()

                    # Clear any existing authentication token cookies
                    response = redirect("login")
                    response.delete_cookie('auth_token')
                    return response
            
            return render(re, "form.html", {"form": form, "h1": "sign up"})
        else:
            return redirect("main")
    except UnboundLocalError:
        return redirect("logout")

def login(re):
    try:
        user = Token(re)
        if user is None:
            if re.method == 'POST':
                form = User_Form_Login(re.POST)
                if form.is_valid():
                    cd = form.cleaned_data
                    username = cd['username']
                    password = cd['password']
                    try:
                        user = User.objects.get(username=username)
                        if password == user.password:
                            # Generate authentication token
                            token = uuid.uuid4().hex
                            
                            # Save the token to the user's auth_token field
                            user.auth_token = token
                            user.save()

                            # Set the token in a cookie
                            response = redirect("main")
                            response.set_cookie('auth_token', token)
                            return response
                        else:
                            # Handle incorrect password
                            return render(re, 'form.html', {'error_message': 'Incorrect password',
                                                            "form":form,
                                                            "h1":"login",})
                    except User.DoesNotExist:
                        signup_url = reverse('signup')
                        error = mark_safe(f"Incorrect password. <a href='{signup_url}'>Sign up</a>")
                        return render(re, 'form.html', {'error_message': error,"form":form,"h1":"login",})
            else:
                form = User_Form_Login()
            return render(re, 'form.html', {'form': form})
        return redirect("main")
    except UnboundLocalError:
        return redirect("logout")
def profile(re):
    try:
        user = Token(re)
        if user is None:
            return redirect("login")
        return render(re, "profile.html", {"user": user.__dict__})
    except UnboundLocalError:
        return redirect("logout")

def logout(re):
    response = redirect("main")
    response.delete_cookie('auth_token')
    return response

def main(re):
    try:
        user = Token(re)
        name,num = jsons()
        zipy = list(zip(name, num))

        if user is None:
            return render(re, "main.html", {"user": 0,"list":zipy})
        return render(re, "main.html", {"user": 1,"list":zipy})
    
    except UnboundLocalError:
        return redirect("logout")

def select(i):
    path = "main/jsons/"
    with open(path + "name.json", 'r', encoding='utf-8-sig') as file:
        dic = json.loads(file.read())
        
        name = dic[i-1]["TITLE"]
        with open(path+"athkar/"+str(i)+".json","r", encoding='utf-8-sig') as f:
            adic = json.loads(f.read())
            an = adic[name]

    return an,name

def athkar(re,num):
    num,name = select(num)
    if num is None:
        return redirect("main")
    try:
        user = Token(re)
        if user is None:
            return render(re, "athkar.html", {"user": 0,"num":num,"name":name})
        return render(re,"athkar.html",{"user": 1,"num":num,"name":name})
    except UnboundLocalError:
        return redirect("logout")
    
def thkr(re):
    try:
        user = Token(re)
        form = Form_Add()
        if re.method == "POST":
                    form = Form_Add(re.POST)

                    if form.is_valid():
                        cd = form.cleaned_data

                        new_thkr = Thkr(
                            user_id = user,
                            thkr = cd['thkr'],
                            repeat = cd['repeat'],
                        )
                        new_thkr.save()
                        
        if re.method == "DELETE":
            idy = json.loads(re.body.decode())["id"]
            idy = Thkr.objects.filter(user_id = user.id,id=idy).delete()

        all = Thkr.objects.filter(user_id = user.id)
        
        jsony = list(all.values())
        json.dumps(jsony)
        return render(re,"form_add.html",{"form":form,"h1":"add your Thkr","all":all,"json":jsony})
    
    except AttributeError:
        return redirect("login")
    except UnboundLocalError:
        return redirect("logout")