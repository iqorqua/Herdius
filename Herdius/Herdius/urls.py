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
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^test', app.views.test, name='test'),
    url(r'^cabinet', app.views.cabinet, name='cabinet'),
    url(r'^registration', app.views.registration, name='registration'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year
            } 
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', app.views.register, name='register'),
    url(r'^edit/$', app.views.edit, name='edit'),
    url(r'^activate/[0-9,a-z,-]{36}$', app.views.activate, name='activate'),
    url(r'^changepass/[0-9,a-z,-]{72}$', app.views.change_password, name='change_password'),#redirect from email
    url(r'^passchange_req/$', app.views.passchange_req, name='passchange_req'),#creating request in db and send email
    url(r'^passchange/$', app.views.passchange, name='passchange'),#request to change pass for ajax in redirected email link
    url(r'^emailusernamecheck/$', app.views.emailusernamecheck, name='emailusernamecheck'),#request to change pass for ajax in redirected email link
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
