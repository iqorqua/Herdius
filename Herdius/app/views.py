"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .models import *
import json
import urllib
from django.core.files import File 
from django.conf import settings
from django.http import HttpResponse
from django.http import JsonResponse
from app.django_encrypt_file import EncryptionService, ValidationError
import traceback

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )   

def cabinet(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/cabinet.html',
        {
            'title':'My cabinet',
            'year':datetime.now().year,
        }
    )   

def registration(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/registration.html',
        {
            'title':'Registration',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    ) 

def register(request):
    try:
        assert isinstance(request, HttpRequest)
        print('!!!->' + str(request.POST) + '<-!!!')
        result = 'Something happened wrong :('
        ''' Begin reCAPTCHA validation '''
        recaptcha_response = request.POST.get('recapcha')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
        data = urllib.parse.urlencode(values).encode()
        req =  urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        recapcha = json.loads(response.read().decode())
        ''' End reCAPTCHA validation '''
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        country = request.POST.get('country')
        adress = request.POST.get('adress')
        postal_code = request.POST.get('postal_code')
        phone = request.POST.get('phone')
        bday = request.POST.get('bday')
        if username == '' or first_name == '' or last_name == '' or password == '' or email == '' or country == '' or adress == '' or postal_code == '' or phone == '' or bday == '' or len(request.FILES) != 2:      
            return JsonResponse({'result': 'Error! There some field(s) are missing!'})
        if recapcha['success']:
            try: 
                user = MyUser.objects.create_user(username, email, password, bday = bday)
                user.is_staff = True
                user.first_name = first_name
                user.last_name = last_name
                user.address = adress
                user.postal_code = postal_code
                user.country = country
                user.phone = phone
                user.bday = bday
                user.avatar.save(request.FILES.get('avatar').name, request.FILES.get('avatar'))
                service = EncryptionService(raise_exception=False)
                try:
                   myfile = request.FILES.get('picture_id', None)
                   password = user.password #getattr(settings, "ENCRYPTION_KEY", None)
                   encrypted_file = EncryptionService().encrypt_file(myfile, password, extension='enc')
                   user.encrypted_data = encrypted_file.name
                   user.save()
                except Exception as e:
                   print(e)
                   result = str(e)
                   return JsonResponse({'result': result})
                result = 'Succsessfully created!'
                return JsonResponse({'result': result})
            except Exception as e:
                result = str(e)
                return JsonResponse({'result': result})
        else:
            result = 'Capcha error!'
            return JsonResponse({'result': result})
    except Exception as ex:
        #print('<<' + str(ex)+ '>>')
        print("Exception in user code:")
        print("-"*60)
        traceback.print_exc(file=sys.stdout)
        print("-"*60)
        result = str(ex)
        return JsonResponse({'result': result})
    
def edit(request):
    try:
        assert isinstance(request, HttpRequest)
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        country = request.POST.get('country')
        adress = request.POST.get('adress')
        postal_code = request.POST.get('postal_code')
        phone = request.POST.get('phone')
        bday = request.POST.get('bday')
        if username == '' or first_name == '' or last_name == '' or password == '' or email == '' or country == '' or adress == '' or postal_code == '' or phone == '' or bday == '':      
            return JsonResponse({'result': 'Error! There some field(s) are missing!'})
        user = MyUser.objects.get(username = username)
        user.email = email
        user.bday = bday
        user.first_name = first_name
        user.last_name = last_name
        user.address = adress
        user.postal_code = postal_code
        user.country = country
        user.phone = phone
        user.bday = bday
        if request.FILES.get('avatar'):
            user.avatar.save(request.FILES.get('avatar').name, request.FILES.get('avatar'))
        if request.FILES.get('picture_id'):
            service = EncryptionService(raise_exception=False)
            try:
                   myfile = request.FILES.get('picture_id', None)
                   password = user.password
                   encrypted_file = EncryptionService().encrypt_file(myfile, password, extension='enc')
                   user.encrypted_data = encrypted_file.name
                   user.save()
            except Exception as e:
                   return JsonResponse({'result': str(ex)})
                   
        user.save()
        return JsonResponse({'result': "Done!"})
    except Exception as ex:
        return JsonResponse({'result': str(ex)})
