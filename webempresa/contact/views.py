from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage
# Create your views here.
def contact(request):
    #print("Tipo de Peticion: {}",format(request.method))
    contact_form = ContactForm()
    if request.method=="POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name=request.POST.get('name','')
            email=request.POST.get('email','')
            content=request.POST.get('content','')
            #Enviamos el correo y redireccionamos
            email = EmailMessage(
                'La Caffetiera: Nuevo Mensaje de Contacto',
                'De {} <{}>\n\nEscribio:\n\n{}'.format(name,email,content),
                'no-contestar@inbox.mailtrap.io',
                ['luchonarvaez1983@gmail.com'],
                reply_to=[email]
            )
            try:
                email.send()
                # todo ha funcionado bien, redireccionamos a ok
                return redirect(reverse('contact')+"?ok")
            except:
                # Algo no ha ido bien, redireccionar Fail
                return redirect(reverse('contact')+"?fail")

            



    return render(request,"contact/contact.html",{'form':contact_form})