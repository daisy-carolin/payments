from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from.forms import PaymentRegistrationForm
from django.shortcuts import render
from.models import Payment



def register_payment(request):
    form=PaymentRegistrationForm()
    return render(request,"register_payment.html",{
        "form":form,
        "name":"Daisi Caroline",
    })
def register_payment(request):
    if request.method=="POST":
        form=PaymentRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=PaymentRegistrationForm()
    return render(request,"register_payment.html",{"form":form})

def payment_list(request):
    payments=Payment.objects.all()
    return render(request,"payment_list.html",{ "payments":payments})

def payment_profile(request,id):
    payment=Payment.objects.get(id=id)
    return render(request,"payment_profile.html",{"payment":payment})

def edit_payment(request,id):
    payment=Payment.objects.get(id=id)
    if request.method=="POST":
        form=PaymentRegistrationForm(request.POST,instance=payment)
        if form.is_valid():
             form.save()
             return redirect("payment_profile",id=payment.id)

    else: 
        form=PaymentRegistrationForm(instance=payment) 
        return render(request,"edit_payment.html",{"form":form}) 