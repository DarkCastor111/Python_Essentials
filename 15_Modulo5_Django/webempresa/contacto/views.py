from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactoForm

# Create your views here.

def contacto(request):
    contacto_form = ContactoForm()
    if request.method == 'POST':
        contacto_form = ContactoForm(data=request.POST)
        if contacto_form.is_valid:
            nbr = request.POST.get('nombre', '')
            crr = request.POST.get('correo', '')
            msj = request.POST.get('mensaje', '')

            cor = EmailMessage(
                "Objet : Nouveau message de contact",
                f"Corps du message : De {nbr} <{crr}> \n\nMessage : \n {msj}",
                "nepasrepondre@inbox.mailtrap.io",
                ["tempo.cat13@gmail.com"],
                reply_to=[crr]
            )

            try:
                cor.send()
                # Email enviado, redirreccionamos
                return redirect(reverse("nm_contacto") + "?ok")
            except Exception as e :
                print("Error : ", e)
                return redirect(reverse("nm_contacto") + "?ko")
            
    return render(request, "contacto/contact.html", {'form':contacto_form})