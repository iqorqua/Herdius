"""
Definition of urls for Herdius.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

from django.conf.urls.static import static
from django.conf import settings

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin 
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^development/$', app.views.home, name='home'),
    url(r'^$', app.views.coming_soon, name='comingsoon'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^test', app.views.test, name='test'),
    url(r'^development/cabinet', app.views.cabinet, name='cabinet'),
    url(r'^development/registration', app.views.registration, name='registration'),
    url(r'^development/login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
                'next': getattr(settings, "LOGIN_REDIRECT_URL", None),
            } 
        },
        name='login'),
    url(r'^development/login_remind/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login_with_remind.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
                'next': getattr(settings, "LOGIN_REDIRECT_URL", None),
            } 
        },
        name='login_remind'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^development/admin/', include(admin.site.urls)),
    url(r'^development/register/$', app.views.register, name='register'),
    url(r'^development/edit/$', app.views.edit, name='edit'),
    url(r'^development/activate/[0-9,a-z,-]{36}$', app.views.activate, name='activate'),
    url(r'^development/changepass/[0-9,a-z,-]{72}$', app.views.change_password, name='change_password'),#redirect from email
    url(r'^development/passchange_req/$', app.views.passchange_req, name='passchange_req'),#creating request in db and send email
    url(r'^development/passchange/$', app.views.passchange, name='passchange'),#request to change pass for ajax in redirected email link
    url(r'^development/emailusernamecheck/$', app.views.emailusernamecheck, name='emailusernamecheck'),#request to change pass for ajax in redirected email link
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static('development'+settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
