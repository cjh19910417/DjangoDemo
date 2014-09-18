from django.conf.urls import patterns, include, url

from django.contrib import admin
from Demo.contact.views import contact, contact_thinks
from Demo.views import hello, hours_ahead, display_request_meta
from Demo.views import current_datetime
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoDemo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^hello/$', hello),
    (r'now/$',current_datetime),
    (r'now/plus/(\d{1,2})/$',hours_ahead),
    (r'meta/$',display_request_meta),
    (r'contact/$',contact),
    (r'contact/thinks/$',contact_thinks),
)