from django.shortcuts import render, redirect 
from django.urls import reverse  
from django.core.mail import EmailMessage
from .forms import ContactForm


# Create your views here.
def contact(request):
    #CREAMOS LA PLANTILLA VACIA
    contact_form = ContactForm()
    #DETECTAREMOS SI SE A ENVIADO POR POST ALGUN DATO
    if request.method == 'POST':
        #SI SE A ENVIADO RELLENAREMOS ESA PLATILLA CON LA DATA DEL DICCIONARIO POST
        contact_form = ContactForm(data=request.POST)
        #VALIDAMOS CON EL SIG METODO Y SI TOD0 ES CORRECTO REGRESARA UN TRUE
        if contact_form.is_valid():
            #SI TODOS LOS DATOS SON CORRECTOS RECUPERAMOS LOS VALORES Y SI NO TIENE NINGUNO QUE NOS REGRESE UNA CADENA VACIA
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #SI A SALIO BIEN HACEMOS UNA REDIRECCION A LA MISMA PAGINA
            email = EmailMessage(
                'Mi blog personal: nuevo mensaje',
                'de {} <{}>\nMensaje: \n\n {}'.format(name, email, content),
                'no-reply@gmail.com',
                ['misopitas@gmail.com'],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact')+'?ok')
            except:
                return redirect(reverse('contact')+'?fail')

    return render(request, 'contacto/contact.html',{'form':contact_form})
