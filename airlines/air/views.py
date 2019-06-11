from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from .models import User, AddPlane, ConfirmTicket

def index(request):
    return render(request, 'air\index.html')

def dashboard(request):
    return render(request,'air\dashboard.html')

def profile(request, pk):
    obj = User.objects.get(pk=pk)
    # print(obj)
    return render(request, 'air\profile.html', {'obj':obj })

def register(request):
    if request.method =="POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        country = request.POST.get('country')
        state = request.POST.get('state')
        pwd1 = request.POST.get('pwd1')
        pwd2 = request.POST.get('pwd2')
        if pwd1==pwd2:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email Already exists')
                return redirect('register')
            else:
                user = User(fname=fname, lname=lname, phone=phone, email=email, country=country, state=state,pwd=pwd1)
                user.save()
                messages.success(request, 'Register Succesfull, You can login now')
                return  redirect('login')
        else:
            messages.error(request, 'Password do not match, please try again')
            return redirect('register')
    else:
        return render(request, 'air/register.html')

def login(request):
    if request.method=="POST":
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')

        if User.objects.filter(email=email) and User.objects.filter(pwd=pwd):
            c = User.objects.filter(email=email)
            return render(request, 'air\dashboard.html', {'y':c})
            # messages.success(request, 'success')
        else:
            messages.error(request, 'Email and password did not match')
            return redirect('login')
    else:
        return render(request, 'air\login.html')

    # ===== Some Error here==================

    # if request.method == "POST":
    #     email = request.POST.get('email')
    #     pwd = request.POST.get('pwd')
    #     print(email)
    #     print(pwd)
    #     user= authenticate(request,email=email, pwd=pwd)
    #     print(user)
    #     if user is not None:
    #         auth.login(request, user)
    #         return render(request, 'air/dashboard.html')
    #     else:
    #         return render(request, 'air/login.html')
    # else:
    #     return render(request, 'air/login.html')
    # =========================

def logout(request):
    auth.logout(request)
    return redirect('index')

def delete(request, dl):
    User.objects.filter(id=dl).delete()
    return render(request, 'air/index.html')

def show(request):
    if request.method=="POST":
        source = request.POST.get('source')
        # estination = request.POST.get('destination')d
        flights= AddPlane.objects.filter(source=source)
        # d = AddPlane.objects.filter(destination=destination)
        # context= {
        #     'source':s,
        #     'destination':d,
        # }
        # print(context)
        return render(request, 'air/show.html', {'flights': flights})
    else:
        flights = AddPlane.objects.all()
        return render(request, 'air/show.html', { 'flights':flights })

def buy(request, buy_id):
    # print("Buy coll ho rha hai kya", buy_id)
    buy_now = AddPlane.objects.filter(id=buy_id)
    # print(buy_now)
    return render(request, 'air/buy.html', { 'buy_now':buy_now })

def confirm(request):
    if request.method == "POST":
        cname = request.POST.get('cname')
        start = request.POST.get('start')
        end = request.POST.get('end')
        dtime = request.POST.get('dtime')
        atime = request.POST.get('atime')
        payprice = request.POST.get('payprice')
        category = request.POST.get('category')
        mail = request.POST.get('mail')
        if User.objects.filter(email=mail).exists():
            cticket = ConfirmTicket(cname=cname, start=start, end=end, dtime=dtime, atime=atime, payprice=payprice, category=category, mail=mail)
            cticket.save()
            print(cticket)
            messages.success(request, ' Ticket Confirm, You can login for download')
            return redirect('login')
        else:
            messages.error(request, 'Email do not match, please try again')
            return redirect('index')
    else:
        return render(request, 'air/index.html')

def ticket(request, e_pk):
    tk = User.objects.filter(email=e_pk)
    tkc =ConfirmTicket.objects.filter(mail=e_pk)
    print(tk)
    print(tkc)
    return render(request, 'air/ticket.html', {'tk':tk, 'tkc':tkc})
